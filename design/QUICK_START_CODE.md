# TaskFlow API - Implementation Quick Start Guide

This guide contains code templates and examples to jumpstart development.

---

## PHASE 1: SPRINT MODEL

### File: `domain/sprint/models.py`

```python
from django.db import models
from django.utils import timezone
from domain.common.models import TimeStampedModel
from domain.project.models import Project

class Sprint(TimeStampedModel):
    """Represents a sprint/iteration in a project"""
    
    STATUS_CHOICES = [
        ('planned', 'Planned'),
        ('active', 'Active'),
        ('completed', 'Completed'),
        ('archived', 'Archived'),
    ]
    
    name = models.CharField(max_length=255)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='sprints')
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='planned')
    goal = models.TextField(blank=True, help_text="Sprint goal/objective")
    capacity = models.IntegerField(
        default=0, 
        help_text="Team capacity in story points"
    )
    
    class Meta:
        ordering = ['-start_date']
        unique_together = ('project', 'name')
        indexes = [
            models.Index(fields=['project', '-start_date']),
            models.Index(fields=['status']),
        ]
    
    def __str__(self):
        return f"{self.name} - {self.project.name}"
    
    @property
    def is_active(self):
        return self.status == 'active'
    
    @property
    def days_remaining(self):
        if self.status == 'active':
            return max(0, (self.end_date - timezone.now()).days)
        return 0
    
    @property
    def progress_percent(self):
        if self.start_date >= self.end_date:
            return 0
        total_days = (self.end_date - self.start_date).days
        elapsed_days = (timezone.now() - self.start_date).days
        return min(100, max(0, int((elapsed_days / total_days) * 100)))
    
    def get_metrics(self):
        """Get sprint metrics"""
        tasks = self.tasks.all()
        total_points = tasks.aggregate(total=models.Sum('story_points'))['total'] or 0
        completed_points = tasks.filter(status='done').aggregate(
            total=models.Sum('story_points')
        )['total'] or 0
        
        return {
            'total_tasks': tasks.count(),
            'completed_tasks': tasks.filter(status='done').count(),
            'in_progress_tasks': tasks.filter(status='in_progress').count(),
            'total_story_points': total_points,
            'completed_story_points': completed_points,
            'remaining_story_points': total_points - completed_points,
        }


class SprintMetrics(TimeStampedModel):
    """Stores calculated metrics for a sprint"""
    
    sprint = models.OneToOneField(Sprint, on_delete=models.CASCADE, related_name='metrics')
    
    # Velocity
    burndown_data = models.JSONField(
        default=list,
        help_text="[{date: '2026-06-01', remaining_points: 40}, ...]"
    )
    velocity = models.FloatField(null=True, help_text="Avg story points completed per sprint")
    
    # Rates
    completion_rate = models.FloatField(default=0, help_text="Percentage of tasks completed 0-100")
    on_time_rate = models.FloatField(default=0, help_text="Percentage of tasks completed by due date")
    
    class Meta:
        verbose_name_plural = "Sprint Metrics"
    
    def __str__(self):
        return f"Metrics for {self.sprint.name}"
```

### File: `domain/task/models.py` (additions)

```python
# Add these fields to existing Task model

class Task(TimeStampedModel):
    # ... existing fields ...
    
    # Sprint-related
    sprint = models.ForeignKey(
        'sprint.Sprint',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='tasks'
    )
    story_points = models.IntegerField(
        null=True,
        blank=True,
        help_text="Complexity/effort estimate in points (Fibonacci: 1,2,3,5,8,13,21)"
    )
    estimated_hours = models.FloatField(null=True, blank=True)
    
    # Priority matrix
    priority_quadrant = models.CharField(
        max_length=50,
        choices=[
            ('urgent_important', 'Urgent & Important - Q1'),
            ('not_urgent_important', 'Not Urgent & Important - Q2'),
            ('urgent_not_important', 'Urgent & Not Important - Q3'),
            ('not_urgent_not_important', 'Not Urgent & Not Important - Q4'),
        ],
        null=True,
        blank=True
    )
    
    # Dependencies
    blocked_by = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='blocks',
        blank=True,
        help_text="Tasks that are blocking this task"
    )
```

### File: `services/sprint/serializers.py`

