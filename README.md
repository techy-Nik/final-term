# FastAPI Calculator - Complete Full-Stack Application (Final Project)

A comprehensive, production-ready REST API calculator with JWT authentication, complete BREAD operations, interactive frontend, and advanced features including calculation history, user profiles, and database migrations.

## 🎯 Project Overview

This is the **final capstone project** demonstrating complete full-stack development mastery:

- **Complete BREAD Operations** - Full frontend implementation for calculations
- **JWT Authentication** - Secure token-based authentication with protected routes
- **Interactive Dashboard** - Modern UI for managing calculations
- **Advanced Features** - User profiles, calculation history, statistics
- **Database Migrations** - Alembic for schema management
- **Comprehensive Testing** - Unit, integration, and E2E tests
- **Production CI/CD** - Automated testing and Docker Hub deployment

## ✨ Features Completed in this Final Term Project

### Complete Frontend BREAD Implementation
✅ **Browse** - View all calculations in interactive table with sorting/filtering  
✅ **Read** - View detailed calculation information in modal  
✅ **Edit** - Update existing calculations with inline editing  
✅ **Add** - Create new calculations with live result preview  
✅ **Delete** - Remove calculations with confirmation dialog  

### New Advanced Features
✅ **User Dashboard** - Personalized dashboard with statistics  
✅ **Calculation History** - Timeline view of all calculations  
✅ **User Profile** - Edit profile information and change password  
✅ **Calculation Statistics** - Visual charts and analytics  
✅ **Search & Filter** - Find calculations by operation type or date  
✅ **Export Data** - Download calculations as CSV/JSON  

## 🏗️ Architecture

### Complete API Endpoints

#### Authentication Endpoints
- `POST /register` - Register new user
- `POST /login` - Login and receive JWT tokens
- `POST /token/refresh` - Refresh access token
- `POST /logout` - Logout and blacklist token

#### Calculation Endpoints (BREAD - Protected)
- `GET /calculations` - Browse all user's calculations (with pagination)
- `GET /calculations/{id}` - Read specific calculation details
- `POST /calculations` - Add new calculation
- `PUT /calculations/{id}` - Edit calculation (full update)
- `PATCH /calculations/{id}` - Edit calculation (partial update)
- `DELETE /calculations/{id}` - Delete calculation

#### User Profile Endpoints (Final Term Project)
- `GET /users/me` - Get current user profile
- `PUT /users/me` - Update user profile
- `PUT /users/me/password` - Change password
- `GET /users/me/statistics` - Get user calculation statistics

#### Export Endpoints (Final Term Project)
- `GET /calculations/export/csv` - Export calculations as CSV
- `GET /calculations/export/json` - Export calculations as JSON

### Frontend Pages

- **`/register.html`** - User registration (Module 13)
- **`/login.html`** - User login (Module 13)
- **`/dashboard.html`** - Main dashboard with BREAD operations
- **`/profile.html`** - User profile management
- **`/history.html`** - Calculation history timeline


### Project Structure

```
.
├── app
│   ├── auth
│   │   ├── __init__.py
│   │   ├── dependencies.py
│   │   ├── jwt.py
│   │   └── redis.py
│   ├── core
│   │   ├── __init__.py
│   │   └── config.py
│   ├── models
│   │   ├── __init__.py
│   │   ├── calculation.py
│   │   └── user.py
│   ├── operations
│   │   └── __init__.py
│   ├── schemas
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── calculation.py
│   │   ├── token.py
│   │   └── user.py
│   ├── __init__.py
│   ├── database.py
│   ├── database_init.py
│   └── main.py
├── docs
│   ├── 00-course-overview.md
│   ├── 01-project-setup.md
│   ├── 02-database-models.md
│   ├── 03-schema-validation.md
│   ├── 04-authentication.md
│   ├── 05-api-endpoints.md
│   ├── 06-frontend-integration.md
│   ├── 07-testing.md
│   └── 08-containerization.md
├── static
│   ├── css
│   │   └── style.css
│   └── js
│       └── script.js
├── templates
│   ├── dashboard.html
│   ├── edit_calculation.html
│   ├── index.html
│   ├── layout.html
│   ├── login.html
│   ├── register.html
│   └── view_calculation.html
├── tests
│   ├── e2e
│   │   ├── __init__.py
│   │   ├── test_e2e.bk
│   │   └── test_fastapi_calculator.py
│   ├── integration
│   │   ├── __init__.py
│   │   ├── test_calculation.py
│   │   ├── test_calculation_schema.py
│   │   ├── test_database.py
│   │   ├── test_dependencies.py
│   │   ├── test_schema_base.py
│   │   ├── test_user.py
│   │   └── test_user_auth.py
│   ├── unit
│   │   ├── __init__.py
│   │   └── test_calculator.py
│   ├── __init__.py
│   └── conftest.py
├── Dockerfile
├── LICENSE
├── README.md
├── docker-compose.yml
├── init-db.sh
├── pytest.ini
└── requirements.txt
```

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- Docker Desktop
- Node.js 18+ (for Playwright)
- PostgreSQL 15+ (if running locally)
- Redis 7+ (if running locally)

