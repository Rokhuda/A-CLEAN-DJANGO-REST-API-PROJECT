# TaskFlow API - Enhanced UI/UX Design Guide

## Design Overview
This document outlines the visual and interaction design for Scrumban + Priority Matrix implementation.

---

## PART 1: SPRINT BOARD VIEW

### 1.1 Sprint Board Layout (Primary View)

```
┌───────────────────────────────────────────────────────────────────────────┐
│  TaskFlow                                              [Search] [👤] [⚙️]  │
├───────────────────────────────────────────────────────────────────────────┤
│  Dashboard │ Sprints │ Projects │ Reports                                 │
│                                                                            │
│  ┌─ Sprint Control ──────────────────────────────────────────────────────┐│
│  │                                                                        ││
│  │ Sprint: [Sprint 1 ▼] │ Start: Jun 1 │ End: Jun 14 │ Status: Active   ││
│  │ Capacity: 40 pts │ Completed: 18 pts │ Remaining: 22 pts │ [+ Add Sprint]││
│  │                                                                        ││
│  │ Goal: "Implement user authentication and password recovery"           ││
│  │                                                                        ││
│  │ ┌─ Team Utilization ────────────────────────────────────────┐         ││
│  │ │ Sarah Johnson: 40/40 hrs (100%)  [████████░░]            │         ││
│  │ │ John Doe:      32/40 hrs (80%)   [██████░░░░]            │         ││
│  │ │ Jane Smith:    38/40 hrs (95%)   [████████░░]            │         ││
│  │ └───────────────────────────────────────────────────────────┘         ││
│  │                                                                        ││
│  │ View: [Board] [List] [Calendar] [Priority Matrix] [Analytics]        ││
│  │                                                                        ││
│  └────────────────────────────────────────────────────────────────────────┘│
│                                                                            │
│  KANBAN BOARD (Current: Backlog Status)                                  │
│                                                                            │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐ ┌──────────────┐     │
│  │   BACKLOG    │ │  IN PROGRESS │ │ UNDER REVIEW │ │     DONE     │     │
│  │  (7 tasks)   │ │  (4 tasks)   │ │  (2 tasks)   │ │  (2 tasks)   │     │
│  │              │ │              │ │              │ │              │     │
│  │┌────────────┐│ │┌────────────┐│ │┌────────────┐│ │┌────────────┐│     │
│  ││ Design     ││ ││ API Setup  ││ ││ Review     ││ ││ Login      ││     │
│  ││ Login Form ││ ││ Database   ││ ││ Password   ││ ││ Logout ✓   ││     │
│  ││ [5 pts]    ││ ││ Schema     ││ ││ Recovery   ││ ││ [3 pts]    ││     │
│  ││ Sarah      ││ ││ [8 pts]    ││ ││ [5 pts]    ││ ││ Sarah ✓    ││     │
│  ││ Due: Jun 5 ││ ││ John       ││ ││ Jane       ││ ││ Due: Jun 1 ││     │
│  ││ Priority:  ││ ││ Due: Jun 7 ││ ││ Due: Jun 8 ││ ││            ││     │
│  ││ Q1 🔴      ││ ││ Priority:  ││ ││ Priority:  ││ ││ [Drag me]  ││     │
│  ││ [Drag me]  ││ ││ Q1 🔴      ││ ││ Q2 🟡      ││ ││            ││     │
│  │└────────────┘│ ││ [Drag me]  ││ │└────────────┘│ │└────────────┘│     │
│  │┌────────────┐│ │└────────────┘│ │┌────────────┐│ │┌────────────┐│     │
│  ││ API Docs   ││ │┌────────────┐│ ││ Password   ││ ││ Forgot     ││     │
│  ││ [3 pts]    ││ ││ Test Suite ││ ││ Reset Flow ││ ││ Password ✓ ││     │
│  ││ Mike       ││ ││ [5 pts]    ││ ││ [8 pts]    ││ ││ [3 pts]    ││     │
│  ││ Due: Jun 10││ ││ Jane       ││ ││ Mike       ││ ││ John ✓     ││     │
│  ││ Priority:  ││ ││ Due: Jun 9 ││ ││ Due: Jun 9 ││ ││ Due: Jun 2 ││     │
│  ││ Q2 🟡      ││ ││ Priority:  ││ ││ Priority:  ││ ││            ││     │
│  ││ [Drag me]  ││ ││ Q1 🔴      ││ ││ Q1 🔴      ││ ││            ││     │
│  │└────────────┘│ │└────────────┘│ │└────────────┘│ │└────────────┘│     │
│  │              │ │              │ │              │ │              │     │
│  │  [+ New]    │ │┌────────────┐│ │              │ │  [+ New]    │     │
│  │              │ ││ Code Review││ │              │ │              │     │
│  │              │ ││ [3 pts]    ││ │              │ │              │     │
│  │              │ ││ Sarah      ││ │              │ │              │     │
│  │              │ ││ Due: Jun 8 ││ │              │ │              │     │
│  │              │ ││ Priority:  ││ │              │ │              │     │
│  │              │ ││ Q2 🟡      ││ │              │ │              │     │
│  │              │ │└────────────┘│ │              │ │              │     │
│  │              │ │  [+ New]    │ │              │ │              │     │
│  │              │ │              │ │              │ │              │     │
│  │              │ │              │ │              │ │              │     │
│  └──────────────┘ └──────────────┘ └──────────────┘ └──────────────┘     │
│                                                                            │
│  ┌─ Sprint Progress ──────────────────────────────────────────────────┐   │
│  │                                                                    │   │
│  │ Burndown Chart:                     Velocity Trend:              │   │
│  │ 40 pts│      ╱╲                     40│  ╱╲     ╱╲              │   │
│  │ 35    │     ╱  ╲                    35│ ╱  ╲   ╱  ╲ Avg: 35.5   │   │
│  │ 30    │    ╱    ╲                   30│╱    ╲ ╱    ╲            │   │
│  │ 25    │   ╱      ╲                  25│      ╲      ╲           │   │
│  │ 20    │  ╱________╲                 20│              ╲          │   │
│  │ 15    │ ╱          ╲                15│               ╲         │   │
│  │ 10    │╱____________╲               10│                ╲        │   │
│  │  5    │                             5 │                 ╲       │   │
│  │  0    └──────────────────               0└─────────────────      │   │
│  │     1  3  5  7  9 11 13 15             Sprint 1 2 3 4 5        │   │
│  │                                                                    │   │
│  └────────────────────────────────────────────────────────────────────┘   │
│                                                                            │
└───────────────────────────────────────────────────────────────────────────┘
```