```python
from rest_framework import serializers
from domain.sprint.models import Sprint, SprintMetrics
from domain.task.models import Task

class SprintSerializer(serializers.ModelSerializer):
    task_count = serializers.SerializerMethodField()
    completed_count = serializers.SerializerMethodField()
    total_story_points = serializers.SerializerMethodField()
    completed_story_points = serializers.SerializerMethodField()
    
    class Meta:
        model = Sprint
        fields = [
            'id', 'name', 'project', 'start_date', 'end_date',
            'status', 'goal', 'capacity', 'progress_percent',
            'days_remaining', 'task_count', 'completed_count',
            'total_story_points', 'completed_story_points'
        ]
        read_only_fields = ['created_at', 'updated_at']
    
    def get_task_count(self, obj):
        return obj.tasks.count()
    
    def get_completed_count(self, obj):
        return obj.tasks.filter(status='done').count()
    
    def get_total_story_points(self, obj):
        result = obj.tasks.aggregate(total=models.Sum('story_points'))
        return result['total'] or 0
    
    def get_completed_story_points(self, obj):
        result = obj.tasks.filter(status='done').aggregate(
            total=models.Sum('story_points')
        )
        return result['total'] or 0


class SprintDetailedSerializer(SprintSerializer):
    metrics = serializers.SerializerMethodField()
    tasks_by_status = serializers.SerializerMethodField()
    
    class Meta(SprintSerializer.Meta):
        fields = SprintSerializer.Meta.fields + ['metrics', 'tasks_by_status']
    
    def get_metrics(self, obj):
        metrics = getattr(obj, 'metrics', None)
        if metrics:
            return {
                'velocity': metrics.velocity,
                'completion_rate': metrics.completion_rate,
                'on_time_rate': metrics.on_time_rate,
                'burndown_data': metrics.burndown_data,
            }
        return {}
    
    def get_tasks_by_status(self, obj):
        statuses = ['backlog', 'in_progress', 'under_review', 'changes_requested', 'done']
        result = {}
        for status in statuses:
            tasks = obj.tasks.filter(status=status)
            result[status] = TaskSerializer(tasks, many=True).data
        return result
```

### File: `api/sprint/views.py`

```python
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from domain.sprint.models import Sprint
from domain.project.models import Project
from services.sprint.serializers import SprintSerializer, SprintDetailedSerializer

class SprintViewSet(viewsets.ModelViewSet):
    """
    API endpoints for Sprint management
    
    list - GET /api/v1/projects/{project_id}/sprints/
    create - POST /api/v1/projects/{project_id}/sprints/
    retrieve - GET /api/v1/sprints/{sprint_id}/
    update - PUT /api/v1/sprints/{sprint_id}/
    partial_update - PATCH /api/v1/sprints/{sprint_id}/
    destroy - DELETE /api/v1/sprints/{sprint_id}/
    """
    
    permission_classes = [IsAuthenticated]
    serializer_class = SprintSerializer
    
    def get_queryset(self):
        project_id = self.kwargs.get('project_id')
        if project_id:
            return Sprint.objects.filter(project_id=project_id).select_related('project')
        sprint_id = self.kwargs.get('pk')
        if sprint_id:
            return Sprint.objects.filter(id=sprint_id)
        return Sprint.objects.none()
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return SprintDetailedSerializer
        return SprintSerializer
    
    def create(self, request, *args, **kwargs):
        project_id = kwargs.get('project_id')
        project = get_object_or_404(Project, id=project_id)
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(project=project)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    @action(detail=True, methods=['post'])
    def start(self, request, *args, **kwargs):
        sprint = self.get_object()
        if sprint.status != 'planned':
            return Response(
                {'error': 'Only planned sprints can be started'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        sprint.status = 'active'
        sprint.save()
        return Response(SprintDetailedSerializer(sprint).data)
    
    @action(detail=True, methods=['post'])
    def complete(self, request, *args, **kwargs):
        sprint = self.get_object()
        if sprint.status != 'active':
            return Response(
                {'error': 'Only active sprints can be completed'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        sprint.status = 'completed'
        sprint.save()
        
        # Generate final metrics
        metrics = sprint.get_metrics()
        
        return Response({
            'sprint': SprintDetailedSerializer(sprint).data,
            'final_metrics': metrics
        })
    
    @action(detail=True, methods=['get'])
    def metrics(self, request, *args, **kwargs):
        sprint = self.get_object()
        metrics = sprint.get_metrics()
        return Response(metrics)
```

---

## PHASE 2: PRIORITY MATRIX

### File: `domain/task/services/priority_service.py`

