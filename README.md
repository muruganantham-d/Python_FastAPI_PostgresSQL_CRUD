# 📚 Bookstore API (FastAPI + PostgreSQL)

A simple CRUD API built with **FastAPI**, **SQLAlchemy**, and **PostgreSQL**

---

## 🚀 Features
- ✅ Create and list books
- ✅ PostgreSQL integration
- ✅ SQLAlchemy ORM models
- ✅ Pydantic v2 schemas for request/response validation
- ✅ Dependency-injected DB session
- ✅ Interactive Swagger docs

---

## 🛠️ Tech Stack
- [FastAPI](https://fastapi.tiangolo.com/) — web framework
- [SQLAlchemy](https://www.sqlalchemy.org/) — ORM
- [PostgreSQL](https://www.postgresql.org/) — database
- [Pydantic v2](https://docs.pydantic.dev/latest/) — validation
- [Uvicorn](https://www.uvicorn.org/) — ASGI server

---

## 📂 Project Structure
bookstore-api/
├── db.py # Database config & session
├── main.py # FastAPI app entrypoint
├── models.py # SQLAlchemy models
├── schemas.py # Pydantic schemas
├── services.py # CRUD logic
├── requirements.txt
└── README.md

yaml
Copy
Edit

---

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/muruganantham-d/Python_FastAPI_PostgresSQL_CRUD.git
cd bookstore-api
2. Create and activate a virtual environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Set up PostgreSQL
Make sure PostgreSQL is installed and running

Create the database:

bash
Copy
Edit
createdb bookstore
Add a .env file in the root:

env
Copy
Edit
DATABASE_URL=postgresql://postgres:your_password@localhost:5432/bookstore
5. Run the app
bash
Copy
Edit
uvicorn main:app --reload
🔗 API Endpoints
Books
GET /books/ → List all books

POST /books/ → Create a new book

Example (POST /books/)
json
Copy
Edit
{
  "title": "The Pragmatic Programmer",
  "author": "Andrew Hunt",
  "description": "Classic programming book",
  "year": 1999
}
📖 API Docs
Swagger UI → http://127.0.0.1:8000/docs

ReDoc → http://127.0.0.1:8000/redoc

🧑‍💻 Contributing
Fork the repo

Create a new branch

Commit your changes

Push and open a Pull Request

📜 License
MIT License © 2025

yaml
Copy
Edit

---


