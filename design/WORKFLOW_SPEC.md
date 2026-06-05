# TaskFlow API - Enhanced Workflow Specification

## Overview
This document defines the enhanced workflow system for TaskFlow API, implementing **Scrumban + Quad Priority Matrix** to improve user experience and team productivity.

---

## PHASE 1: SCRUMBAN IMPLEMENTATION

### 1.1 Sprint Management

#### Models to Add/Modify
```python
# NEW: domain/sprint/models.py
from django.db import models
from domain.project.models import Project
from domain.common.models import TimeStampedModel

class Sprint(TimeStampedModel):
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
    goal = models.TextField(blank=True)
    capacity = models.IntegerField(default=0, help_text="Team capacity in story points")
    
    class Meta:
        ordering = ['-start_date']
        unique_together = ('project', 'name')
    
    def __str__(self):
        return f"{self.name} - {self.project.name}"

# MODIFY: domain/task/models.py
class Task(TimeStampedModel):
    PRIORITY_QUADRANT_CHOICES = [
        ('urgent_important', 'Urgent & Important'),      # Q1: DO FIRST
        ('not_urgent_important', 'Not Urgent & Important'),   # Q2: SCHEDULE
        ('urgent_not_important', 'Urgent & Not Important'),   # Q3: DELEGATE
        ('not_urgent_not_important', 'Not Urgent & Not Important'),# Q4: ELIMINATE
    ]
    
    # ... existing fields ...
    sprint = models.ForeignKey(Sprint, null=True, blank=True, on_delete=models.SET_NULL, related_name='tasks')
    story_points = models.IntegerField(null=True, blank=True, default=None)
    priority_quadrant = models.CharField(max_length=50, choices=PRIORITY_QUADRANT_CHOICES, null=True, blank=True)
    estimated_hours = models.FloatField(null=True, blank=True)
    blocked_by = models.ManyToManyField('self', symmetrical=False, related_name='blocks', blank=True)
```

#### API Endpoints to Add
```
# Sprint Management
POST   /api/v1/projects/{project_id}/sprints/
GET    /api/v1/projects/{project_id}/sprints/
GET    /api/v1/sprints/{sprint_id}/
PUT    /api/v1/sprints/{sprint_id}/
PATCH  /api/v1/sprints/{sprint_id}/
DELETE /api/v1/sprints/{sprint_id}/

# Sprint Tasks
GET    /api/v1/sprints/{sprint_id}/tasks/
POST   /api/v1/sprints/{sprint_id}/tasks/
PUT    /api/v1/sprints/{sprint_id}/tasks/{task_id}/move/

# Sprint Metrics & Operations
GET    /api/v1/sprints/{sprint_id}/metrics/
GET    /api/v1/sprints/{sprint_id}/burndown/
POST   /api/v1/sprints/{sprint_id}/complete/
POST   /api/v1/sprints/{sprint_id}/start/
```

#### Serializers
```python
# services/sprint/serializers.py

class SprintSerializer(serializers.ModelSerializer):
    task_count = serializers.SerializerMethodField()
    completed_count = serializers.SerializerMethodField()
    total_story_points = serializers.SerializerMethodField()
    completed_story_points = serializers.SerializerMethodField()
    in_progress_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Sprint
        fields = [
            'id', 'name', 'project', 'start_date', 'end_date', 
            'status', 'goal', 'capacity', 'task_count', 
            'completed_count', 'in_progress_count',
            'total_story_points', 'completed_story_points',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']
    
    def get_task_count(self, obj):
        return obj.tasks.count()
    
    def get_completed_count(self, obj):
        return obj.tasks.filter(status='done').count()
    
    def get_in_progress_count(self, obj):
        return obj.tasks.filter(status='in_progress').count()
    
    def get_total_story_points(self, obj):
        return obj.tasks.aggregate(total=models.Sum('story_points'))['total'] or 0
    
    def get_completed_story_points(self, obj):
        return obj.tasks.filter(status='done').aggregate(total=models.Sum('story_points'))['total'] or 0


class SprintDetailedSerializer(SprintSerializer):
    tasks = TaskSerializer(many=True, read_only=True)
    metrics = serializers.SerializerMethodField()
    
    class Meta(SprintSerializer.Meta):
        fields = SprintSerializer.Meta.fields + ['tasks', 'metrics']
    
    def get_metrics(self, obj):
        return {
            'velocity': calculate_velocity(obj),
            'completion_rate': calculate_completion_rate(obj),
            'burndown_data': generate_burndown_data(obj),
        }


class TaskWithSprintSerializer(TaskSerializer):
    sprint = SprintSerializer(read_only=True)
    story_points = serializers.IntegerField(required=False)
    estimated_hours = serializers.FloatField(required=False)
    priority_quadrant = serializers.CharField(required=False)
```

