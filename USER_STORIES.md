# DeskZen User Stories

## Overview

DeskZen is a backend microservices system that allows employees to reserve desks and meeting rooms in an office. The system provides different levels of access for Employee, Manager, and Admin, ensuring secure and efficient booking, management, and reporting.

## 1. Employee User Stories

### US-EMP-01 – Register and Authenticate
As an employee, I want to register and log in securely so that I can access the DeskZen reservation system.

#### Acceptance Criteria:
- Employee can register via /auth/register.
- Employee can log in via /auth/login and receive a JWT.
- Employee can refresh and log out using /auth/refresh and /auth/logout.

### US-EMP-02 – View Own Profile and Preferences
As an employee, I want to view and update my profile and workspace preferences.

#### Acceptance Criteria:
- Employee can GET/PUT /users/profile.
- Employee can GET/PUT /users/preferences.
- Changes are saved in users and user_preferences tables.

### US-EMP-03 – Browse Available Resources
As an employee, I want to check available desks and meeting rooms so I can plan my day.

#### Acceptance Criteria:
- Employee can GET /reservations/desks/available and /reservations/rooms/available.
- Only resources not already reserved or under maintenance are returned.
- Filters: date, floor, capacity (for meeting rooms).

### US-EMP-04 – Create, Modify, and Cancel Reservations
As an employee, I want to reserve, update, or cancel my own desk or meeting room reservations.

#### Acceptance Criteria:
- Employee can POST /reservations/desks or /reservations/rooms.
- Employee can PUT /reservations/{id} and DELETE /reservations/{id} for their own reservations.
- Conflicts, blackout dates, and maintenance are checked before booking.
- Reservation changes are recorded in reservation_audit_logs.
- Notifications are triggered for creation or cancellation.

## 2. Manager User Stories

### US-MGR-01 – Department-Level Visibility
As a manager, I want to view reservations for all employees in my department so that I can monitor resource usage.

#### Acceptance Criteria:
- Manager can GET /reservations/my-reservations filtered by department.
- Can access reservations data for all employees in the same department_id.

### US-MGR-02 – Manage Department Reservations
As a manager, I want to update or cancel reservations for employees in my department when necessary.

#### Acceptance Criteria:
- Manager can PUT or DELETE reservations made by employees in their department.
- Actions are logged in reservation_audit_logs.
- Notifications sent to affected employees.

### US-MGR-03 – View Department Reports
As a manager, I want to view analytics for my department's resource usage.

#### Acceptance Criteria:
- Manager can GET reports via Reports Service endpoints.
- Access restricted to department-specific usage statistics.

## 3. Admin User Stories

### US-ADM-01 – Manage Users and Departments
As an admin, I want to create, update, or delete users and manage departments.

#### Acceptance Criteria:
- Admin can POST, PUT, GET /admin/users.
- Admin can create and manage departments table entries.
- Role assignment (employee, manager, admin) is controlled.

### US-ADM-02 – Manage Desks and Meeting Rooms
As an admin, I want to add or update desks and meeting rooms so that the inventory stays accurate.

#### Acceptance Criteria:
- Admin can POST and PUT /inventory/desks and /inventory/rooms.
- Can manage office_layout and resources data.

### US-ADM-03 – Schedule Maintenance
As an admin, I want to mark resources under maintenance so that users cannot reserve them.

#### Acceptance Criteria:
- Admin can POST and DELETE /inventory/maintenance-schedules.
- Reservations service prevents bookings on scheduled maintenance.

### US-ADM-04 – Access System-Wide Reports
As an admin, I want to view usage and performance reports across all departments.

#### Acceptance Criteria:
- Admin can GET /reports/usage, /reports/department-utilization, and generate custom reports.
- Analytics data comes from analytics_db.

### US-ADM-05 – Audit Logging
As an admin, I want a complete audit trail of user and reservation actions for accountability.

#### Acceptance Criteria:
- All critical actions logged in audit_logs and reservation_audit_logs.
- Logs include user_id, action, timestamp, and affected entities.