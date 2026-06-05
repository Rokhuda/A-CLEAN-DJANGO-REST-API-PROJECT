# TaskFlow API - UI/UX Wireframes

## 1. MAIN APPLICATION UI - KANBAN DASHBOARD

```
┌─────────────────────────────────────────────────────────────────────┐
│  TaskFlow  [Logo]              Search: [___________]  👤 Notifications ⚙️ │
├─────────────────────────────────────────────────────────────────────┤
│ ├─ Dashboard      ├─ My Tasks      ├─ Projects      ├─ Reports       │
│                                                                       │
│  Kanban Board: "Project Alpha" (Active Sprint)                      │
│                                                                       │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│  │   BACKLOG    │ │  IN PROGRESS │ │ UNDER REVIEW │ │   CHANGES    │ │     DONE     │
│  │  (12 tasks)  │ │  (5 tasks)   │ │  (3 tasks)   │ │ REQUESTED    │ │  (25 tasks)  │
│  │              │ │              │ │              │ │ (2 tasks)    │ │              │
│  │┌────────────┐│ │┌────────────┐│ │┌────────────┐│ │┌────────────┐│ │┌────────────┐│
│  ││ Task Title ││ ││ Task Title ││ ││ Task Title ││ ││ Task Title ││ ││ Task Title ││
│  ││ Due: Jun15 ││ ││ Due: Jun 7 ││ ││ Due: Jun 9 ││ ││ Due: Jun12 ││ ││ Due: Jun 5 ││
│  ││ Priority:  ││ ││ Priority:  ││ ││ Priority:  ││ ││ Priority:  ││ ││ Priority:  ││
│  ││ [Drag me] ││ ││ [Drag me] ││ ││ [Drag me] ││ ││ [Drag me] ││ ││ [Drag me] ││
│  │└────────────┘│ │└────────────┘│ │└────────────┘│ │└────────────┘│ │└────────────┘│
│  │┌────────────┐│ │┌────────────┐│ │┌────────────┐│ │┌────────────┐│ │┌────────────┐│
│  ││ Task Title ││ ││ Task Title ││ ││ Task Title ││ │└────────────┘│ │└────────────┘│
│  ││ Due: Jun20 ││ ││ Due: Jun 8 ││ ││            ││ │              │ │              │
│  ││ Priority:  ││ ││ Priority:  ││ │└────────────┘│ │┌────────────┐│ │┌────────────┐│
│  ││ [Drag me] ││ ││ [Drag me] ││ │              │ ││ Task Title ││ ││ Task Title ││
│  │└────────────┘│ │└────────────┘│ │┌────────────┐│ ││            ││ ││ Complete ✓ ││
│  │              │ │┌────────────┐│ ││ Task Title ││ │└────────────┘│ │└────────────┘│
│  │  [+ New]    │ ││ Task Title ││ ││            ││ │              │ │ ...more tasks│
│  │              │ ││ Due: Jun 6 ││ │└────────────┘│ │  [+ New]    │ │              │
│  │              │ ││ Priority:  ││ │              │ │              │ │  [+ New]    │
│  │              │ ││ [Drag me] ││ │  [+ New]    │ │              │ │              │
│  │              │ │└────────────┘│ │              │ │              │ │              │
│  │              │ │┌────────────┐│ │              │ │              │ │              │
│  │              │ ││ Task Title ││ │              │ │              │ │              │
│  │              │ ││ Due: Jun 9 ││ │              │ │              │ │              │
│  │              │ ││ Priority:  ││ │              │ │              │ │              │
│  │              │ ││ [Drag me] ││ │              │ │              │ │              │
│  │              │ │└────────────┘│ │              │ │              │ │              │
│  │              │ │  [+ New]    │ │              │ │              │ │              │
│  │              │ │              │ │              │ │              │ │              │
│  └──────────────┘ └──────────────┘ └──────────────┘ └──────────────┘ └──────────────┘
│                                                                       │
│  [← Previous Sprint]         Sprint: Sprint 1 (June 1 - 14)    [Next Sprint →]
└─────────────────────────────────────────────────────────────────────┘
```

