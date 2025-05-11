# 🚀 Validated Item API with FastAPI
A beginner-friendly REST API built with FastAPI, demonstrating how to handle path parameters, query parameters, and request bodies with built-in validation and documentation support. This project serves as a practical example of how to structure modern Python APIs with clear, validated inputs.

## 🌟 Features

* Path parameters with type and value validation
* Query parameters with length and range constraints
* Request body validation using **Pydantic** models
* Optional and required parameters support
* Interactive API documentation generated automatically
* Clean and beginner-friendly structure
  
## 📁 Project Setup

### 1. Clone and Initialize the Project

```bash
uv init fastdca_p1
cd fastdca_p1
uv venv
source .venv/bin/activate  # or .venv\Scripts\activate for Windows
uv add "fastapi[standard]"
```

### 2. File Structure

```
fastdca_p1/
├── main.py
├── pyproject.toml
└── README.md  ← (You're here!)
```

---

## 🧠 Understanding FastAPI Parameters

FastAPI provides different ways to handle incoming data:

1. **Path Parameters** → `/items/{item_id}`
2. **Query Parameters** → `/items/?q=test&skip=0`
3. **Request Body** → JSON data sent via POST or PUT
4. **Headers, Cookies, Form, File** → Advanced use cases (not covered here)

---

## 🛠 Example Code (main.py)

```python
from fastapi import FastAPI, Path, Query, Body
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float

@app.get("/items/{item_id}")
async def read_item(
    item_id: int = Path(..., title="The ID of the item", ge=1)
):
    return {"item_id": item_id}

@app.get("/items/")
async def read_items(
    q: str | None = Query(None, title="Query string", min_length=3, max_length=50),
    skip: int = Query(0, ge=0),
    limit: int = Query(10, le=100)
):
    return {"q": q, "skip": skip, "limit": limit}

@app.put("/items/validated/{item_id}")
async def update_item(
    item_id: int = Path(..., title="Item ID", ge=1),
    q: str | None = Query(None, min_length=3),
    item: Item | None = Body(None, description="Optional item data (JSON body)")
):
    result = {"item_id": item_id}
    if q:
        result.update({"q": q})
    if item:
        result.update({"item": item.model_dump()})
    return result
```

---

## ▶️ Run the Application

```bash
fastapi dev main.py
```

Or use:

```bash
uvicorn main:app --reload
```

Access your API at:
👉 `http://localhost:8000/docs` (Swagger UI)
👉 `http://localhost:8000/redoc` (ReDoc)

---

## 🔍 API Endpoints Summary

### 1. **Get Item by ID**

* `GET /items/{item_id}`
* Validates: `item_id >= 1`
* Example: `GET /items/5`

### 2. **Get List of Items**

* `GET /items/`
* Optional query parameters:

  * `q` (3-50 characters)
  * `skip` (>=0)
  * `limit` (<=100)

### 3. **Update Item**

* `PUT /items/validated/{item_id}`
* Combines:

  * `Path`: `item_id`
  * `Query`: `q`
  * `Body`: `Item` (name, description, price)

---

## 🧪 Example Usage with curl

```bash
curl http://localhost:8000/items/1

curl "http://localhost:8000/items/?q=shoes&skip=0&limit=10"

curl -X PUT "http://localhost:8000/items/1?q=update" \
     -H "Content-Type: application/json" \
     -d '{"name": "Updated Item", "description": "Updated description", "price": 25.5}'
```

---

## 📋 Key Takeaways

* Use `Path()` to validate path parameters (like IDs).
* Use `Query()` to validate optional query string inputs.
* Use `Body()` and Pydantic models for structured JSON input.
* FastAPI automatically validates and returns helpful errors on failure.
* Interactive docs make testing your API fun and easy!



## 🌈 Quote

> *"Every line of code you write today is a building block of your future self. Keep coding, Code Queen — your empire is under construction"* 👑💻