---

## PHASE 2: PRIORITY QUADRANT MATRIX

### 2.1 Priority Matrix Service

```python
# domain/task/services/priority_service.py

class PriorityMatrixService:
    """
    Calculates and manages task priority quadrants using urgency and importance scores.
    
    Quadrants:
    Q1: Urgent & Important  (Do First)
    Q2: Not Urgent & Important (Schedule)
    Q3: Urgent & Not Important (Delegate)
    Q4: Not Urgent & Not Important (Eliminate)
    """
    
    @staticmethod
    def calculate_priority_scores(task: Task) -> dict:
        """
        Returns {'urgency': 0-100, 'importance': 0-100}
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
        """
        Factors: due date proximity, blocking status, priority flag, client-facing
        """
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
        if task.blocks.exists():
            blocked_count = task.blocks.count()
            score += min(30, blocked_count * 5)
        
        # Is being blocked (0-20 points)
        if task.blocked_by.exists():
            score += 10
        
        # Priority level (0-10 points)
        if task.priority == 'high':
            score += 10
        elif task.priority == 'medium':
            score += 5
        
        return min(100, score)
    
    @staticmethod
    def _calculate_importance(task: Task) -> int:
        """
        Factors: story points, blocking impact, dependencies, business value
        """
        score = 0
        
        # Story points (0-30 points)
        if task.story_points:
            score += min(30, task.story_points * 2)
        
        # Number of dependencies (0-25 points)
        blocked_count = task.blocks.count()
        score += min(25, blocked_count * 5)
        
        # Task type/category (0-25 points)
        if task.task_type in ['bug', 'security', 'critical']:
            score += 25
        elif task.task_type == 'feature':
            score += 15
        
        # Has sub-tasks (0-20 points)
        if task.subtasks.exists():
            score += min(20, task.subtasks.count() * 5)
        
        return min(100, score)
    
    @staticmethod
    def _determine_quadrant(urgency: int, importance: int) -> str:
        """Determine quadrant based on scores (thresholds: 50)"""
        if urgency >= 50 and importance >= 50:
            return 'urgent_important'  # Q1
        elif urgency < 50 and importance >= 50:
            return 'not_urgent_important'  # Q2
        elif urgency >= 50 and importance < 50:
            return 'urgent_not_important'  # Q3
        else:
            return 'not_urgent_not_important'  # Q4
    
    @staticmethod
    def recalculate_all_tasks_in_project(project: Project):
        """Batch recalculate priorities for all tasks in a project"""
        for task in project.tasks.all():
            scores = PriorityMatrixService.calculate_priority_scores(task)
            task.priority_quadrant = scores['quadrant']
            task.save()
```

### 2.2 Priority Matrix API Endpoints

```python
# api/task/views.py

class PriorityMatrixViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoints for priority matrix view
    GET /api/v1/projects/{project_id}/priority-matrix/
    GET /api/v1/projects/{project_id}/priority-matrix/Q1/
    """
    
    def get_queryset(self):
        project_id = self.kwargs['project_id']
        return Task.objects.filter(project_id=project_id)
    
    @action(detail=False, methods=['get'])
    def by_quadrant(self, request, project_id=None):
        """Get tasks grouped by quadrant"""
        tasks = self.get_queryset()
        
        quadrants = {
            'Q1_urgent_important': tasks.filter(priority_quadrant='urgent_important'),
            'Q2_not_urgent_important': tasks.filter(priority_quadrant='not_urgent_important'),
            'Q3_urgent_not_important': tasks.filter(priority_quadrant='urgent_not_important'),
            'Q4_not_urgent_not_important': tasks.filter(priority_quadrant='not_urgent_not_important'),
        }
        
        data = {
            quadrant: TaskSerializer(qs, many=True).data 
            for quadrant, qs in quadrants.items()
        }
        
        return Response(data)
    
    @action(detail=False, methods=['post'])
    def recalculate(self, request, project_id=None):
        """Recalculate priority matrix for all tasks in project"""
        project = Project.objects.get(id=project_id)
        PriorityMatrixService.recalculate_all_tasks_in_project(project)
        return Response({'status': 'recalculated'})
```

