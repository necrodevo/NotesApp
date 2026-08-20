<div align="center">

# Basic Notes App

A simple, lightweight notes API built with modern Python tools.

</div>

---

## Tech Stack

* **[FastAPI](https://fastapi.tiangolo.com/)** — high-performance, easy-to-use web framework for building APIs
* **Python type hinting** — clean, maintainable code with full type clarity

---

## How It Works

There is currently no database — an in-memory Python list acts as storage for the lifetime of the server process. Notes are lost on restart.

**Available endpoints:**

| Method | Route | Description |
|---|---|---|
| POST | `/notes` | Create a new note (author, note as query params) |
| GET | `/note/{item_id}` | Retrieve a note by its id (path parameter) |

Note IDs are generated automatically based on the current list length at creation time.

---

## Known Limitations

- `POST /notes` currently accepts `author` and `note` as **query parameters** rather than a JSON request body. This means note content appears directly in the URL and server logs, and is not suitable for long or sensitive text. This was a deliberate choice while learning how query parameters work in FastAPI — a production version would use a Pydantic request body instead.
- Data persists between server restarts - used sqlite through sqlalchemy thought using simple syntax and practice involving ORM is avoided beacause of learning purpose for now.

---

## Running Locally

**1. Start the API server:**
```bash
uvicorn fapi:app --reload
```

**2. In a separate terminal, run the client:**
```bash
python sender.py
```

`uvicorn` starts a local server on `http://127.0.0.1:8000` — the note list lives in memory on this process for as long as it's running.

---

## Roadmap

- [To-Do] Move note creation to a JSON request body via a Pydantic model
- [Done] Add persistent storage (SQLite via SQLAlchemy)
- [To-Do] Add update (`PATCH`) and delete (`DELETE`) endpoints
- [To-Do] Add input validation and error responses for missing/invalid notes