```python
from django.db.models import Q, Count
from django.utils import timezone
from domain.task.models import Task

class PriorityMatrixService:
    """Calculates and manages task priority quadrants"""
    
    URGENCY_THRESHOLD = 50
    IMPORTANCE_THRESHOLD = 50
    
    @staticmethod
    def calculate_priority_scores(task: Task) -> dict:
        """
        Calculate urgency and importance scores for a task.
        Returns: {urgency_score, importance_score, quadrant}
        """
        urgency = PriorityMatrixService._calculate_urgency(task)
        importance = PriorityMatrixService._calculate_importance(task)
        quadrant = PriorityMatrixService._determine_quadrant(urgency, importance)
        
        return {
            'urgency_score': urgency,
            'importance_score': importance,
            'quadrant': quadrant
        }
    
    @staticmethod
    def _calculate_urgency(task: Task) -> int:
        """Calculate urgency score (0-100)"""
        score = 0
        
        # Due date proximity (0-40 points)
        if task.due_date:
            days_until_due = (task.due_date - timezone.now()).days
            if days_until_due < 0:  # Overdue
                score += 40
            elif days_until_due <= 3:
                score += 35
            elif days_until_due <= 7:
                score += 25
            elif days_until_due <= 14:
                score += 15
            else:
                score += 5
        
        # Blocking other tasks (0-30 points)
        blocked_count = task.blocks.count()
        if blocked_count > 0:
            score += min(30, blocked_count * 8)
        
        # Is being blocked (0-20 points)
        if task.blocked_by.exists():
            score += 10
        
        # Priority flag (0-10 points)
        if task.priority == 'high':
            score += 10
        elif task.priority == 'medium':
            score += 5
        
        return min(100, score)
    
    @staticmethod
    def _calculate_importance(task: Task) -> int:
        """Calculate importance score (0-100)"""
        score = 0
        
        # Story points (0-30 points)
        if task.story_points:
            score += min(30, task.story_points * 2)
        
        # Number of tasks this blocks (0-25 points)
        blocked_count = task.blocks.count()
        score += min(25, blocked_count * 5)
        
        # Task type/category (0-25 points)
        if task.task_type in ['bug', 'security', 'critical']:
            score += 25
        elif task.task_type == 'feature':
            score += 15
        
        # Has subtasks (0-20 points)
        subtask_count = task.subtasks.count() if hasattr(task, 'subtasks') else 0
        if subtask_count > 0:
            score += min(20, subtask_count * 5)
        
        return min(100, score)
    
    @staticmethod
    def _determine_quadrant(urgency: int, importance: int) -> str:
        """Determine quadrant based on scores"""
        if urgency >= PriorityMatrixService.URGENCY_THRESHOLD and \
           importance >= PriorityMatrixService.IMPORTANCE_THRESHOLD:
            return 'urgent_important'  # Q1: Do First
        elif urgency < PriorityMatrixService.URGENCY_THRESHOLD and \
             importance >= PriorityMatrixService.IMPORTANCE_THRESHOLD:
            return 'not_urgent_important'  # Q2: Schedule
        elif urgency >= PriorityMatrixService.URGENCY_THRESHOLD and \
             importance < PriorityMatrixService.IMPORTANCE_THRESHOLD:
            return 'urgent_not_important'  # Q3: Delegate
        else:
            return 'not_urgent_not_important'  # Q4: Eliminate
    
    @staticmethod
    def recalculate_project_priorities(project):
        """Batch recalculate priorities for all tasks in a project"""
        tasks = Task.objects.filter(project=project)
        
        for task in tasks:
            scores = PriorityMatrixService.calculate_priority_scores(task)
            task.priority_quadrant = scores['quadrant']
            task.save()
        
        return tasks.count()
```

---

## PHASE 3: SWIMLANES

### File: `domain/sprint/models.py` (additions)

```python
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Swimlane(TimeStampedModel):
    """Organizes tasks by team, epic, or feature area"""
    
    TYPE_CHOICES = [
        ('team', 'Team'),
        ('epic', 'Epic'),
        ('feature_area', 'Feature Area'),
        ('component', 'Component'),
    ]
    
    sprint = models.ForeignKey(Sprint, on_delete=models.CASCADE, related_name='swimlanes')
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    description = models.TextField(blank=True)
    color = models.CharField(max_length=7, default='#3498db')  # Hex color
    order = models.IntegerField(default=0)
    
    # Generic relation to Team, Epic, etc
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    object_id = models.PositiveIntegerField(null=True, blank=True)
    content_object = GenericForeignKey('content_type', 'object_id')
    
    class Meta:
        ordering = ['sprint', 'order', 'name']
        unique_together = ('sprint', 'name')
    
    def __str__(self):
        return f"{self.sprint.name} - {self.name}"
    
    def get_tasks(self):
        return self.tasks.all()
    
    def get_task_count_by_status(self):
        return self.tasks.values('status').annotate(count=Count('id'))
```