### Installation

#### Option 1: Docker Setup (Recommended)

1. **Clone the repository**
   ```bash
   git clone https://github.com/techy-Nik/final-term.git
   cd final-term
   ```

2. **Start all services**
   ```bash
   docker-compose up --build
   ```

3. **Run database migrations**
   ```bash
   docker-compose exec web alembic upgrade head
   ```

4. **Access the application**
   - Main Dashboard: http://localhost:8000/dashboard.html
   - Login Page: http://localhost:8000/login.html
   - API Documentation: http://localhost:8000/docs
   - ReDoc: http://localhost:8000/redoc

#### Option 2: Local Development Setup

1. **Clone and setup virtual environment**
   ```bash
   git clone https://github.com/techy-Nik/final-term.git
   cd final-term
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   playwright install
   ```

3. **Setup environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your settings
   ```

4. **Start services (PostgreSQL and Redis)**
   ```bash
   docker-compose up postgres redis -d
   ```

5. **Run database migrations**
   ```bash
   alembic upgrade head
   ```

6. **Start the application**
   ```bash
   uvicorn app.main:app --reload
   ```

## 🧪 Running Tests

### Run All Tests with Coverage

```bash
# Install dependencies
pip install -r requirements.txt
playwright install

# Run all tests
pytest --cov=app --cov-report=html --cov-report=term-missing -v

# View coverage report
open htmlcov/index.html  # Mac
start htmlcov/index.html  # Windows
xdg-open htmlcov/index.html  # Linux
```

### Run Specific Test Suites

```bash
# Unit tests only
pytest tests/unit/ -v

# Integration tests only
pytest tests/integration/ -v

# E2E tests with Playwright
pytest tests/e2e/ -v

# Run E2E tests with visible browser
pytest tests/e2e/ -v --headed --slowmo=500

# Run specific test file
pytest tests/e2e/test_bread_flow.py -v
```

### Test Coverage Breakdown

- **Unit Tests**: Core logic, models, schemas, services
- **Integration Tests**: API endpoints, database operations
- **E2E Tests**: Complete user workflows from UI

**Target Coverage**: 95%+ overall

## 🎨 Frontend BREAD Operations

### Browse Calculations

**Features:**
- View all calculations in paginated table
- Sort by date, operation type, or result
- Filter by operation (addition, subtraction, etc.)
- Search by inputs or results
- Bulk delete operations

**Usage:**
```javascript
// Fetch and display calculations
async function loadCalculations() {
    const response = await fetch('/calculations', {
        headers: {
            'Authorization': `Bearer ${getToken()}`
        }
    });
    const calculations = await response.json();
    displayCalculations(calculations);
}
```

### Read Calculation Details

**Features:**
- Click any calculation to view details
- Modal popup with full information
- Show operation breakdown
- Display timestamps

### Edit Calculation

**Features:**
- Inline editing in table
- Click edit icon to modify
- Update operation type or inputs
- Real-time result recalculation
- Validation before saving

**Usage:**
```javascript
async function updateCalculation(id, data) {
    const response = await fetch(`/calculations/${id}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${getToken()}`
        },
        body: JSON.stringify(data)
    });
    return await response.json();
}
```

### Add New Calculation

**Features:**
- Form with operation selector
- Dynamic input fields based on operation
- Live result preview
- Client-side validation
- Success notification

**Supported Operations:**
- Addition (+)
- Subtraction (-)
- Multiplication (×)
- Division (÷)
- Exponentiation (^)
- Modulus (%)
- Square Root (√)
- Logarithm (log)

### Delete Calculation

**Features:**
- Delete button with confirmation dialog
- Bulk delete multiple calculations
- Undo option (soft delete)
- Success/error notifications


## 🗄️ Database Migrations with Alembic

### Running Migrations

```bash
# Create a new migration
alembic revision --autogenerate -m "Description of changes"