## 2. TASK DETAIL MODAL - OPENED FROM KANBAN CARD

```
┌──────────────────────────────────────────┐
│  Task Detail                        [×]  │
├──────────────────────────────────────────┤
│                                          │
│  Task Title: [__________________________] │
│                                          │
│  Description:                            │
│  [____________________________________ ] │
│  [____________________________________ ] │
│  [____________________________________ ] │
│                                          │
│  Status: [Backlog ▼]                     │
│                                          │
│  Priority: [High ▼]                      │
│                                          │
│  Assigned To: [Select User ▼]            │
│                                          │
│  Due Date: [Jun 15, 2026]  [📅]          │
│                                          │
│  Labels: [Tag1] [Tag2] [+ Add]           │
│                                          │
│  Attachments:                            │
│  [document.pdf] [image.png]  [+ Upload]  │
│                                          │
│  Comments (3):                           │
│  ┌──────────────────────────────────────┐│
│  │ User: "This needs more detail"       ││
│  │ Jun 3, 2:30 PM                       ││
│  │ [Reply] [Like]                       ││
│  └──────────────────────────────────────┘│
│  ┌──────────────────────────────────────┐│
│  │ Developer: "Working on it"           ││
│  │ Jun 4, 10:15 AM                      ││
│  │ [Reply] [Like]                       ││
│  └──────────────────────────────────────┘│
│                                          │
│  Comment: [________________________] [Send]│
│                                          │
│  [Delete]              [Save Changes]    │
└──────────────────────────────────────────┘
```

## 3. CREATE NEW TASK FORM

```
┌──────────────────────────────────────────┐
│  Create New Task                     [×] │
├──────────────────────────────────────────┤
│                                          │
│  *Title: [_____________________________ ] │
│                                          │
│  *Description:                           │
│  [____________________________________ ] │
│  [____________________________________ ] │
│  [____________________________________ ] │
│                                          │
│  Project: [Select Project ▼]             │
│                                          │
│  *Status: [Backlog ▼]                    │
│                                          │
│  *Priority: [Medium ▼]                   │
│                                          │
│  *Assigned To: [Current User ▼]          │
│                                          │
│  Due Date: [___________] [📅]            │
│                                          │
│  Labels: [+ Add Label]                   │
│                                          │
│  Subtasks:                               │
│  [ ] Subtask 1 [___________] [×]         │
│  [ ] Subtask 2 [___________] [×]         │
│  [+ Add Subtask]                         │
│                                          │
│  [Cancel]          [Create Task]         │
└──────────────────────────────────────────┘
```

## 4. DASHBOARD / OVERVIEW PAGE

```
┌─────────────────────────────────────────────────────────────────────┐
│  TaskFlow  [Logo]              Search: [___________]  👤 Notifications │
├─────────────────────────────────────────────────────────────────────┤
│ ├─ Dashboard      ├─ My Tasks      ├─ Projects      ├─ Reports       │
│                                                                       │
│  Welcome Back, Sarah! 👋                                             │
│                                                                       │
│  ┌────────────────────┐ ┌────────────────────┐ ┌────────────────────┐
│  │  My Tasks (Today)  │ │ Active Projects    │ │ Team Performance    │
│  │                    │ │                    │ │                    │
│  │  5 Assigned        │ │ Project Alpha: 12  │ │ Completion: 78%    │
│  │  2 Due Today       │ │ Project Beta: 8    │ │ On-time: 92%       │
│  │  3 Overdue ⚠️      │ │ Project Gamma: 15  │ │ Avg Duration: 4d   │
│  └────────────────────┘ └────────────────────┘ └────────────────────┘
│                                                                       │
│  Recently Updated Tasks:                                             │
│  ┌─────────────────────────────────────────────────────────────────┐
│  │ Task Title        Status          Due Date    Assigned  Updated  │
│  ├─────────────────────────────────────────────────────────────────┤
│  │ Design Login UI   Under Review    Jun 5      Sarah     2h ago  │
│  │ Setup Database    In Progress     Jun 6      John      1h ago  │
│  │ API Documentation Backlog         Jun 10     Team      3h ago  │
│  │ Testing Module    Changes Req.    Jun 8      Mike      30m ago │
│  │ Deploy to Prod    In Progress     Jun 12     Admin     Just now│
│  └─────────────────────────────────────────────────────────────────┘
│                                                                       │
│  Upcoming Deadlines:                                                 │
│  Jun 5:  Design Login UI  (OVERDUE - 2 days)                        │
│  Jun 6:  Setup Database   (TOMORROW)                                │
│  Jun 8:  Testing Module   (IN 2 DAYS)                              │
│  Jun 10: API Documentation (IN 4 DAYS)                              │
└─────────────────────────────────────────────────────────────────────┘
```

