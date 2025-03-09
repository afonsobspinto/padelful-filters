# 🎾 Padel Racket Filtering API 🎾

I wanted to buy a **padel racket** as a **birthday gift** for my father, but the [Padelful](https://www.padelful.com/en/rackets) website lacked the filtering options I needed. To solve this, I **scraped their data** and built an API that enables custom filtering. With this API, I can now effortlessly find the perfect padel racket for my Dad based on attributes like **power, control, rebound, maneuverability, sweet spot, and overall rating**. Happy birthday, Dad! 🎂

---

## 🔥 Getting Started

### 1️⃣ Clone the Repository
```sh
git clone git@github.com:afonsobspinto/padelful-filters.git
cd padelful-filters
```

### 2️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 3️⃣ Apply Migrations
```sh
alembic upgrade head
```

### 4️⃣ Launch the API
```sh
uvicorn app.main:app --reload
```
📌 The API will be available at **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)** 🎉

---

## 🚀 API Endpoints

### ✅ Retrieve All Rackets
```http
GET /rackets/
```

### ✅ Filter by Power (`power > 90`)
```http
GET /rackets/?power_gt=90
```

### ✅ Filter & Sort Results
```http
GET /rackets/?power_gt=85&sort_by=overall_rating&order=desc
```

---

## 🌱 Database Seeding
To populate the database with scraped data:
```sh
python -m app.seed
```

---

## 🛠️ Technology Stack

- **FastAPI** - High-performance API framework.
- **SQLAlchemy** - ORM for managing database operations.
- **Alembic** - Handles database migrations.
- **Pydantic** - Ensures data validation.
- **SQLite** - Lightweight database storage.

---

## ⚠️ Disclaimer

This project **scrapes data from the Padelful website** solely for personal and demonstration purposes. **All racket data remains the property of Padelful** and must **not be used, distributed, or republished without explicit permission**.

---
