
## 💡 **What is Pydantic?**

**Pydantic** is a Python library used for **data validation** and **settings management** using **Python type hints**.

It is the backbone of FastAPI for handling:

* API **request validation**
* API **response formatting**
* **Error handling** and type safety

---

## 🧠 **Why Use Pydantic?**

It helps you ensure:

* The data is of the correct **type** (e.g., `int`, `str`, `List[str]`)
* Optional fields work as expected
* **Default values** are handled automatically
* You can build **nested models**
* You can **add custom validators** for your own rules

---

## ✅ **Pydantic Validation Examples**

Let’s walk through examples one by one:

---

### 🔹 1. **Basic Model Validation**

**File**: `pydantic_example_1.py`

```python
from pydantic import BaseModel, ValidationError

class User(BaseModel):
    id: int
    name: str
    email: str
    age: int | None = None  # optional

# Valid input
user = User(id=1, name="Alice", email="alice@example.com", age=25)

# Invalid input
try:
    User(id="abc", name="Bob", email="bob@example.com")
except ValidationError as e:
    print(e)
```

✅ Automatically checks if `id` is an `int`
❌ Gives a **clear error** if wrong type is passed

---

### 🔹 2. **Nested Models**

**File**: `pydantic_example_2.py`

```python
from pydantic import BaseModel, EmailStr

class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class UserWithAddress(BaseModel):
    id: int
    name: str
    email: EmailStr
    addresses: list[Address]

user_data = {
    "id": 2,
    "name": "Bob",
    "email": "bob@example.com",
    "addresses": [
        {"street": "123 Main St", "city": "New York", "zip_code": "10001"},
    ]
}
user = UserWithAddress.model_validate(user_data)
```

✅ Supports **nested data structures**
✅ Built-in **email format** validation

---

### 🔹 3. **Custom Validators**

**File**: `pydantic_example_3.py`

```python
from pydantic import BaseModel, EmailStr, validator, ValidationError
from typing import List

class UserWithAddress(BaseModel):
    id: int
    name: str
    email: EmailStr
    addresses: List[Address]

    @validator("name")
    def name_must_be_at_least_two_chars(cls, v):
        if len(v) < 2:
            raise ValueError("Name must be at least 2 characters long")
        return v
```

✅ You can create **custom rules**
❌ Gives **clear custom error** if rule is broken

---

### 🔹 4. **FastAPI Integration**

**File**: `main.py`

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from datetime import datetime, UTC
from uuid import uuid4

app = FastAPI()

class Metadata(BaseModel):
    timestamp: datetime = Field(default_factory=lambda: datetime.now(tz=UTC))
    session_id: str = Field(default_factory=lambda: str(uuid4()))

class Message(BaseModel):
    user_id: str
    text: str
    metadata: Metadata
    tags: list[str] | None = None

class Response(BaseModel):
    user_id: str
    reply: str
    metadata: Metadata

@app.post("/chat/", response_model=Response)
async def chat(message: Message):
    if not message.text.strip():
        raise HTTPException(status_code=400, detail="Message text cannot be empty")
    return Response(
        user_id=message.user_id,
        reply=f"Hello {message.user_id}, you said: {message.text}",
        metadata=Metadata()
    )
```

✅ Automatically handles validation in FastAPI
✅ Supports **timestamp and session ID generation**
✅ Uses **nested models** inside API requests/responses

---

## 🔧 Installation Steps (if you're testing locally)

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install pydantic fastapi email-validator uvicorn
```

Run:

```bash
uvicorn main:app --reload
```

Go to: `http://127.0.0.1:8000/docs` to test the API.

---

## ✨ Summary (Urdu + English)

**Pydantic** aik library hai jo aap ke data ko validate karti hai.
Aap ke FastAPI app mein ye ensure karti hai ke user se milne wali har value sahi type ki ho.
Jaise `int`, `str`, ya `email`. Agar koi problem ho to ye **automatic error** dikhati hai.

It helps in:

* Accurate data validation ✅
* Clean error messages ❌
* Structured APIs 🧱

---

Would you like me to create practice tasks or a mini-project using Pydantic and FastAPI to help you practice these skills further?