---

## ADMIN SITE UI

## 5. DJANGO ADMIN DASHBOARD - CUSTOM ADMIN INTERFACE

```
┌─────────────────────────────────────────────────────────────────────┐
│  TaskFlow Admin                     👤 Admin User  [Settings] [Logout]│
├─────────────────────────────────────────────────────────────────────┤
│ ├─ Dashboard   ├─ Users   ├─ Projects   ├─ Tasks   ├─ Teams        │
│                          ├─ Analytics  ├─ Settings                  │
│                                                                       │
│  System Overview                                                     │
│  ────────────────────────────────────────────────────────────────   │
│                                                                       │
│  ┌──────────────────┐ ┌──────────────────┐ ┌──────────────────┐     │
│  │  Total Users     │ │  Total Projects  │ │   Total Tasks    │     │
│  │      247         │ │       18         │ │      2,341       │     │
│  │    ↑ 12 this mo. │ │   ↑ 3 this mo.   │ │  ↑ 247 this mo.  │     │
│  └──────────────────┘ └──────────────────┘ └──────────────────┘     │
│                                                                       │
│  ┌──────────────────┐ ┌──────────────────┐ ┌──────────────────┐     │
│  │  Active Sessions │ │  System Health   │ │  Disk Usage      │     │
│  │       64         │ │  ✓ All Good      │ │   67% / 500GB    │     │
│  │   ↑ 8 active    │ │  API: 99.8%      │ │   ~335 GB Free   │     │
│  └──────────────────┘ └──────────────────┘ └──────────────────┘     │
│                                                                       │
│  Recent Admin Actions:                                               │
│  ┌───────────────────────────────────────────────────────────────┐  │
│  │ User "john@example.com" created                Jun 4, 11:45  │  │
│  │ Project "Mobile App" created                  Jun 4, 10:30  │  │
│  │ User "jane@example.com" role changed to Admin  Jun 3, 9:15  │  │
│  │ Task #1234 deleted by @admin                  Jun 3, 8:00  │  │
│  │ System backup completed                       Jun 3, 2:00  │  │
│  └───────────────────────────────────────────────────────────────┘  │
│                                                                       │
└─────────────────────────────────────────────────────────────────────┘
```

## 6. USER MANAGEMENT PAGE - ADMIN

```
┌─────────────────────────────────────────────────────────────────────┐
│  User Management                              [+ Add User] [Export]  │
├─────────────────────────────────────────────────────────────────────┤
│                                                                       │
│  Search: [______________] Status: [All ▼] Role: [All ▼]            │
│                                                                       │
│  ┌─────────────────────────────────────────────────────────────────┐
│  │ Name          Email                  Role      Status   Joined   │
│  ├─────────────────────────────────────────────────────────────────┤
│  │ Sarah Johnson sarah@company.com      Admin     Active   Jan 2025 │
│  │ John Doe      john@company.com       Manager   Active   Feb 2025 │
│  │ Jane Smith    jane@company.com       User      Active   Mar 2025 │
│  │ Mike Chen     mike@company.com       User      Inactive Apr 2025 │
│  │ Lisa Wong     lisa@company.com       Viewer    Active   May 2025 │
│  │ Robert Brown  robert@company.com     Manager   Active   May 2025 │
│  │ ...                                                               │
│  └─────────────────────────────────────────────────────────────────┘
│                                                                       │
│  [◀ Previous]  Page 1 of 25    [Next ▶]                              │
│                                                                       │
```

