# ✅ Task Tracker API (Built with FastAPI)

This is a simple **Task Management API** built using **FastAPI** and **Pydantic** 
It lets you create users, assign tasks to them, update task status, and retrieve task lists

## 📦 Features

- Create and fetch users 👤
- Create tasks for users 📝
- Update task status (pending, in_progress, completed) 🔁
- View all tasks assigned to a user 📋
- All data stored temporarily using in-memory dictionaries 🧠

---

## 🛠️ Installation Guide

Make sure Python is installed (version 3.8+ recommended).

Install **FastAPI** and **Uvicorn** using pip:

```bash
pip install fastapi uvicorn
```

---

## 🚀 Run the Application

Start the FastAPI development server using Uvicorn:

```bash
uvicorn main:app --reload
```

It will be live at:

```
http://127.0.0.1:8000
```

---

## 🔍 API Documentation (Swagger UI)

To test the API easily, open this in your browser:

```
http://127.0.0.1:8000/docs
```

It shows all available endpoints with input boxes — no Postman required!

---

## 📌 API Endpoints Guide

### 👤 Users

| Method | Endpoint           | Description            |
| ------ | ------------------ | ---------------------- |
| POST   | `/users/`          | Create a new user      |
| GET    | `/users/{user_id}` | Get user details by ID |

**Example - Create User**

```json
{
  "username": "codequeen",
  "email": "codequeen@example.com"
}
```

---

### 📝 Tasks

| Method | Endpoint                 | Description                        |
| ------ | ------------------------ | ---------------------------------- |
| POST   | `/tasks/`                | Create a task for a user           |
| GET    | `/tasks/{task_id}`       | Get task details by ID             |
| PUT    | `/tasks/{task_id}`       | Update task status only            |
| GET    | `/users/{user_id}/tasks` | List all tasks for a specific user |

**Example - Create Task**

```json
{
  "title": "Finish FastAPI project",
  "description": "Implement all endpoints",
  "due_date": "2025-06-25",
  "user_id": 1
}
```

**Example - Update Task Status**

```json
{
  "status": "completed"
}
```

> Only allowed status values: `"pending"`, `"in_progress"`, `"completed"`

---

## ✅ Validations Included

* Email format is checked (`EmailStr`)
* Username must be 3–20 characters
* Due date must be today or in the future
* Task status is validated strictly

---

## 🧠 Technologies Used

* Python 🐍
* FastAPI ⚡
* Pydantic ✅
* Swagger UI (auto-generated)

