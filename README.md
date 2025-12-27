# StreamQuest (Flask)

Simple Flask app for managing users and OTT-style content. Uses Flask, Flask-SQLAlchemy and Flask-Migrate. Includes blueprints for authentication, content listing/details, and a minimal admin route for adding content.

## Features

- **Auth:** signup and login flows (routes in `routes/auth.py`).
- **Content:** list, details and JSON API for contents (`routes/content.py`).
- **Admin:** add content via a POST route (`routes/admin.py`).
- **DB migrations:** powered by Flask-Migrate / Alembic (migrations/ present).

## Requirements

See `requirements.txt` for full pinned dependencies. Key libraries used:

- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- SQLAlchemy
- PyMySQL (optional if using MySQL)

## Quickstart (development)

1. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Configure database (default)

The default configuration is in `config.py` and uses SQLite:

```py
SQLALCHEMY_DATABASE_URI = "sqlite:///ott.db"
```

To use a different database, update `SQLALCHEMY_DATABASE_URI` or set your own config.

3. Run migrations (if needed)

If this is a fresh checkout and you want to apply existing migrations:

```bash
export FLASK_APP=app.py
flask db upgrade
```

To create a new migration after model changes:

```bash
flask db migrate -m "describe change"
flask db upgrade
```

4. Run the app

```bash
python app.py
# or
export FLASK_APP=app.py
flask run
```

The app serves pages like `/`, `/login`, `/signup`, and `/admin` and registers blueprints for API-like endpoints.

## Important Routes

- **Frontend pages:** `/`, `/login`, `/signup`, `/admin`
- **Auth (blueprint `auth_bp`):** `POST /auth/signup`, `POST /auth/login`
- **Content (blueprint `content_bp`):** `GET /contents` (JSON), `GET /details/<id>` (details page)
- **Admin (blueprint `admin_bp`):** `POST /admin/content` to add content

## Models (summary)

- `User`: `id`, `name`, `email` (unique), `password`, `is_admin`
- `Content`: `id`, `title`, `description`, `genre`

## Project layout

- `app.py` - application factory and top-level routes
- `config.py` - app configuration
- `extensions.py` - extension instances (e.g. `db`, `migrate`)
- `models.py` - SQLAlchemy models
- `routes/` - blueprints for `auth`, `content`, `admin`
- `templates/` - Jinja templates for pages
- `static/` - static assets (CSS/JS)
- `migrations/` - Alembic migration history

## Notes & Next Steps

- Passwords are stored directly in the `password` column in `models.py`. Add hashing (e.g. `werkzeug.security.generate_password_hash`) before storing credentials.
- Add proper session/CSRF protection and input validation for production.
- Consider externalizing config (environment variables) and adding a `.env` or instance config.

## License

Add a license file if you plan to open-source the project.

## Usage examples (code)

Quick curl and Python examples to exercise the main endpoints (development, `localhost:5000`):

- Signup (JSON):

```bash
curl -X POST http://localhost:5000/auth/signup \
	-H "Content-Type: application/json" \
	-d '{"name":"Alice","email":"alice@example.com","password":"secret"}' \
	-v
```

- Login (form, save cookies):

```bash
curl -X POST http://localhost:5000/auth/login \
	-d "email=alice@example.com&password=secret" \
	-c cookies.txt -L -v
```

- Add content (use saved session cookies):

```bash
curl -X POST http://localhost:5000/admin/content \
	-H "Content-Type: application/json" \
	-d '{"title":"My Show","description":"A great show","genre":"Drama"}' \
	-b cookies.txt -L -v
```

- List contents (JSON):

```bash
curl http://localhost:5000/contents
```

- Details page (HTML):

```bash
curl http://localhost:5000/details/1
```

Python (requests) example:

```python
import requests

base = "http://localhost:5000"
sess = requests.Session()

# Signup
sess.post(f"{base}/auth/signup", json={"name":"Bob","email":"bob@example.com","password":"pw"})

# List contents
resp = sess.get(f"{base}/contents")
print(resp.json())
```

Notes: these examples assume the app is running locally and uses the default session/cookie behavior. Use `-L` with `curl` to follow redirects and `-c`/`-b` to persist cookies between requests.