## 7. PROJECT MANAGEMENT PAGE - ADMIN

```
┌─────────────────────────────────────────────────────────────────────┐
│  Project Management                        [+ Create Project]        │
├─────────────────────────────────────────────────────────────────────┤
│                                                                       │
│  Search: [______________] Status: [All ▼]                          │
│                                                                       │
│  ┌──────────────────────────────────────────────────────────────────┐
│  │ Project Name  Owner         Status     Tasks   Members  Created   │
│  ├──────────────────────────────────────────────────────────────────┤
│  │ Project Alpha Sarah Johnson Active     342     8       Jan 2025  │
│  │ Project Beta  John Doe      Active     156     5       Feb 2025  │
│  │ Project Gamma Lisa Wong     Active     489     12      Mar 2025  │
│  │ Mobile App    Robert Brown  Planning   0       2       May 2025  │
│  │ Legacy System Sarah Johnson Archived   892     10      Jun 2024  │
│  │ ...                                                               │
│  └──────────────────────────────────────────────────────────────────┘
│                                                                       │
│  [◀ Previous]  Page 1 of 5     [Next ▶]                              │
│                                                                       │
```

## 8. TASK MANAGEMENT PAGE - ADMIN

```
┌─────────────────────────────────────────────────────────────────────┐
│  Task Management                                 [Export] [Bulk Edit]│
├─────────────────────────────────────────────────────────────────────┤
│                                                                       │
│  Search: [______________] Status: [All ▼] Priority: [All ▼]        │
│  Project: [All Projects ▼]                                          │
│                                                                       │
│  ┌──────────────────────────────────────────────────────────────────┐
│  │ ☐ Task ID  Title             Status        Priority Assigned     │
│  ├──────────────────────────────────────────────────────────────────┤
│  │ ☐ #2341   Design Login UI    Under Review  High    Sarah       │
│  │ ☐ #2340   API Endpoint       In Progress   High    John        │
│  │ ☐ #2339   Database Schema    Done          Medium  Jane        │
│  │ ☐ #2338   Testing Module     Changes Req.  High    Mike        │
│  │ ☐ #2337   Documentation      Backlog       Low     Lisa        │
│  │ ☐ #2336   Security Audit     Backlog       Critical Admin      │
│  │ ...                                                               │
│  └──────────────────────────────────────────────────────────────────┘
│                                                                       │
│  [◀ Previous]  Page 1 of 250   [Next ▶]                              │
│                                                                       │
```

## 9. ANALYTICS PAGE - ADMIN

```
┌─────────────────────────────────────────────────────────────────────┐
│  Analytics & Reporting                                              │
├─────────────────────────────────────────────────────────────────────┤
│                                                                       │
│  Time Period: [Last 30 Days ▼]  Project: [All Projects ▼]          │
│                                                                       │
│  ┌────────────────────────────────────────────────────────────────┐ │
│  │ Task Completion Rate (Last 30 Days)                           │ │
│  │ 78% ████████░░ Completed vs 22% Pending/In Progress          │ │
│  └────────────────────────────────────────────────────────────────┘ │
│                                                                       │
│  ┌─────────────────┐ ┌─────────────────┐ ┌─────────────────────────┐
│  │ Tasks by Status │ │ Tasks by Priority│ │ Velocity Chart (Tasks)  │
│  │                 │ │                 │ │                         │
│  │ Done: 892       │ │ Critical: 24    │ │  50│      ╱╲     ╱      │
│  │ In Progress: 65 │ │ High: 156       │ │  40│     ╱  ╲   ╱       │
│  │ Under Review: 34│ │ Medium: 287     │ │  30│    ╱    ╲ ╱        │
│  │ Backlog: 143    │ │ Low: 89         │ │  20│   ╱      ╲        │
│  │ Changes Req: 22 │ │                 │ │  10│  ╱________╲       │
│  │                 │ │                 │ │   0└─────────────────  │
│  │                 │ │                 │ │   W1 W2 W3 W4          │
│  └─────────────────┘ └─────────────────┘ └─────────────────────────┘
│                                                                       │
│  Team Performance:                                                   │
│  ┌──────────────────────────────────────────────────────────────┐   │
│  │ Team Member   Tasks Completed  Avg Completion Time  On-Time  │   │
│  │ Sarah Johnson      87            4.2 days           94%      │   │
│  │ John Doe          65            3.8 days           89%       │   │
│  │ Jane Smith        92            3.5 days           98%       │   │
│  │ Mike Chen         54            5.1 days           76%       │   │
│  │ Lisa Wong         78            4.0 days           91%       │   │
│  └──────────────────────────────────────────────────────────────┘   │
│                                                                       │
└─────────────────────────────────────────────────────────────────────┘
```

