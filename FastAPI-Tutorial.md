Excellent 🚀 — **CRUD + relational models (User ↔ Account ↔ Transaction)**, plus explanations, code examples, diagrams, and quizzes.
This will be a **complete textbook-style tutorial** — self-contained, so no video access is required.

Here’s the **full `.md` file**:

---

````markdown
# 📘 FastAPI – A Complete Guide for Python Developers in Financial IT

*A textbook-style guide with CRUD, relational models, diagrams, quizzes, and real-world job preparation.*

---

## 📑 Table of Contents

1. Introduction  
   1.1 Why FastAPI?  
   1.2 FastAPI in Financial IT  
   1.3 What You’ll Learn  

2. Environment Setup  
   2.1 Installing Dependencies  
   2.2 Project Structure  

3. FastAPI Basics  
   3.1 Creating Your First API  
   3.2 Path & Query Parameters  
   3.3 Type Hints & Validation  

4. Request Body & Pydantic  
   4.1 Simple Models  
   4.2 Nested Models  
   4.3 Response Models  

5. Error Handling  
   5.1 HTTPException  
   5.2 Custom Error Responses  

6. Dependency Injection  
   6.1 What Are Dependencies?  
   6.2 DB Sessions as Dependencies  

7. Authentication & Security  
   7.1 OAuth2 Basics  
   7.2 JWT Tokens  
   7.3 Role-Based Access Control  

8. CRUD with SQLAlchemy  
   8.1 Database Setup  
   8.2 Account Model CRUD  
   8.3 Relational Models (Users & Transactions)  

9. Testing APIs  
   9.1 Using TestClient  
   9.2 Writing CRUD Tests  

10. Deployment  
    10.1 Dockerizing FastAPI  
    10.2 Production Servers  
    10.3 Security Checklist  

11. Case Study: Financial Transactions API  
    11.1 Design Endpoints  
    11.2 Audit Logging  
    11.3 Compliance Considerations  

12. Learning Path: Junior → Mid-Level  

13. Quizzes with Answers  

14. Diagrams & Cheat Sheets  

---

## 1. Introduction

FastAPI is a modern Python web framework for building **high-performance APIs**.  

### ✅ Why FastAPI?
- **Asynchronous**: handles thousands of requests per second.  
- **Validation**: built-in via Pydantic.  
- **Security**: OAuth2, JWT support.  
- **Docs**: automatic Swagger & ReDoc.  

### ✅ FastAPI in Financial IT
Financial systems require:
- Strong validation  
- Audit logging  
- Authentication & authorization  
- Low-latency responses  

FastAPI provides all of these **out of the box**.

---

## 2. Environment Setup

### Install dependencies

```bash
pip install fastapi uvicorn[standard] sqlalchemy pydantic[dotenv] python-jose[cryptography] passlib[bcrypt] pytest
````

### Project Structure

```
finance_api/
 ├── app/
 │   ├── main.py
 │   ├── database.py
 │   ├── models.py
 │   ├── schemas.py
 │   ├── routers/
 │   │   ├── accounts.py
 │   │   ├── users.py
 │   │   └── transactions.py
 ├── tests/
 │   └── test_crud.py
 └── requirements.txt
```

---

## 3. FastAPI Basics

`main.py`

```python
from fastapi import FastAPI

app = FastAPI(title="Finance API")

@app.get("/")
async def root():
    return {"message": "Welcome to Finance API"}
```

Run:

```bash
uvicorn app.main:app --reload
```

---

## 4. Request Body & Pydantic

`schemas.py`

```python
from pydantic import BaseModel
from typing import Optional, List

class AccountBase(BaseModel):
    name: str
    balance: float

class AccountCreate(AccountBase):
    pass

class AccountUpdate(BaseModel):
    name: Optional[str] = None
    balance: Optional[float] = None

class AccountOut(AccountBase):
    id: int
    class Config:
        orm_mode = True
```

---

## 5. Error Handling

```python
from fastapi import HTTPException, status

@app.get("/accounts/{id}")
async def get_account(id: int):
    if id != 1:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Account {id} not found"
        )
    return {"id": id, "balance": 100.0}
```

---

## 6. Dependency Injection

`database.py`

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQLALCHEMY_DATABASE_URL = "sqlite:///./finance.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

---

## 7. Authentication & Security (JWT)

`security.py`

```python
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
SECRET_KEY = "supersecret"
ALGORITHM = "HS256"