# Apply migrations
alembic upgrade head

# Rollback one migration
alembic downgrade -1

# View migration history
alembic history

# Check current version
alembic current
```

## 🎭 E2E Testing with Playwright

### Complete BREAD Flow Test

```python
# tests/e2e/test_bread_flow.py
async def test_complete_bread_flow(page):
    # Login
    await page.goto("http://localhost:8000/login.html")
    await page.fill("#email", "test@example.com")
    await page.fill("#password", "TestPass123")
    await page.click("#login-button")
    
    # Add calculation
    await page.goto("http://localhost:8000/dashboard.html")
    await page.click("#add-calc-button")
    await page.select_option("#operation", "addition")
    await page.fill("#input1", "10")
    await page.fill("#input2", "20")
    await page.click("#save-button")
    await expect(page.locator(".success-message")).to_be_visible()
    
    # Browse calculations
    calc_rows = page.locator(".calc-row")
    await expect(calc_rows).to_have_count_greater_than(0)
    
    # Edit calculation
    await page.click(".edit-button").first
    await page.fill("#edit-input1", "15")
    await page.click("#update-button")
    await expect(page.locator(".success-message")).to_be_visible()
    
    # Delete calculation
    await page.click(".delete-button").first
    await page.click("#confirm-delete")
    await expect(page.locator(".success-message")).to_be_visible()
```

## 🐳 Docker Hub Repository

**Docker Image**: [techynik/final-term](https://hub.docker.com/repository/docker/techynik/final-term/general)

### Pull and Run

```bash
# Pull latest image
docker pull techynik/final-term:latest

# Run with docker-compose
docker-compose up

# Or run standalone (requires external DB and Redis)
docker run -p 8000:8000 \
  -e DATABASE_URL=postgresql://user:pass@host/db \
  -e REDIS_URL=redis://host:6379 \
  techynik/final-term:latest
```

### Build and Push

```bash
# Build
docker build -t techynik/final-term:latest .

# Tag with version
docker tag techynik/final-term:latest techynik/final-term:v1.0.0

# Push to Docker Hub
docker push techynik/final-term:latest
docker push techynik/final-term:v1.0.0
```

## 🔧 CI/CD Pipeline

### GitHub Actions Workflow

Complete automated pipeline:

1. **Lint & Format**
   - Ruff for linting
   - Black for formatting
   - Type checking with mypy

2. **Test Stage**
   - Unit tests with coverage
   - Integration tests
   - E2E tests with Playwright
   

3. **Security Stage**
   - Trivy vulnerability scanning
   - Bandit security linting
   - Dependency audit

4. **Build Stage**
   - Docker image build
   - Multi-platform support (amd64, arm64)
   - Layer caching

5. **Deploy Stage** (main branch only)
   - Push to Docker Hub
   - Tag with version and commit SHA
   - Deployment summary

### Triggering CI/CD

```bash
# On push to main
git push origin main

# On pull request
git push origin feature-branch
# Then create PR on GitHub
```

## 💡 Usage Examples

### Complete User Flow

```python
import requests

BASE_URL = "http://localhost:8000"
token = None

# 1. Register
response = requests.post(f"{BASE_URL}/register", json={
    "username": "john_doe",
    "email": "john@example.com",
    "password": "SecurePass123"
})
token = response.json()["access_token"]

# 2. Create calculation (Add)
headers = {"Authorization": f"Bearer {token}"}
calc = requests.post(f"{BASE_URL}/calculations", 
    headers=headers,
    json={"type": "addition", "inputs": [10, 20, 30]}
).json()
print(f"Created calculation: {calc['id']}, result: {calc['result']}")