## 10. SETTINGS PAGE - ADMIN

```
┌─────────────────────────────────────────────────────────────────────┐
│  Admin Settings                                              [Save]  │
├─────────────────────────────────────────────────────────────────────┤
│                                                                       │
│  General Settings:                                                   │
│  ┌─────────────────────────────────────────────────────────────────┐
│  │ Application Name: [TaskFlow API________________]                │
│  │ System Email:     [admin@taskflow.com________]                  │
│  │ Timezone:         [UTC ▼]                                       │
│  │ Max Upload Size:  [50 MB ▼]                                     │
│  │ Enable Notifications: [✓]                                       │
│  │ Public Registration:  [✗]                                       │
│  └─────────────────────────────────────────────────────────────────┘
│                                                                       │
│  Email Configuration:                                                │
│  ┌─────────────────────────────────────────────────────────────────┐
│  │ SMTP Server:  [mail.company.com________________]                │
│  │ SMTP Port:    [587______]                                       │
│  │ SMTP User:    [admin@company.com______________]                 │
│  │ SMTP Pass:    [••••••••••] [Show/Hide]                          │
│  │ From Email:   [noreply@taskflow.com_________]                  │
│  │ [Test Email]                                                    │
│  └─────────────────────────────────────────────────────────────────┘
│                                                                       │
│  API Configuration:                                                  │
│  ┌─────────────────────────────────────────────────────────────────┐
│  │ API Rate Limit:  [1000 requests/hour ▼]                         │
│  │ API Timeout:     [30 seconds ▼]                                 │
│  │ Enable API Docs: [✓]                                            │
│  │ Swagger UI:      [✓]                                            │
│  │ API Key Required:[✗]                                            │
│  └─────────────────────────────────────────────────────────────────┘
│                                                                       │
│  [Cancel]                                                   [Save]   │
└─────────────────────────────────────────────────────────────────────┘
```

---

## KEY FEATURES SUMMARY

### User Interface Features:
- ✅ Kanban Board with 5 columns (Backlog, In Progress, Under Review, Changes Requested, Done)
- ✅ Drag & Drop task movement between columns
- ✅ Task detail modal with full information
- ✅ Create/Edit task forms
- ✅ Dashboard with quick stats and recent activities
- ✅ Search and filtering capabilities
- ✅ User profile and notification system
- ✅ Comments/activity tracking on tasks
- ✅ Subtasks support
- ✅ Priority levels (Critical, High, Medium, Low)
- ✅ Due dates and deadline tracking

### Admin Interface Features:
- ✅ Custom admin dashboard with system overview
- ✅ User management (create, edit, deactivate users)
- ✅ Project management (create, archive projects)
- ✅ Task management (bulk editing, filtering)
- ✅ Analytics & reporting (task completion, team velocity, performance metrics)
- ✅ System settings & configuration
- ✅ Email & API configuration
- ✅ Activity logs and audit trail
- ✅ Role-based access control (Admin, Manager, User, Viewer)

---

## TECHNOLOGY RECOMMENDATIONS

For frontend implementation:
- **React** or **Vue.js** for interactive kanban board
- **React Beautiful DnD** or **dnd-kit** for drag & drop functionality
- **Axios** for API communication with your Django REST backend
- **Chart.js** or **Recharts** for analytics visualizations
- **Tailwind CSS** or **Material-UI** for styling
- **Redux** or **Zustand** for state management