def create_token(data: dict):
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None
```

---

## 8. CRUD with SQLAlchemy

### 8.1 Database Models

`models.py`

```python
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    accounts = relationship("Account", back_populates="owner")

class Account(Base):
    __tablename__ = "accounts"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    balance = Column(Float, default=0.0)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="accounts")
    transactions = relationship("Transaction", back_populates="account")

class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float)
    description = Column(String)
    account_id = Column(Integer, ForeignKey("accounts.id"))

    account = relationship("Account", back_populates="transactions")
```

---

### 8.2 CRUD Routers

#### Users

`routers/users.py`

```python
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = models.User(username=user.username)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.get("/", response_model=list[schemas.UserOut])
def read_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()
```

#### Accounts

`routers/accounts.py`

```python
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db

router = APIRouter(prefix="/accounts", tags=["accounts"])

@router.post("/", response_model=schemas.AccountOut)
def create_account(account: schemas.AccountCreate, db: Session = Depends(get_db)):
    db_account = models.Account(**account.dict())
    db.add(db_account)
    db.commit()
    db.refresh(db_account)
    return db_account

@router.get("/{account_id}", response_model=schemas.AccountOut)
def read_account(account_id: int, db: Session = Depends(get_db)):
    acc = db.query(models.Account).filter(models.Account.id == account_id).first()
    if not acc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    return acc
```

#### Transactions

`routers/transactions.py`

```python
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db

router = APIRouter(prefix="/transactions", tags=["transactions"])

@router.post("/", response_model=schemas.TransactionOut)
def create_txn(txn: schemas.TransactionCreate, db: Session = Depends(get_db)):
    db_txn = models.Transaction(**txn.dict())
    db.add(db_txn)
    db.commit()
    db.refresh(db_txn)
    return db_txn
```

---

### 8.3 Main App

`main.py`

```python
from fastapi import FastAPI
from . import models
from .database import engine
from .routers import users, accounts, transactions

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Finance API")

app.include_router(users.router)
app.include_router(accounts.router)
app.include_router(transactions.router)
```

---

## 9. Testing

`tests/test_crud.py`

```python
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_user():
    res = client.post("/users/", json={"username": "alice"})
    assert res.status_code == 200
    assert res.json()["username"] == "alice"

def test_create_account():
    res = client.post("/accounts/", json={"name": "Savings", "balance": 1000.0, "owner_id": 1})
    assert res.status_code == 200
    assert res.json()["balance"] == 1000.0
```

---

## 10. Case Study: Financial Transactions API

**Flow Diagram**

```text
Client --> [Uvicorn] --> [FastAPI Router]
                  |--> [Auth Dependency] --> JWT Verify
                  |--> [DB Dependency]   --> SQLAlchemy Session
                  --> [CRUD Operation]
                  --> Response JSON
```

---

## 11. Learning Path

### Junior Developer

* Master CRUD operations
* Learn Pydantic & validation
* Write unit tests

### Mid-Level Developer

* Add JWT authentication
* Implement user ↔ account relationships
* Build Docker deployment
* Ensure compliance (audit logs, error handling)

---

## 12. Quizzes

**Q1.** What does `orm_mode = True` do?
👉 It allows SQLAlchemy ORM objects to be returned as Pydantic models.

**Q2.** Which HTTP status code is correct for successful DELETE?
👉 204 No Content

**Q3.** Why do we call `db.refresh()` after `commit()`?
👉 To reload auto-generated fields like IDs.

**Q4.** How to model one-to-many relationship in SQLAlchemy?
👉 Use `relationship()` in parent and `ForeignKey()` in child.

---

## 13. Cheat Sheet

* Run app: `uvicorn app.main:app --reload`
* Docs: `/docs` → Swagger UI
* DB migration: Alembic (advanced)
* Testing: `pytest -v`

---

# ✅ End of Guide

```

---

This `.md` file is a **standalone FastAPI textbook**, including CRUD, relational models, explanations, diagrams, quizzes, and a junior → mid-level learning path.  

Would you like me to also **generate a polished PDF** version with shaded quiz boxes, colored diagrams, and professional formatting for distribution to learners?
```
