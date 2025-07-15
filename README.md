# 🧠 StashBrain

**StashBrain** is a fully self-hosted, open-source **second brain** system designed for capturing ideas, journaling, saving links, managing tasks, and uploading files — with no cloud or AI dependencies.

Built for privacy, simplicity, and long-term extensibility.

---

## ✨ Features

- 🧠 **Capture anything** — links, ideas, tasks, notes, and files
- 📆 **Daily journaling** with rich text editor
- 🔐 **User authentication** (username/password)
- 📂 **Self-hosted file uploads**
- 🌐 **Frontend + Backend included**
- 🐳 **Runs with Docker**
- 💌 **Email notifications via SMTP (optional)**

---

## 🛠️ Tech Stack

- **Backend**: FastAPI + SQLAlchemy + SQLite (or Postgres)
- **Frontend**: React + TailwindCSS
- **Auth**: JWT-based login with password hashing
- **Storage**: Local filesystem
- **Dev Tools**: Docker, MailDev (for testing SMTP)

---

## 🚀 Getting Started

### 1. Clone this repo

```bash
git clone https://github.com/yourusername/stashbrain.git
cd stashbrain
```

### 2. Copy the environment file

```bash
cp .env.example .env
```

Update values in `.env` as needed.

### 3. Build and run using Docker

```bash
docker compose up --build
```

This will launch:

- `backend`: FastAPI server at http://localhost:8000
- `frontend`: React app at http://localhost:3000
- `maildev`: Dev email viewer at http://localhost:1080

### 4. Initialise the database

```bash
docker compose exec backend python init_db.py
```

---

## 🧪 API Docs

Once running, visit [http://localhost:8000/docs](http://localhost:8000/docs) for full OpenAPI documentation and test console.

---

## 🔒 User Auth

- Register via `/auth/register`
- Login to receive JWT via `/auth/login`
- Use the token for authenticated requests

---

## 📂 File Uploads

Files are stored in the `/uploads` directory and served at `/uploads/<filename>`.

---

## 📥 Coming Soon

- Tag filtering and search
- Task manager view
- Export options
- Mobile layout improvements

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 💬 Contributions Welcome!

This project is just getting started — feel free to fork, submit issues, or open PRs. Let’s build a simple and open second brain together.