---

## PHASE 3: SWIMLANES (Team/Epic View)

### 3.1 Swimlane Model

```python
# domain/sprint/models.py

class Swimlane(TimeStampedModel):
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
    
    # Link to related object (Team, Epic, etc)
    content_type = models.ForeignKey(
        ContentType, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True
    )
    object_id = models.PositiveIntegerField(null=True, blank=True)
    
    class Meta:
        ordering = ['sprint', 'order', 'name']
        unique_together = ('sprint', 'name')
    
    def __str__(self):
        return f"{self.sprint.name} - {self.name}"


# Modify Task model to add swimlane
class Task(TimeStampedModel):
    # ... existing fields ...
    swimlane = models.ForeignKey(Swimlane, null=True, blank=True, on_delete=models.SET_NULL, related_name='tasks')
```

### 3.2 Swimlane Serializers

```python
# services/sprint/serializers.py

class SwimlaneSerializer(serializers.ModelSerializer):
    task_count = serializers.SerializerMethodField()
    tasks_by_status = serializers.SerializerMethodField()
    
    class Meta:
        model = Swimlane
        fields = [
            'id', 'sprint', 'name', 'type', 'description', 
            'color', 'order', 'task_count', 'tasks_by_status'
        ]
    
    def get_task_count(self, obj):
        return obj.tasks.count()
    
    def get_tasks_by_status(self, obj):
        """Return tasks grouped by status"""
        from domain.task.models import Task
        
        statuses = [choice[0] for choice in Task.STATUS_CHOICES]
        return {
            status: TaskSerializer(
                obj.tasks.filter(status=status), 
                many=True
            ).data
            for status in statuses
        }


class SprintWithSwimlanesSerializer(SprintDetailedSerializer):
    swimlanes = SwimlaneSerializer(many=True, read_only=True)
    
    class Meta(SprintDetailedSerializer.Meta):
        fields = SprintDetailedSerializer.Meta.fields + ['swimlanes']
```

---

## PHASE 4: TIME-BLOCKING & CAPACITY PLANNING

### 4.1 Task Time Estimation Model

```python
# domain/task/models.py

class TaskTimeEstimate(TimeStampedModel):
    task = models.OneToOneField(Task, on_delete=models.CASCADE, related_name='time_estimate')
    
    # Estimates
    estimated_hours = models.FloatField(
        help_text="Estimated hours to complete",
        null=True,
        blank=True
    )
    estimated_days = models.IntegerField(
        help_text="Estimated days to complete",
        null=True,
        blank=True
    )
    
    # Actuals
    actual_hours = models.FloatField(null=True, blank=True)
    actual_days = models.IntegerField(null=True, blank=True)
    
    # Timeline
    started_at = models.DateTimeField(null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    
    # Metrics
    estimation_accuracy = models.FloatField(
        null=True, 
        blank=True,
        help_text="actual/estimated ratio"
    )
    
    class Meta:
        verbose_name = "Task Time Estimate"
        verbose_name_plural = "Task Time Estimates"
    
    def calculate_accuracy(self):
        """Calculate estimation accuracy"""
        if self.estimated_hours and self.actual_hours:
            return round(self.actual_hours / self.estimated_hours, 2)
        return None
    
    def save(self, *args, **kwargs):
        self.estimation_accuracy = self.calculate_accuracy()
        super().save(*args, **kwargs)


class SprintMetrics(TimeStampedModel):
    sprint = models.OneToOneField(Sprint, on_delete=models.CASCADE, related_name='metrics')
    
    # Velocity data
    burndown_data = models.JSONField(
        default=list,
        help_text="List of {date, remaining_points}"
    )
    velocity = models.FloatField(
        null=True,
        help_text="Average story points completed per sprint"
    )
    
    # Rates
    completion_rate = models.FloatField(
        default=0,
        help_text="Percentage of tasks completed"
    )
    on_time_rate = models.FloatField(
        default=0,
        help_text="Percentage of tasks completed by due date"
    )
    
    class Meta:
        verbose_name_plural = "Sprint Metrics"
```