### Color Coding for Priority Quadrants
- **Q1 (🔴 Red)**: Urgent & Important - DO FIRST
- **Q2 (🟡 Yellow)**: Not Urgent & Important - SCHEDULE  
- **Q3 (🟠 Orange)**: Urgent & Not Important - DELEGATE
- **Q4 (⚪ Gray)**: Not Urgent & Not Important - ELIMINATE

---

## PART 2: PRIORITY MATRIX VIEW

### 2.1 Interactive Priority Matrix

```
┌────────────────────────────────────────────────────────────────────────┐
│  Priority Matrix View                        [Recalculate] [Settings]  │
├────────────────────────────────────────────────────────────────────────┤
│                                                                        │
│                                                                        │
│           IMPORTANCE SCORE (0-100)                                   │
│                100                                                   │
│                  │                                                   │
│                  │      Q2: SCHEDULE                                │
│             80   │      NOT URGENT & IMPORTANT                      │
│             │    │      (12 tasks)                                  │
│             │    │      [████]                                      │
│  URGENCY    │    │                    │                             │
│   SCORE    60   │      ┌──────────────┼──────────────┐              │
│  (0-100)   │    │      │              │              │              │
│             │    │      │    Q1        │    Q2        │              │
│             │    │      │    (8)       │    (12)      │              │
│          50 ├────┼──────┼──────────────┼──────────────┤─────        │
│             │    │      │    Q3        │    Q4        │              │
│             │    │      │    (3)       │    (15)      │              │
│             │    │      │              │              │              │
│          30 │    │      └──────────────┼──────────────┘              │
│             │    │                    │                             │
│            10    │                    │                             │
│             └────┴────────────────────┴──────────────────            │
│                 10    30    50    70    90    100                   │
│                              ↑                                      │
│                        IMPORTANCE SCORE                             │
│                                                                        │
│  LEGEND:                                                             │
│  🔴 Q1: 8 tasks  │ 🟡 Q2: 12 tasks  │ 🟠 Q3: 3 tasks  │ ⚪ Q4: 15 tasks
│                                                                        │
│  Click on quadrant to view/manage tasks                             │
│                                                                        │
└────────────────────────────────────────────────────────────────────────┘
```

