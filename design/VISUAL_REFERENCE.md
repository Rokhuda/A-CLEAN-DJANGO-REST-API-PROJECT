# TaskFlow API - Visual Reference & Quick Guide

## 🎨 Design System at a Glance

### Priority Quadrants Color Coding
```
┌──────────────────────────────────────────┐
│        PRIORITY MATRIX                   │
├──────────────────┬──────────────────────┤
│                  │                      │
│  Q1 🔴 RED       │  Q2 🟡 YELLOW       │
│  Urgent &        │  Not Urgent &       │
│  Important       │  Important          │
│  DO FIRST        │  SCHEDULE           │
│                  │                      │
├──────────────────┼──────────────────────┤
│                  │                      │
│  Q3 🟠 ORANGE    │  Q4 ⚪ GRAY          │
│  Urgent &        │  Not Urgent &       │
│  Not Important   │  Not Important      │
│  DELEGATE        │  ELIMINATE          │
│                  │                      │
└──────────────────┴──────────────────────┘
```

### Task Status Colors
```
| Status | Color | Hex |
|--------|-------|-----|
| Backlog | Gray | #ecf0f1 |
| In Progress | Blue | #3498db |
| Under Review | Purple | #9b59b6 |
| Changes Requested | Orange | #e67e22 |
| Done | Green | #27ae60 |
```

---

## 📱 UI Components

### 1. Sprint Selector
```
┌─────────────────────┐
│ Sprint: [Sprint 1 ▼] │ ← Click to change
│ Status: Active       │
│ Days Remaining: 8    │
└─────────────────────┘
```

### 2. Task Card (Kanban View)
```
┌─────────────────────────┐
│ Design Login Form       │ ← Title
│ [Q1 🔴] [5 pts] [Jun 5] │ ← Priority, Points, Due Date
├─────────────────────────┤
│ Sarah Johnson (Assigned) │ ← Assigned to
│ In Progress             │ ← Status
│ Blocks: #8, #10         │ ← Dependencies (if any)
│                         │
│ [View] [Edit] [Move]    │ ← Quick actions
└─────────────────────────┘
```

### 3. Team Workload Indicator
```
Sarah:  [████████░░] 100% (40/40 hrs)
John:   [██████░░░░] 80% (32/40 hrs)
Jane:   [████████░░] 95% (38/40 hrs)
Mike:   [░░░░░░░░░░] 10% (4/40 hrs)
```

### 4. Sprint Metrics Mini-Dashboard
```
┌──────────────────────────────┐
│ Total Tasks: 15              │
│ Completed: 8 (53%)           │
│ Story Points: 40 / 18        │
│ Velocity: 35.5 pts/sprint    │
│ On-Time Rate: 92%            │
└──────────────────────────────┘
```

---

## 🔄 User Workflows

### Workflow 1: Sprint Planning
```
1. Create Sprint
   ↓
2. Set goal & capacity
   ↓
3. Add tasks to backlog
   ↓
4. Assign story points
   ↓
5. Create swimlanes (teams)
   ↓
6. Assign tasks to swimlanes
   ↓
7. Start sprint
```

### Workflow 2: Daily Standup
```
1. Open Sprint Board
   ↓
2. Review burndown chart
   ↓
3. Check at-risk tasks (red indicators)
   ↓
4. Verify team workload
   ↓
5. Discuss blockers
```

### Workflow 3: Prioritization (Weekly)
```
1. Go to Priority Matrix
   ↓
2. Review tasks in Q1 (urgent & important)
   ↓
3. Move completed → Done
   ↓
4. Recalculate priorities
   ↓
5. Review Q2 for next sprint
```

### Workflow 4: Resource Allocation
```
1. View Capacity Plan
   ↓
2. Check team utilization (%)
   ↓
3. If >100%: Move tasks to less-loaded team
   ↓
4. If <70%: Add tasks from backlog
   ↓
5. Rebalance until optimal (80-95%)
```

---

## 🗂️ Navigation Map

```
MAIN MENU
├── Dashboard
│   ├── Quick Stats
│   ├── Recent Tasks
│   └── Upcoming Deadlines
│
├── Sprints (NEW)
│   ├── Active Sprint
│   │   ├── Board View
│   │   ├── Priority Matrix
│   │   ├── Swimlanes
│   │   ├── Calendar
│   │   ├── Analytics
│   │   └── Team Capacity
│   ├── Planned Sprints
│   ├── Completed Sprints
│   └── Create Sprint
│
├── Projects
│   ├── Project List
│   ├── Project Details
│   └── Project Settings
│
├── Tasks
│   ├── My Tasks
│   ├── All Tasks
│   ├── By Priority
│   ├── By Team
│   └── Overdue
│
└── Reports (NEW)
    ├── Sprint Velocity
    ├── Team Performance
    ├── Estimation Accuracy
    └── Risk Analysis
```

---

## 📊 Key Metrics Explained

### Velocity
**What**: Average story points completed per sprint
**Example**: If you complete 35 points on average, velocity = 35
**Use**: Predict how much work can fit in next sprint

### Burndown Chart
**What**: Line showing remaining work (Y-axis) over days (X-axis)
**Ideal**: Line slopes down from left to right
**Red Flag**: Burndown line going UP (indicates added work)

### Completion Rate
**What**: Percentage of tasks finished
**Example**: 8 of 15 tasks done = 53% completion
**Target**: >90% by end of sprint

