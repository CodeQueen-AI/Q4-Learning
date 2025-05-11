# 💡 **What is Pydantic?**

**Pydantic** is a Python library used for **data validation** and **settings management** through **Python type hints** It is the core validation tool for **FastAPI**, ensuring:
* API **request validation**
* API **response formatting**
* **Error handling** and type safety

# 🧠 **Why Use Pydantic?**

Pydantic helps you ensure:

* Data is of the correct **type** (e.g., `int`, `str`, `List[str]`)
* **Optional fields** work as expected
* **Default values** are handled automatically
* You can create **nested models**
* You can **add custom validators** to enforce your own rules

---

# ✅ **Pydantic Validation Examples**

### 🔹 **1. Basic Model Validation**

* Ensures fields like `int`, `str`, etc., are the correct type.
* Automatically provides an **error** if invalid data is passed.

### 🔹 **2. Nested Models**

* Supports **nested models** where one model can be used inside another.
* For example, an `Address` model inside a `User` model.


### 🔹 **3. Custom Validators**

* Allows you to define your own rules (e.g., validating the length of a name).
* Pydantic will show an error if your custom validation fails.


### 🔹 **4. FastAPI Integration**

* Seamlessly integrates with **FastAPI**, automatically validating request data.
* Handles complex features like **session ID creation** and **timestamp generation**.

---

# 🔧 **Installation Steps (Locally)**

To test Pydantic and FastAPI locally:

```bash
python -m venv .venv
source .venv/bin/activate  # For Windows: .venv\Scripts\activate
pip install pydantic fastapi email-validator uvicorn
```

To run the FastAPI server:

```bash
uvicorn main:app --reload
```

Visit: `http://127.0.0.1:8000/docs` to test the API.

---

# ✨ **Summary**

**Pydantic** is a Python library that validates your data, ensuring correct types such as `int`, `str`, and `email` in FastAPI apps. If there is an issue, it automatically provides a clear error message.

It is used for:

* **Accurate data validation** ✅
* **Clean error messages** ❌
* **Structured APIs** 🧱


*"The journey of a thousand miles begins with a single step Keep coding, keep growing!"* ✨