### 2.2 Q1 (Do First) Task Detail View

```
┌────────────────────────────────────────────────────────────────────────┐
│  Q1: Urgent & Important - 8 Tasks                      [← Back]        │
├────────────────────────────────────────────────────────────────────────┤
│                                                                        │
│  Filter: [All] [My Tasks] [By Team]  |  Sort: [Due Date ▼]         │
│                                                                        │
│  ┌──────────────────────────────────────────────────────────────────┐│
│  │ Task Title            │ Due Date │ Assigned │ Points │ Status   ││
│  ├──────────────────────────────────────────────────────────────────┤│
│  │ Design Login Form     │ Jun 5    │ Sarah    │ 5      │ In Prog. ││
│  │ API Database Schema   │ Jun 7    │ John     │ 8      │ In Prog. ││
│  │ Password Reset Flow   │ Jun 9    │ Mike     │ 8      │ Review   ││
│  │ User Auth Service     │ Jun 8    │ Jane     │ 13     │ In Prog. ││
│  │ Session Management    │ Jun 10   │ Sarah    │ 5      │ Backlog  ││
│  │ JWT Token Setup       │ Jun 6    │ John     │ 3      │ In Prog. ││
│  │ Email Verification    │ Jun 11   │ Mike     │ 8      │ Backlog  ││
│  │ Two-Factor Auth       │ Jun 12   │ Jane     │ 13     │ Backlog  ││
│  └──────────────────────────────────────────────────────────────────┘│
│                                                                        │
│  Summary:                                                            │
│  • Total: 8 tasks, 63 story points                                  │
│  • In Progress: 4 tasks                                             │
│  • Blocked: 1 task (waiting for JWT Token Setup)                    │
│  • Overdue: 0 tasks                                                 │
│                                                                        │
└────────────────────────────────────────────────────────────────────────┘
```

---

## PART 3: SWIMLANE BOARD VIEW

### 3.1 Team Swimlane Board