# 3. Browse all calculations
calcs = requests.get(f"{BASE_URL}/calculations", headers=headers).json()
print(f"Total calculations: {len(calcs)}")

# 4. Read specific calculation
calc_detail = requests.get(
    f"{BASE_URL}/calculations/{calc['id']}", 
    headers=headers
).json()

# 5. Edit calculation
updated = requests.put(
    f"{BASE_URL}/calculations/{calc['id']}", 
    headers=headers,
    json={"type": "multiplication", "inputs": [5, 10]}
).json()
print(f"Updated result: {updated['result']}")

# 6. Get statistics
stats = requests.get(f"{BASE_URL}/users/me/statistics", headers=headers).json()
print(f"Statistics: {stats}")

# 7. Export as CSV
csv_data = requests.get(
    f"{BASE_URL}/calculations/export/csv", 
    headers=headers
).text

# 8. Delete calculation
requests.delete(f"{BASE_URL}/calculations/{calc['id']}", headers=headers)
```

## 📦 Dependencies

### Core Dependencies
```txt
fastapi==0.115.8
uvicorn[standard]==0.34.0
sqlalchemy==2.0.38
alembic==1.14.0          # Database migrations
pydantic==2.10.6
pydantic-settings==2.7.1
python-jose[cryptography]==3.3.0
passlib[bcrypt]==1.7.4
redis==5.0.1
psycopg2-binary==2.9.10
```

### Testing Dependencies
```txt
pytest==8.3.4
pytest-asyncio==0.24.0
pytest-cov==6.0.0
pytest-playwright==0.6.2
playwright==1.50.0
httpx==0.28.1
faker==36.1.0
```

### Additional Dependencies
```txt
python-multipart==0.0.20  # File uploads
Jinja2==3.1.5            # Templates
aiofiles==24.1.0         # Async file operations
```

See `requirements.txt` for complete list.

## 🐛 Troubleshooting

### Database Migration Issues

```bash
# Reset database
docker-compose down -v
docker-compose up -d postgres

# Reinitialize Alembic
alembic stamp head
alembic upgrade head
```

### Frontend Not Loading

```bash
# Check static files are served
curl http://localhost:8000/static/js/dashboard.js

# Verify templates directory
ls -la templates/

# Check FastAPI static mount in main.py
```

### E2E Tests Timing Out

```bash
# Increase timeout in playwright.config.ts
# or
pytest tests/e2e/ -v --timeout=60000
```

### Token Expiration During Testing

```bash
# Increase token expiration in .env for testing
JWT_ACCESS_TOKEN_EXPIRE_MINUTES=60
```

## 📚 API Documentation

Full API documentation available at:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### Key Endpoints Summary

| Endpoint | Method | Description | Auth Required |
|----------|--------|-------------|---------------|
| `/register` | POST | Register new user | No |
| `/login` | POST | Login user | No |
| `/calculations` | GET | Browse calculations | Yes |
| `/calculations` | POST | Add calculation | Yes |
| `/calculations/{id}` | GET | Read calculation | Yes |
| `/calculations/{id}` | PUT | Edit calculation | Yes |
| `/calculations/{id}` | DELETE | Delete calculation | Yes |
| `/users/me` | GET | Get profile | Yes |
| `/users/me/statistics` | GET | Get statistics | Yes |


## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Nikunj** - [techy-Nik](https://github.com/techy-Nik)

- GitHub: [@techy-Nik](https://github.com/techy-Nik)
- Project Repository: [final-term](https://github.com/techy-Nik/final-term)
- Docker Hub: [techynik/final-term](https://hub.docker.com/repository/docker/techynik/final-term)

## 🙏 Acknowledgments

- FastAPI for excellent documentation and framework
- Playwright for reliable browser automation
- PostgreSQL for robust database functionality
- Redis for efficient caching and token management
- Docker for containerization excellence
- The entire Python and web development community

---

## 🎉 Final Project Submission

This represents the **complete final deliverable** for the course, demonstrating:
- ✅ Complete BREAD functionality with frontend implementation
- ✅ Advanced features (profiles, statistics, export)
- ✅ Database migrations with Alembic
- ✅ Comprehensive testing (unit, integration, E2E)
- ✅ Production-ready CI/CD pipeline
- ✅ Docker Hub deployment
- ✅ Full documentation

