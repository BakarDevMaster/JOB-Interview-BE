# AI-Powered Interview Application Backend

A FastAPI-based backend service for conducting AI-powered interviews using Google's Generative AI and LangChain.

## Features

- **FastAPI Framework**: Modern, fast web framework for building APIs
- **AI Integration**: Google Generative AI for intelligent interview questions and evaluation
- **Database Management**: PostgreSQL with SQLModel ORM and Alembic migrations
- **Authentication**: JWT-based user authentication with bcrypt password hashing
- **Modular Architecture**: Clean separation of concerns with routers, models, schemas, and CRUD operations
- **CORS Support**: Configured for frontend integration
- **Vercel Ready**: Optimized for serverless deployment

## Tech Stack

- **Backend**: FastAPI, Python 3.11+
- **Database**: PostgreSQL with SQLModel ORM
- **AI/ML**: LangChain, Google Generative AI
- **Authentication**: JWT, bcrypt
- **Deployment**: Vercel (serverless)
- **Package Management**: Poetry (development), pip (production)

## Project Structure

```
├── app/
│   ├── main.py              # Main FastAPI application
│   ├── database.py          # Database configuration
│   ├── settings.py          # Environment settings
│   ├── dependencies.py      # Dependency injection
│   ├── routers/            # API route handlers
│   │   ├── users.py        # User management endpoints
│   │   ├── categories.py   # Interview category endpoints
│   │   └── session.py      # Interview session endpoints
│   ├── models/             # SQLModel database models
│   ├── schemas/            # Pydantic request/response schemas
│   ├── crud/               # Database CRUD operations
│   └── services/           # Business logic services
├── tests/                  # Test suite
├── index.py                # Vercel entry point
├── main.py                 # Alternative entry point
├── requirements.txt        # Production dependencies
├── pyproject.toml          # Poetry configuration
├── vercel.json             # Vercel deployment configuration
└── DEPLOYMENT.md           # Deployment guide
```

## API Endpoints

### Core Endpoints
- `GET /` - Welcome message and health check
- `GET /docs` - Interactive API documentation (Swagger UI)
- `GET /redoc` - Alternative API documentation

### User Management
- User registration and authentication
- Profile management
- JWT token handling

### Interview Categories
- Category creation and management
- Question categorization

### Interview Sessions
- Session creation and management
- AI-powered question generation
- Response evaluation


## Local Development

### Prerequisites
- Python 3.11+
- PostgreSQL
- Poetry (recommended) or pip

### Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd ai_powered_interview
   ```

2. **Install dependencies**
   
   Using Poetry (recommended):
   ```bash
   poetry install
   poetry shell
   ```
   
   Using pip:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your actual values
   ```

4. **Set up database**
   ```bash
   # Create database
   createdb interview_db
   
   # Run migrations
   alembic upgrade head
   ```

5. **Run the application**
   ```bash
   # Using uvicorn directly
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   
   # Or using the main.py entry point
   python main.py
   ```

6. **Access the application**
   - API: http://localhost:8000
   - Documentation: http://localhost:8000/docs
   - Alternative docs: http://localhost:8000/redoc

## Testing

```bash
# Run tests
pytest

# Run with coverage
pytest --cov=app tests/
```

## Database Migrations

```bash
# Create a new migration
alembic revision --autogenerate -m "Description of changes"

# Apply migrations
alembic upgrade head

# Rollback migration
alembic downgrade -1
```

## Deployment

This application is configured for deployment on Vercel. See [DEPLOYMENT.md](./DEPLOYMENT.md) for detailed instructions.

### Quick Deployment Steps:
1. Push code to GitHub
2. Connect repository to Vercel
3. Set environment variables in Vercel dashboard
4. Deploy

## API Documentation

Once running, visit `/docs` for interactive API documentation with Swagger UI, or `/redoc` for alternative documentation.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass
6. Submit a pull request