```
┌────────────────────────────────────────────────────────────────────────┐
│  Sprint 1 - By Team                     [Add Swimlane] [Settings]      │
├────────────────────────────────────────────────────────────────────────┤
│                                                                        │
│  SWIMLANE: Frontend Team (3 members)                                 │
│  ┌────────┬────────┬────────┬────────┬────────┐                      │
│  │ BACKLOG│ READY  │WORKING │ REVIEW │  DONE  │                      │
│  │(2)     │(1)     │(2)     │(1)     │(1)     │                      │
│  ├────────┼────────┼────────┼────────┼────────┤                      │
│  │ Task 1 │ Task 4 │ Task 7 │ Task 9 │ Task 11│                      │
│  │ Task 2 │        │ Task 8 │        │        │                      │
│  │        │        │        │        │        │                      │
│  └────────┴────────┴────────┴────────┴────────┘                      │
│  Capacity: 40 pts │ Assigned: 38 pts │ Utilization: 95%             │
│                                                                        │
│  SWIMLANE: Backend Team (2 members)                                  │
│  ┌────────┬────────┬────────┬────────┬────────┐                      │
│  │ BACKLOG│ READY  │WORKING │ REVIEW │  DONE  │                      │
│  │(3)     │(2)     │(2)     │(1)     │(1)     │                      │
│  ├────────┼────────┼────────┼────────┼────────┤                      │
│  │ Task 3 │ Task 6 │ Task 10│ Task 13│ Task 14│                      │
│  │ Task 5 │ Task 6 │ Task 12│        │        │                      │
│  │        │        │        │        │        │                      │
│  └────────┴────────┴────────┴────────┴────────┘                      │
│  Capacity: 40 pts │ Assigned: 40 pts │ Utilization: 100%            │
│                                                                        │
│  SWIMLANE: DevOps (1 member)                                         │
│  ┌────────┬────────┬────────┬────────┬────────┐                      │
│  │ BACKLOG│ READY  │WORKING │ REVIEW │  DONE  │                      │
│  │(1)     │(0)     │(1)     │(0)     │(0)     │                      │
│  ├────────┼────────┼────────┼────────┼────────┤                      │
│  │ Task 15│        │ Task 16│        │        │                      │
│  │        │        │        │        │        │                      │
│  └────────┴────────┴────────┴────────┴────────┘                      │
│  Capacity: 20 pts │ Assigned: 15 pts │ Utilization: 75%             │
│                                                                        │
│  ┌─ Overall Sprint Capacity ─────────────────────┐                  │
│  │ Total Capacity:    100 pts                    │                  │
│  │ Total Assigned:     93 pts                    │                  │
│  │ Overall Util:       93%  [███████░░]         │                  │
│  │ Status: ✓ Healthy                            │                  │
│  └───────────────────────────────────────────────┘                  │
│                                                                        │
└────────────────────────────────────────────────────────────────────────┘
```

---

## PART 4: CALENDAR/TIME-BLOCKED VIEW

### 4.1 Sprint Calendar View

```
┌────────────────────────────────────────────────────────────────────────┐
│  Sprint 1 Calendar - Week 1 (Jun 1-7)                                 │
├────────────────────────────────────────────────────────────────────────┤
│                                                                        │
│  [← Previous Week]              [Week 1 of 2]              [Next Week →]
│                                                                        │
│  ┌─────────────────────────────────────────────────────────────────┐  │
│  │ Sunday    Monday    Tuesday   Wednesday  Thursday  Friday   Sat │  │
│  │ Jun 1     Jun 2     Jun 3     Jun 4      Jun 5     Jun 6     Jun 7
│  ├─────────────────────────────────────────────────────────────────┤  │
│  │         ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐         │  │
│  │         │ BACKLOG │ │READY(2) │ │WORKING(2)│REVIEW(1)│         │  │
│  │         │    -    │ │  8 pts  │ │ 10 pts  │  5 pts  │         │  │
│  │         │         │ │         │ │         │         │         │  │
│  │         │ 4 tasks │ │ Task 4  │ │Task 7   │ Task 9  │         │  │
│  │         │         │ │ Task 6  │ │Task 8   │ (Review)│         │  │
│  │         │         │ │         │ │         │         │         │  │
│  │         │ 10 pts  │ └─────────┘ └─────────┘ └─────────┘         │  │
│  │         │         │         ↓                                   │  │
│  │         └─────────┘      DONE(1)                                │  │
│  │                          Task 11                                │  │
│  │                           (3 pts)                               │  │
│  │                                                                 │  │
│  │ Team Workload (Daily):                                          │  │
│  │ • Sarah:  8h │ 8h │ 6h │ 4h │ 0h │ 2h │ 0h = 28h / 40h (70%) │  │
│  │ • John:   0h │ 4h │ 8h │ 8h │ 4h │ 0h │ 0h = 24h / 40h (60%) │  │
│  │ • Jane:   0h │ 0h │ 0h │ 2h │ 4h │ 8h │ 0h = 14h / 40h (35%) │  │
│  │ • Mike:   0h │ 0h │ 0h │ 0h │ 0h │ 4h │ 0h = 4h / 40h (10%)  │  │
│  │                                                                 │  │
│  │ Recommended Action:                                             │  │
│  │ "Move 1-2 tasks from Sarah to Jane to balance workload"        │  │
│  │                                                                 │  │
│  └─────────────────────────────────────────────────────────────────┘  │
│                                                                        │
└────────────────────────────────────────────────────────────────────────┘
```

