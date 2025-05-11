# 🚀 FastAPI "Hello World" Project with UV
Welcome to first **FastAPI** project! This guide walks you through setting up and running a simple 
"Hello World" API using **UV**, a fast Python dependency and virtual environment manager

## 📚 Table of Contents
* [Overview](#overview)
* [Prerequisites](#prerequisites)
* [Installation & Setup](#installation--setup)
* [Project Structure](#project-structure)
* [API Endpoints](#api-endpoints)
* [Running the Server](#running-the-server)
* [Interactive API Docs](#interactive-api-docs)
* [Testing](#testing)
* [Troubleshooting](#troubleshooting)
* [License](#license)

## ✅ Overview
This project demonstrates how to set up a basic **FastAPI** application using **UV** FastAPI is a modern web
framework built for speed, automatic docs and ease of development

### Key Features
* FastAPI with type checking and validation
* Dependency management using `uv`
* Automatic API docs via Swagger and ReDoc
* Lightweight "Hello World" API example

## ⚙️ Installation & Setup
### Step 1: Project Initialization

```bash
uv init fastdca-p1
cd fastdca-p1
```

### Step 2: Create and Activate Virtual Environment

On macOS/Linux:

```bash
uv venv
source .venv/bin/activate
```

On Windows:

```bash
uv venv
.venv\Scripts\activate
```

> **Note**: With PEP 582 (Python 3.11+), manual activation may not be needed.

### Step 3: Install Dependencies

```bash
uv add "fastapi[standard]"
uv add --dev pytest pytest-asyncio
```

---

## 🗂 Project Structure

```
fastdca-p1/
├── main.py               # FastAPI application
├── pyproject.toml        # Project config and dependencies
├── README.md             # Project documentation
├── .venv/                # Virtual environment
└── uv.lock               # Lock file for uv
```

---

## 📌 API Endpoints

### Root Endpoint `/`

* **Method**: `GET`
* **Response**:

```json
{ "Hello": "World" }
```

### Items Endpoint `/items/{item_id}`

* **Method**: `GET`
* **Path Parameter**: `item_id` (integer)
* **Query Parameter (optional)**: `q` (string)
* **Response**:

```json
{
  "item_id": 123,
  "q": "optional query"
}
```

### Example Code in `main.py`:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}
```

---

## ▶️ Running the Server

Use either of the following commands:

### Option 1: FastAPI CLI (Development Mode)

```bash
fastapi dev main.py
```

### Option 2: Using Uvicorn with UV

```bash
uv run uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

> Visit: `http://localhost:8000`

---

## 🧪 Interactive API Docs

* Swagger UI: [`http://localhost:8000/docs`](http://localhost:8000/docs)
* ReDoc: [`http://localhost:8000/redoc`](http://localhost:8000/redoc)

---

## 🧪 Testing

```bash
pytest
```

* `pytest-asyncio` supports async FastAPI test functions.

---

## 🛠 Troubleshooting

* **Port in Use**: Use another port or stop the running process.
* **FastAPI not found**: Ensure it's installed in your local environment.
* **Module not found**: Check that `.venv` is activated and `uv` dependencies are installed.

---

## 📜 License

This project is open-source. Feel free to use and modify it.

---

Let me know if you’d like a sample `pyproject.toml` or test file included too?