### Team Utilization
**What**: Percentage of available capacity being used
**Example**: Sarah has 40 hours capacity, assigned 36 hrs = 90%
**Healthy Range**: 80-95% (not overbooked, not idle)

### Estimation Accuracy
**What**: How close estimates are to actual time
**Example**: Estimated 8 hours, took 10 hours = 80% accuracy
**Improvement**: Helps future estimates get better

---

## ⚡ Quick Actions

### Move Task
```
1. Click & Hold task card
2. Drag to new column
3. Release
→ Task status updated automatically
```

### Assign to Sprint
```
1. Click task
2. Select "Sprint" dropdown
3. Choose target sprint
→ Task added to sprint backlog
```

### Add Story Points
```
1. Click task
2. Click "Points" field
3. Enter value (1, 2, 3, 5, 8, 13, 21)
4. Save
→ Points added, priority updated
```

### Create Swimlane
```
1. In Sprint view: Click "+ Add Swimlane"
2. Enter name (e.g., "Frontend Team")
3. Select type (Team / Epic)
4. Choose color
5. Create
→ New row appears in sprint board
```

---

## 🚨 Alert Indicators

```
🔴 RED ALERTS:
├── Task overdue by >2 days
├── Blocker not resolved
├── Team utilization >110%
├── Burndown trending up
└── 2+ critical dependencies not met

🟡 YELLOW WARNINGS:
├── Task due within 3 days
├── Low estimation accuracy
├── Team utilization 100-110%
├── Burndown not following trend
└── 1 potential blocker

🟢 GREEN OK:
├── Tasks on schedule
├── Team balanced (80-95%)
├── Burndown tracking well
├── Estimation improving
└── No blockers
```

---

## 📈 Analytics Views

### 1. Sprint Health Dashboard
```
Sprint Status: 🟢 HEALTHY
├── Progress: 53% (8/15 tasks)
├── Velocity: On track (35.5 avg)
├── Team Util: Balanced (93%)
├── Blockers: None
└── At-Risk Tasks: 2
```

### 2. Team Performance
```
Team Member | Tasks Done | Avg Days | On-Time
Sarah       | 8          | 4.2      | 100% ✓
John        | 5          | 3.8      | 80%  ⚠
Jane        | 3          | 5.1      | 50%  ❌
Mike        | 2          | 4.0      | 100% ✓
```

### 3. Velocity Trend (Multi-Sprint)
```
Sprint 1: 35 pts ████████████
Sprint 2: 38 pts ████████████████
Sprint 3: 32 pts ███████████
Sprint 4: 40 pts ████████████████░ Avg: 36.25
```

---

## 🎓 Common Questions

### Q: How do I know what to do first?
**A**: Look at Priority Matrix. Q1 (Red) tasks should always be done first.

### Q: Why is my team showing 110% utilization?
**A**: You assigned too many tasks. Remove some tasks or extend the sprint.

### Q: What's story points?
**A**: Complexity rating (1-21 scale). Higher = harder/longer. Used for capacity planning.

### Q: When should I recalculate priorities?
**A**: Daily (automatic) or weekly when reviewing Q2 for next sprint.

### Q: Can I move tasks between sprints?
**A**: Yes! Just change the "Sprint" field on the task.

### Q: What if I want to reschedule a sprint?
**A**: Go to Sprint settings, edit start/end dates. No problem!

---

## 🔧 Admin Tasks

### Daily
- Review sprint board
- Check burndown chart
- Address any red alerts
- Update blocking tasks

### Weekly
- Sprint planning/review
- Recalculate priorities
- Check team performance
- Forecast next sprint capacity

### Monthly
- Review velocity trend
- Analyze estimation accuracy
- Team performance review
- Plan next month's sprints

---

## 📚 Document Cross-Reference

| Question | Document |
|----------|----------|
| "How do I design the database?" | WORKFLOW_SPEC.md |
| "What should the UI look like?" | UI_DESIGN_GUIDE.md |
| "How long will this take?" | IMPLEMENTATION_ROADMAP.md |
| "Show me code examples" | QUICK_START_CODE.md |
| "Which workflow is best?" | WORKFLOW_RECOMMENDATIONS.md |
| "How should it look?" | UI_WIREFRAMES.md |

---

## 🎯 Implementation Phases at a Glance

```
PHASE 1 (Weeks 1-2): SPRINT BOARD
└─ Kanban with sprints, story points, metrics

PHASE 2 (Weeks 3-4): PRIORITY MATRIX
└─ Smart prioritization, Q1-Q4 quadrants

PHASE 3 (Weeks 5-6): SWIMLANES
└─ Team organization, capacity planning

PHASE 4 (Weeks 7-8): TIME-BLOCKING
└─ Calendar, burndown, advanced analytics

RESULT: 4.0 ⭐ → 5.0+ ⭐
```

---

## 💡 Tips for Success

✅ **DO:**
- Start with Phase 1 (sprint basics)
- Test each phase before moving to next
- Get team feedback early & often
- Track metrics from day one
- Celebrate small wins

❌ **DON'T:**
- Skip testing phases
- Implement all 4 phases at once
- Change database schema mid-sprint
- Ignore performance issues
- Deploy without staging test

---

## 🚀 Ready to Build?

1. **Start Here**: README.md (overview)
2. **Then Study**: WORKFLOW_SPEC.md (architecture)
3. **Reference**: QUICK_START_CODE.md (code)
4. **Review**: UI_DESIGN_GUIDE.md (UI)
5. **Plan**: IMPLEMENTATION_ROADMAP.md (timeline)

Good luck! 🎉