### 4.2 Capacity Planning Service

```python
# domain/sprint/services/capacity_service.py

class CapacityPlanningService:
    """Manages team capacity and workload distribution"""
    
    @staticmethod
    def get_team_workload(sprint: Sprint, user: User) -> dict:
        """
        Get user's workload for a sprint
        Returns total hours, available hours, utilization %
        """
        tasks = sprint.tasks.filter(assigned_to=user)
        
        total_estimated_hours = sum(
            t.time_estimate.estimated_hours or 0 
            for t in tasks
        )
        
        # Assume 8 hour work days, 5 work days per week
        available_hours = calculate_business_days(sprint.start_date, sprint.end_date) * 8
        
        utilization_percent = (total_estimated_hours / available_hours * 100) if available_hours > 0 else 0
        
        return {
            'user_id': user.id,
            'user_name': user.name,
            'total_estimated_hours': total_estimated_hours,
            'available_hours': available_hours,
            'utilization_percent': utilization_percent,
            'is_overloaded': utilization_percent > 100,
            'tasks': TaskSerializer(tasks, many=True).data
        }
    
    @staticmethod
    def get_sprint_capacity(sprint: Sprint) -> dict:
        """Get overall sprint capacity and utilization"""
        team_members = sprint.project.team_members.all()
        workloads = [CapacityPlanningService.get_team_workload(sprint, user) for user in team_members]
        
        total_capacity = sum(w['available_hours'] for w in workloads)
        total_planned = sum(w['total_estimated_hours'] for w in workloads)
        
        return {
            'total_team_capacity_hours': total_capacity,
            'total_planned_hours': total_planned,
            'utilization_percent': (total_planned / total_capacity * 100) if total_capacity > 0 else 0,
            'team_workload': workloads,
            'status': 'healthy' if (total_planned / total_capacity) < 0.9 else 'at_capacity' if (total_planned / total_capacity) < 1.0 else 'overloaded'
        }
```

---

## API Response Examples

### Sprint Overview with Metrics
```json
{
  "id": 1,
  "name": "Sprint 1 - Authentication",
  "project_id": 1,
  "start_date": "2026-06-01T00:00:00Z",
  "end_date": "2026-06-14T23:59:59Z",
  "status": "active",
  "goal": "Implement user authentication and authorization",
  "capacity": 40,
  "task_count": 15,
  "completed_count": 8,
  "in_progress_count": 4,
  "total_story_points": 40,
  "completed_story_points": 18,
  "metrics": {
    "velocity": 35.5,
    "completion_rate": 53.3,
    "on_time_rate": 92.0,
    "burndown": [
      {"date": "2026-06-01", "remaining": 40},
      {"date": "2026-06-02", "remaining": 38},
      {"date": "2026-06-03", "remaining": 35},
      {"date": "2026-06-04", "remaining": 32}
    ]
  }
}
```

### Priority Matrix View
```json
{
  "Q1_urgent_important": [
    {
      "id": 101,
      "title": "Design Login UI",
      "priority_quadrant": "urgent_important",
      "urgency_score": 85,
      "importance_score": 90,
      "status": "in_progress",
      "assigned_to": "Sarah",
      "due_date": "2026-06-05"
    }
  ],
  "Q2_not_urgent_important": [
    {
      "id": 102,
      "title": "API Documentation",
      "priority_quadrant": "not_urgent_important",
      "urgency_score": 30,
      "importance_score": 75,
      "status": "backlog"
    }
  ],
  "Q3_urgent_not_important": [...],
  "Q4_not_urgent_not_important": [...]
}
```

### Team Capacity Plan
```json
{
  "sprint_id": 1,
  "total_team_capacity_hours": 320,
  "total_planned_hours": 285,
  "utilization_percent": 89.1,
  "status": "healthy",
  "team_workload": [
    {
      "user_id": 1,
      "user_name": "Sarah Johnson",
      "total_estimated_hours": 40,
      "available_hours": 40,
      "utilization_percent": 100,
      "is_overloaded": false
    },
    {
      "user_id": 2,
      "user_name": "John Doe",
      "total_estimated_hours": 32,
      "available_hours": 40,
      "utilization_percent": 80,
      "is_overloaded": false
    }
  ]
}
```

