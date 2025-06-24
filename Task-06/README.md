Absolutely Code Queen 👑!
Here’s a clear, professional, and beginner-friendly **`README.md` file** for your **Task Tracker API project** — explaining how to install, run, and use all the endpoints with full clarity. 💡

---

## 🧩 `README.md` for Task Tracker API

````markdown
# ✅ Task Tracker API (Built with FastAPI)

This is a simple **Task Management API** built using **FastAPI** and **Pydantic**.  
It lets you create users, assign tasks to them, update task status, and retrieve task lists.

---

## 📦 Features

- Create and fetch users 👤
- Create tasks for users 📝
- Update task status (pending, in_progress, completed) 🔁
- View all tasks assigned to a user 📋
- All data stored temporarily using in-memory dictionaries 🧠

---

## 🛠️ Installation Guide

### 1. 📂 Clone this repository (or copy files)
```bash
git clone https://github.com/your-username/task-tracker-api.git
cd task-tracker-api
````

### 2. 📦 Install dependencies

Make sure Python is installed (version 3.8+ recommended).

Install **FastAPI** and **Uvicorn** using pip:

```bash
pip install fastapi uvicorn
```

> If using requirements.txt, you can do:

```bash
pip install -r requirements.txt
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

---

## 💡 Project Status

This is a basic prototype using in-memory storage.
For production use, connect it with a real database like PostgreSQL, MongoDB, or SQLite.

---

## 🏁 Getting Started for Beginners

| Term   | Meaning                                         |
| ------ | ----------------------------------------------- |
| `GET`  | Read data from server (e.g., get user info)     |
| `POST` | Send data to server (e.g., create user or task) |
| `PUT`  | Update existing data (e.g., update task status) |

---

## 💖 Made with love by Code Queen 👑

```

---

Would you like me to save this as a file and send it to you? Or help you set it up in GitHub too? You’re ready to show off your skills! 💪🚀
```