---

## PART 5: ANALYTICS & REPORTING

### 5.1 Sprint Analytics Dashboard

```
┌────────────────────────────────────────────────────────────────────────┐
│  Sprint 1 Analytics                         [Export] [Print]            │
├────────────────────────────────────────────────────────────────────────┤
│                                                                        │
│  Period: Jun 1-14 │ Status: Active (8 days remaining)                 │
│                                                                        │
│  ┌──────────────────┐ ┌──────────────────┐ ┌──────────────────┐       │
│  │ Sprint Health     │ │ Task Completion │ │ Team Efficiency  │       │
│  │                  │ │                  │ │                  │       │
│  │ On Track ✓       │ │ 53.3% Complete   │ │ 93% Utilization  │       │
│  │ Status: Green    │ │ Expected: 50%    │ │ Status: Healthy  │       │
│  │ Velocity: 35.5   │ │ Trend: ↑ +5%     │ │ Velocity OK      │       │
│  │ Confidence: 92%  │ │                  │ │ Burndown: Good   │       │
│  └──────────────────┘ └──────────────────┘ └──────────────────┘       │
│                                                                        │
│  ┌─────────────────────────────────────────────────────────────────┐  │
│  │ Burndown Chart                                                  │  │
│  │                                                                 │  │
│  │ 45 │      ╱╲                                                   │  │
│  │ 40 │     ╱  ╲          Ideal Line (gray)                       │  │
│  │ 35 │    ╱    ╲──────  Actual (blue)                            │  │
│  │ 30 │   ╱         ╲                                             │  │
│  │ 25 │  ╱           ╲                                            │  │
│  │ 20 │ ╱             ╲                                           │  │
│  │ 15 │╱               ╲                                          │  │
│  │ 10 │                 ╲                                         │  │
│  │  5 │                  ╲                                        │  │
│  │  0 └──────────────────────────────────────────────────────    │  │
│  │    0  2  4  6  8  10 12 14 (Days in Sprint)                  │  │
│  │                                                                 │  │
│  │ Trend: Healthy - tracking below ideal, ahead of schedule      │  │
│  └─────────────────────────────────────────────────────────────────┘  │
│                                                                        │
│  ┌─────────────────────────────────────────────────────────────────┐  │
│  │ Team Performance                                                │  │
│  │                                                                 │  │
│  │ Member        │ Assigned │ Completed │ Velocity │ On-Time     │  │
│  │ Sarah Johnson │ 15 pts   │ 8 pts (53%)│ 8.0/day  │ 100% ✓     │  │
│  │ John Doe      │ 12 pts   │ 5 pts (42%)│ 5.0/day  │ 80%  ⚠️    │  │
│  │ Jane Smith    │ 18 pts   │ 3 pts (17%)│ 3.0/day  │ 50%  ❌    │  │
│  │ Mike Chen     │ 8 pts    │ 2 pts (25%)│ 2.0/day  │ 100% ✓     │  │
│  │                                                                 │  │
│  │ Team Total    │ 63 pts   │ 18 pts    │ 18/day   │ 92%        │  │
│  └─────────────────────────────────────────────────────────────────┘  │
│                                                                        │
│  ┌─────────────────────────────────────────────────────────────────┐  │
│  │ Risk Analysis                                                   │  │
│  │                                                                 │  │
│  │ ⚠️  Jane Smith: Falling behind (50% on-time)                   │  │
│  │     Recommendation: Redistribute 3 pts to other team members  │  │
│  │                                                                 │  │
│  │ ⚠️  4 Tasks at Risk of missing deadline                        │  │
│  │     • Task 8 (John) - Due Jun 9                               │  │
│  │     • Task 12 (Jane) - Due Jun 9                              │  │
│  │     • Task 7 (John) - Due Jun 8                               │  │
│  │     • Task 10 (Mike) - Due Jun 10                             │  │
│  │                                                                 │  │
│  │ ✓  1 Blocker dependency resolved this sprint                  │  │
│  │                                                                 │  │
│  │ ✓  Sprint goal on track: "Implement user auth" 92% complete  │  │
│  └─────────────────────────────────────────────────────────────────┘  │
│                                                                        │
└────────────────────────────────────────────────────────────────────────┘
```