---

## DATABASE MIGRATIONS

### File: `domain/sprint/migrations/0001_initial.py`

```python
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sprint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('status', models.CharField(choices=[('planned', 'Planned'), ('active', 'Active'), ('completed', 'Completed'), ('archived', 'Archived')], default='planned', max_length=20)),
                ('goal', models.TextField(blank=True)),
                ('capacity', models.IntegerField(default=0, help_text='Team capacity in story points')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sprints', to='project.project')),
            ],
            options={
                'ordering': ['-start_date'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='sprint',
            unique_together={('project', 'name')},
        ),
        migrations.AddIndex(
            model_name='sprint',
            index=models.Index(fields=['project', '-start_date'], name='sprint_project_idx'),
        ),
        migrations.AddIndex(
            model_name='sprint',
            index=models.Index(fields=['status'], name='sprint_status_idx'),
        ),
    ]
```

---

## TESTS EXAMPLE

### File: `tests/domain/sprint/test_models.py`

```python
import pytest
from django.utils import timezone
from datetime import timedelta
from domain.sprint.models import Sprint
from domain.project.models import Project

@pytest.mark.django_db
class TestSprint:
    
    @pytest.fixture
    def project(self):
        return Project.objects.create(name="Test Project")
    
    @pytest.fixture
    def sprint(self, project):
        return Sprint.objects.create(
            name="Sprint 1",
            project=project,
            start_date=timezone.now(),
            end_date=timezone.now() + timedelta(days=14),
            goal="Implement auth",
            capacity=40
        )
    
    def test_sprint_creation(self, sprint):
        assert sprint.name == "Sprint 1"
        assert sprint.is_active == False
        assert sprint.capacity == 40
    
    def test_sprint_status_transitions(self, sprint):
        assert sprint.status == 'planned'
        
        sprint.status = 'active'
        sprint.save()
        assert sprint.is_active == True
    
    def test_progress_percent(self, sprint):
        # Sprint just started
        assert sprint.progress_percent == 0
    
    def test_unique_sprint_name_per_project(self, project):
        Sprint.objects.create(
            name="Duplicate Sprint",
            project=project,
            start_date=timezone.now(),
            end_date=timezone.now() + timedelta(days=14)
        )
        
        with pytest.raises(Exception):  # IntegrityError
            Sprint.objects.create(
                name="Duplicate Sprint",
                project=project,
                start_date=timezone.now(),
                end_date=timezone.now() + timedelta(days=14)
            )
```

---

## QUICK SETUP CHECKLIST

- [ ] Copy models to `domain/sprint/models.py`
- [ ] Copy models additions to `domain/task/models.py`
- [ ] Copy serializers to `services/sprint/serializers.py`
- [ ] Copy viewsets to `api/sprint/views.py`
- [ ] Copy priority service to `domain/task/services/priority_service.py`
- [ ] Create and run migrations
- [ ] Register viewsets in `api/urls.py`
- [ ] Write and run tests
- [ ] Update API documentation

---

## COMMON PATTERNS

### Creating a Sprint
```python
from domain.sprint.models import Sprint
from datetime import timedelta

sprint = Sprint.objects.create(
    name="Sprint 1",
    project_id=1,
    start_date=timezone.now(),
    end_date=timezone.now() + timedelta(days=14),
    goal="Implement authentication",
    capacity=40
)
```

### Getting Sprint Metrics
```python
sprint = Sprint.objects.get(id=1)
metrics = sprint.get_metrics()
# Returns: {total_tasks, completed_tasks, total_story_points, ...}
```

### Calculating Task Priority
```python
from domain.task.services.priority_service import PriorityMatrixService

task = Task.objects.get(id=1)
scores = PriorityMatrixService.calculate_priority_scores(task)
# Returns: {urgency_score, importance_score, quadrant}
```

### Batch Update Priorities
```python
from domain.task.services.priority_service import PriorityMatrixService

count = PriorityMatrixService.recalculate_project_priorities(project)
print(f"Updated {count} tasks")
```

This code should give you a solid foundation to begin implementation!
