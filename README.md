# personal_notes_manager
---

## 📒 Personal Notes Manager API

A simple yet powerful **FastAPI + MongoDB** based REST API for managing personal notes — with user authentication, searching, and reminders.

---

### 🚀 Features

- 🔐 JWT Authentication (register/login)
- ✅ Create, Read, Update, Delete notes
- 🔍 Search notes by title or tag
- 📅 Get notes due today (reminders)
- 🧪 Built using **FastAPI**, **MongoDB**, **Pydantic**, and **Motor**

---

### 🛠️ Tech Stack

- **Backend**: [FastAPI](https://fastapi.tiangolo.com/)
- **Database**: [MongoDB](https://www.mongodb.com/) (using async `motor`)
- **Auth**: JWT with OAuth2 Password flow
- **Validation**: Pydantic

---

### ⚙️ Setup Instructions

#### 1. Clone the Repo

```bash
git clone https://github.com/your-username/personal-notes-manager.git
cd personal-notes-manager
```

#### 2. Create Virtual Environment

```bash
python -m venv note_env
source note_env/bin/activate  # On Windows: note_env\Scripts\activate
```

#### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

#### 4. Add `.env` file (for secrets)

```env
SECRET_KEY=your-secret-key
MONGO_URL=mongodb://localhost:27017
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

#### 5. Run the API 🚀

```bash
uvicorn main:app --reload
```

---

### 🔌 API Endpoints

#### 🧑 Auth
- `POST /auth/register` – Register a new user
- `POST /auth/login` – Login and get JWT token

#### 📝 Notes
- `POST /notes/` – Create a note (auth required)
- `GET /notes/` – Get all notes
- `GET /notes/{id}` – Get note by ID
- `PUT /notes/{id}` – Update a note
- `DELETE /notes/{id}` – Delete a note

#### 🔍 Search & Reminders
- `GET /search/?query=title_or_tag` – Search notes
- `GET /due-today/` – Get notes due today

---

### 🧠 MongoDB Note Schema

```json
{
  "_id": "ObjectId",
  "title": "Meeting Notes",
  "content": "Discuss project plan",
  "tags": ["work", "urgent"],
  "created_at": "ISODate",
  "updated_at": "ISODate",
  "reminder_date": "ISODate (optional)",
  "user_id": "ObjectId"
}
```

---

### 🧪 Testing the API

Use tools like:
- [Postman](https://www.postman.com/)
- [HTTPie](https://httpie.io/)
- Or Swagger UI: `http://localhost:8000/docs`

---

### 📂 Project Structure

```bash
.
├── main.py
├── models/
│   └── user.py, note.py
├── routes/
│   └── auth.py, notes.py
├── database/
│   └── connection.py
├── utils/
│   └── jwt.py, hashing.py
├── requirements.txt
└── .env
```

---

### ✍️ Author

- **Name**: Umer Farooq  
- **GitHub**: [@Umer786277](https://github.com/Umer786277)

---

### 📄 License

This project is licensed under the MIT License. See `LICENSE` for details.