---

## PART 6: TASK CARD DESIGN

### 6.1 Enhanced Task Card

```
┌─────────────────────────────┐
│ Design Login Form           │  ← Task Title
│ [Q1 🔴] [5 pts] [Due: Jun 5]│  ← Priority, Points, Due Date
├─────────────────────────────┤
│                             │
│ Description:                │
│ Create a responsive login   │
│ form with email/password    │
│ fields                      │
│                             │
│ Status: In Progress         │
│ Assigned to: Sarah Johnson  │
│ Sprint: Sprint 1            │
│ Swimlane: Frontend Team     │
│                             │
│ Blocking: Task #8, Task #10 │  ← Dependencies
│ Blocked by: None            │
│                             │
│ [View Details] [Edit]       │
│                             │
└─────────────────────────────┘
```

---

## PART 7: DESIGN TOKENS

### Color Palette
```
Primary:
- Brand Blue: #3498db
- Dark Blue: #2c3e50

Priority Quadrants:
- Q1 (Urgent & Important): #e74c3c (Red)
- Q2 (Not Urgent & Important): #f39c12 (Yellow)
- Q3 (Urgent & Not Important): #e67e22 (Orange)
- Q4 (Not Urgent & Not Important): #95a5a6 (Gray)

Status Colors:
- Backlog: #ecf0f1 (Light Gray)
- In Progress: #3498db (Blue)
- Under Review: #9b59b6 (Purple)
- Changes Requested: #e67e22 (Orange)
- Done: #27ae60 (Green)

Health Indicators:
- Healthy: #27ae60 (Green)
- At Risk: #f39c12 (Yellow)
- Blocked/Critical: #e74c3c (Red)
```

### Typography
```
Headings:
- H1: 28px, Bold, #2c3e50
- H2: 22px, Bold, #2c3e50
- H3: 18px, Semi-bold, #34495e

Body:
- Regular: 14px, Regular, #34495e
- Small: 12px, Regular, #7f8c8d
- Label: 12px, Semi-bold, #2c3e50
```

### Spacing
```
- XS: 4px
- S: 8px
- M: 16px
- L: 24px
- XL: 32px
- XXL: 48px
```

---

## PART 8: INTERACTION PATTERNS

### 8.1 Drag & Drop
- **Source**: Task cards in any column
- **Target**: Any other column or swimlane
- **Feedback**: Visual placeholder, highlighted target zone
- **Result**: Task status updated, time-logged

### 8.2 Quick Actions
- **Hover**: Task card shows [Edit] [Move] [Comment] [Details]
- **Click**: Opens task detail modal
- **Right-click**: Context menu (Move, Assign, Priority, Delete)

### 8.3 Notifications
- Task moved to urgent column
- Team member added/removed
- Blocker resolved
- Deadline approaching
- Workload imbalance detected

---

## Implementation Priority

1. **High Priority**: Sprint Board, Kanban Columns, Basic Cards
2. **Medium Priority**: Priority Matrix, Swimlanes, Team Utilization
3. **Lower Priority**: Advanced Analytics, Calendar View, AI Features

---

## Responsive Design Breakpoints

```
Desktop (1200px+):   Full layout, all features
Tablet (768px):     Compact swimlanes, scrollable board
Mobile (320px):     Single column, list view only
```
