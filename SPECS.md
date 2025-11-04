# DeskZen – Backend Microservices Specification

## Project Overview

| Item      | Detail                                      |
|-----------|---------------------------------------------|
| Name      | DeskZen                                     |
| Purpose   | Backend microservices for office desk & meeting room reservations |
| Architecture | REST APIs + Event-driven architecture + Database-per-service |
| Focus     | Clean service boundaries, scalability, auditability |

## 👥 User Roles & Access

| Role      | Permissions                                      |
|-----------|--------------------------------------------------|
| Employee  | Book/cancel/edit own reservations                |
| Manager   | Employee permissions + department-level visibility |
| Admin     | All actions + user/department/resource management |

## 🏛 Microservices Overview

| Service             | Owns Data | Purpose                          |
|---------------------|-----------|----------------------------------|
| API Gateway         | ❌       | Authentication + routing         |
| Users Service       | ✅ users_db | Users, departments, preferences, roles |
| Inventory Service   | ✅ inventory_db | Physical assets (desks, rooms), layout, maintenance |
| Reservation Service | ✅ reservations_db | Booking logic & reservation tracking |
| Notification Service| ✅ notifications_db (optional) | Sends emails/SMS using events |
| Analytics Service   | ✅ analytics_db | Aggregated historical data |
| Reports Service     | ❌       | Uses Analytics to serve reports |

## 🔑 1. API Gateway (Edge Layer)

**Purpose:** Auth, JWT validation, routing to microservices.

### Public Endpoints:

- `POST /auth/login`
- `POST /auth/register`
- `POST /auth/refresh`
- `POST /auth/logout`

### User-facing Routes (proxy to services):

- `GET  /users/profile`
- `PUT  /users/profile`
- `GET  /reservations/my`
- `POST /reservations/desks`
- `POST /reservations/rooms`
- `GET  /reservations/desks/available`
- `GET  /reservations/rooms/available`

## 🧑‍💼 2. Users Service (users_db)

### ✅ Tables

- `users(id, email, password_hash, full_name, department_id, role, created_at, updated_at)`
- `departments(id, name, floor_assignment, max_capacity)`
- `user_preferences(user_id, preferred_floor, preferred_zone, notification_email, notification_sms, quiet_workspace)`
- `refresh_tokens(id, user_id, token, expires_at, created_at)`
- `audit_logs(id, user_id, action, details, timestamp)`

### ✅ Core Features

- ✔ Password hashing (bcrypt)
- ✔ JWT issuing
- ✔ Validates department capacity
- ✔ Role-based access control (ENUM: employee, manager, admin)

## 💺 3. Inventory Service (inventory_db)

### ✅ Tables

- `desks(id, desk_number, floor, zone, amenities JSON, status)`
- `meeting_rooms(id, room_name, floor, capacity, equipment JSON, status)`
- `office_layout(id, floor_number, zone_name, capacity, floor_map_data)`
- `maintenance_schedules(id, resource_type ENUM('desk','meeting_room'), resource_id, start_time, end_time, reason)`

### ✅ Responsibilities

- ✔ Manages physical resources
- ✔ Publishes MAINTENANCE_SCHEDULED events
- ✔ Provides real-time availability to Reservation Service

## 📅 4. Reservation Service (reservations_db)

### ✅ Tables

- `reservations (id, user_id, resource_type ENUM('desk','meeting_room'), resource_id, start_time, end_time, status ENUM('confirmed','cancelled','completed'), created_at, updated_at)`
- `recurring_patterns (id, reservation_id, recurrence_type ENUM('daily','weekly','monthly'), interval INT DEFAULT 1, end_date DATETIME)`
- `reservation_audit_logs (id, reservation_id, user_id, action, previous_values JSON, new_values JSON, timestamp)`
- `blackout_dates(id, date, reason)`

### ✅ Core Business Logic

- ✔ Double-booking prevention
- ✔ Checks maintenance + blackout days
- ✔ Recurring reservation conflict detection
- ✔ Max advance booking = 30 days
- ✔ Publishes RESERVATION_CREATED, RESERVATION_CANCELLED

## 📩 5. Notification Service (notifications_db)

### ✅ Tables

- `notification_templates (id, type, subject, content TEXT, channel ENUM('email','sms'))`
- `notification_logs (id, user_id, type, channel, status, sent_at)`

### ✅ Event Subscriber

- `USER_REGISTERED` → Send welcome email
- `RESERVATION_CREATED` → Send confirmation
- `RESERVATION_CANCELLED` → Send cancellation notice

Retry on failure, logs stored

## 📊 6. Analytics Service (analytics_db)

### ✅ Tables

- `daily_usage (date, floor, total_desks, reserved_desks, utilization_rate)`
- `peak_hours (date, hour, reservation_count)`
- `user_behavior (user_id, preferred_zone, avg_weekly_reservations)`

Subscribes to: RESERVATION_CREATED, RESERVATION_CANCELLED, USER_REGISTERED

Periodic ETL into aggregates

Indexed on date, floor, user_id

## 📑 7. Reports Service

No own DB — queries Analytics DB

Endpoints like:

- `GET /reports/usage?format=csv&date=2024-01`
- `GET /reports/department-utilization`
- `POST /reports/generate-custom`

## 🔄 Event-Driven Architecture

| Event                | Publisher    | Subscriber(s)                  |
|----------------------|--------------|--------------------------------|
| USER_REGISTERED      | Users        | Notifications, Analytics       |
| RESERVATION_CREATED  | Reservations | Inventory (capacity), Analytics, Notifications |
| MAINTENANCE_SCHEDULED| Inventory    | Reservations, Notifications    |

## 🔐 Security

- ✔ JWT auth via API Gateway
- ✔ Refresh tokens stored in DB
- ✔ RBAC per service
- ✔ Rate limits (auth 5/min, reservations 10/min)
- ✔ XSS & SQL injection protection