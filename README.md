# Finance Tracker API

A personal finance management REST API built as a portfolio project. Allows users to manage accounts, track income and expenses, and categorize transactions.

---

## Stack

| Layer | Technology |
|---|---|
| Language | Python 3.11 |
| Framework | FastAPI |
| ORM | SQLAlchemy |
| Migrations | Alembic |
| Database | PostgreSQL |
| Auth | JWT (python-jose) |
| Validation | Pydantic v2 |
| Server | Uvicorn |

---

## Architecture

The project follows a layered architecture with clear separation of concerns:

```
backend/
    app/
        api/          # Route handlers — receives requests, returns responses
        models/       # SQLAlchemy models — maps Python classes to DB tables
        schemas/      # Pydantic schemas — validates input and output data
        services/     # Business logic — rules that don't belong in routes or models
        core/         # Central config — database connection, environment variables
    tests/
```

Each layer has a single responsibility and only communicates with the adjacent layer. `api/` never touches `models/` directly — it always goes through `services/`.

---

## Data Model

> DER — pending (to be added after entity design session)

### Entities

**User**
- id, email, password_hash, created_at

**Account**
- id, user_id (FK), name

**Category**
- id, user_id (FK), name, description

**Transaction**
- id, account_id (FK), category_id (FK), amount, type (ENUM: income/expense), description, date

### Relationships

```
User     1:N  Account
User     1:N  Category
Account  1:N  Transaction
Category 1:N  Transaction
```

### Design decisions

- **No balance column on Account**: balance is derived by summing transactions. Storing it separately risks inconsistency if a bug skips the update.
- **Transaction type as ENUM**: avoids inconsistent string values like `"gasto"`, `"Gasto"`, `"expense"`. Fixed vocabulary enforced at the DB level.
- **Category as a separate entity**: avoids duplicating category names across transactions. Renaming a category updates it in one place.

---

## Local Setup

### Requirements

- Python 3.11+
- PostgreSQL 18+
- Git

### Installation

```bash
# Clone the repository
git clone https://github.com/Lchurrasqui/finance-tracker.git
cd finance-tracker/backend

# Create and activate virtual environment
python -m venv venv
source venv/Scripts/activate  # Windows (Git Bash)
source venv/bin/activate       # Mac / Linux

# Install dependencies
pip install -r requirements.txt
```

### Environment variables

Create a `.env` file inside `backend/` with the following:

```
DATABASE_URL=postgresql://postgres:your_password@localhost:5432/finance_tracker
SECRET_KEY=your_secret_key
```

### Database

```bash
# Create the database in PostgreSQL
CREATE DATABASE finance_tracker;

# Run migrations (once Alembic is configured)
alembic upgrade head
```

### Run the server

```bash
cd backend
uvicorn app.main:app --reload
```

API available at: `http://localhost:8000`
Interactive docs: `http://localhost:8000/docs`

---

## API Endpoints

> Full documentation available at `/docs` (Swagger UI) when running locally.

| Method | Route | Description | Auth required |
|---|---|---|---|
| GET | /health | Health check | No |

*More endpoints to be added as development progresses.*

---

## Project Status

| Phase | Status |
|---|---|
| Git & GitHub setup | ✅ Complete |
| Project structure & environment | ✅ Complete |
| FastAPI + DB connection | ✅ Complete |
| Entity design & migrations | 🔄 In progress |
| CRUD endpoints | ⏳ Pending |
| JWT Authentication | ⏳ Pending |
| Frontend (React) | ⏳ Pending |
| Docker & Deploy | ⏳ Pending |


1. Definición del Problema y Solución

Problema: Gestionar finanzas personales de forma manual es tedioso, propenso a errores y dificulta el análisis histórico de gastos para tomar decisiones de ahorro.

Solución: Una API Backend que permita centralizar el registro de ingresos y gastos, categorizarlos y consultar reportes de balance de forma programática.

2. Casos de Uso (¿Qué puede hacer el usuario?)

Registrar Usuario: El usuario crea una cuenta con email y contraseña.

Cargar Transacción: El usuario registra un monto, indica si es gasto/ingreso y le asigna una categoría.

Consultar Balance: El usuario pide ver cuánto dinero tiene disponible (Ingresos - Gastos).

Listar Movimientos: El usuario ve su historial filtrado por fecha o categoría.

3. User stories

    As a user, I want to create an account so that I can track my finances.

    As a user, I want to log in so that I can access my financial data.

    As a user, I want to add transactions manually so that I can record my expenses and income.

    As a user, I want to edit or delete transactions so that I can correct mistakes.

    As a user, I want to create categories so that I can organize my transactions.

    As a user, I want to see a graphical summary of my expenses so that I understand my spending habits.

    As a user, I want to import transactions from a CSV file so that I can upload data from my bank.

    As a user, I want to see my monthly balance so that I know if I am saving or spending more than I earn.

3. Requerimientos Funcionales (RF)

RF1: El sistema debe permitir el login seguro.

RF2: El sistema debe validar que no se ingresen montos negativos.

RF3: El sistema debe permitir crear categorías personalizadas (ej: "Suscripciones", "UTN").