---

## Database Migrations

```sql
-- Add Sprint table
CREATE TABLE sprint (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    project_id INT NOT NULL REFERENCES project(id),
    start_date TIMESTAMP NOT NULL,
    end_date TIMESTAMP NOT NULL,
    status VARCHAR(20) DEFAULT 'planned',
    goal TEXT,
    capacity INT DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(project_id, name)
);

-- Add Swimlane table
CREATE TABLE swimlane (
    id SERIAL PRIMARY KEY,
    sprint_id INT NOT NULL REFERENCES sprint(id),
    name VARCHAR(255) NOT NULL,
    type VARCHAR(20) NOT NULL,
    description TEXT,
    color VARCHAR(7) DEFAULT '#3498db',
    order_index INT DEFAULT 0,
    content_type_id INT,
    object_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(sprint_id, name)
);

-- Modify Task table
ALTER TABLE task 
ADD COLUMN sprint_id INT REFERENCES sprint(id),
ADD COLUMN swimlane_id INT REFERENCES swimlane(id),
ADD COLUMN story_points INT,
ADD COLUMN priority_quadrant VARCHAR(50),
ADD COLUMN estimated_hours FLOAT,
ADD COLUMN blocked_by_task_id INT REFERENCES task(id);

-- Add TaskTimeEstimate table
CREATE TABLE task_time_estimate (
    id SERIAL PRIMARY KEY,
    task_id INT NOT NULL UNIQUE REFERENCES task(id),
    estimated_hours FLOAT,
    estimated_days INT,
    actual_hours FLOAT,
    actual_days INT,
    started_at TIMESTAMP,
    completed_at TIMESTAMP,
    estimation_accuracy FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Add SprintMetrics table
CREATE TABLE sprint_metrics (
    id SERIAL PRIMARY KEY,
    sprint_id INT NOT NULL UNIQUE REFERENCES sprint(id),
    burndown_data JSONB DEFAULT '[]',
    velocity FLOAT,
    completion_rate FLOAT DEFAULT 0,
    on_time_rate FLOAT DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Add indexes for performance
CREATE INDEX idx_task_sprint ON task(sprint_id);
CREATE INDEX idx_task_swimlane ON task(swimlane_id);
CREATE INDEX idx_task_priority_quadrant ON task(priority_quadrant);
CREATE INDEX idx_swimlane_sprint ON swimlane(sprint_id);
CREATE INDEX idx_sprint_project ON sprint(project_id);
```

---

## Implementation Roadmap

**Phase 1 (Weeks 1-2): Core Scrumban**
- [ ] Create Sprint model and migrations
- [ ] Create Sprint ViewSet and serializers
- [ ] Modify Task model to include sprint
- [ ] Create SprintBoard UI component
- [ ] API tests for sprint endpoints

**Phase 2 (Weeks 3-4): Priority Matrix**
- [ ] Implement PriorityMatrixService
- [ ] Create priority scoring algorithm
- [ ] Add priority_quadrant to Task model
- [ ] Create PriorityMatrix API endpoints
- [ ] Create PriorityMatrix UI component
- [ ] Batch recalculation job

**Phase 3 (Weeks 5-6): Swimlanes**
- [ ] Create Swimlane model and migrations
- [ ] Create Swimlane serializers
- [ ] Create SwimlaneBoardView component
- [ ] Integrate with SprintBoard
- [ ] Add workload visualization

**Phase 4 (Weeks 7-8): Time-Blocking**
- [ ] Create TaskTimeEstimate model
- [ ] Create CapacityPlanningService
- [ ] Create calendar view UI
- [ ] Create burndown chart visualization
- [ ] Add workload balancing features

---

## Success Metrics

- ⭐ User satisfaction: 4.0 → 5.0+
- 📈 Adoption rate: 60% → 95%+
- ⏱️ Admin overhead: 30% reduction
- 🚀 Team productivity: 40% increase
- 📅 Missed deadlines: 20% reduction
