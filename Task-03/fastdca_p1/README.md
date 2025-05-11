
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
* Pydantic ensures fields like `int`, `str`, etc., are the correct type.
* If wrong data is provided, it gives an error.

---

### 🔹 2. **Nested Models**
* You can have models inside models.
* For example, an `Address` inside a `User` model.

---

### 🔹 3. **Custom Validators**

* You can create your own rules (like name length).
* Pydantic will show an error if your custom rule is violated.

---

### 🔹 4. **FastAPI Integration**

* Pydantic works with FastAPI to automatically validate request data.
* It also handles things like creating unique session IDs.

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

Pydantic is a library that validates your data.
In your FastAPI app, it ensures that every value received from the user is of the correct type, such as int, str, or email. If there is any issue, it automatically shows an error

It helps in:

* Accurate data validation ✅
* Clean error messages ❌
* Structured APIs 🧱

