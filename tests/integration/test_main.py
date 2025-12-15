# tests/integration/test_main.py
import pytest
from uuid import uuid4
from fastapi.testclient import TestClient
from app.main import app
from app.database import get_db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base

# -------------------------
# Setup test database
# -------------------------
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Override get_db dependency
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

# Create tables before tests
Base.metadata.create_all(bind=engine)

# -------------------------
# Helper functions
# -------------------------
def create_unique_user():
    unique_id = str(uuid4())
    payload = {
        "username": f"user_{unique_id}",
        "email": f"user_{unique_id}@example.com",
        "password": "Password123!",
        "confirm_password": "Password123!",
        "first_name": "Test",
        "last_name": "User"
    }
    response = client.post("/auth/register", json=payload)
    assert response.status_code == 201
    return payload

def login_user(payload):
    response = client.post("/auth/login", json={
        "username": payload["username"],
        "password": payload["password"]
    })
    assert response.status_code == 200
    return response.json()["access_token"]

# -------------------------
# Health endpoint
# -------------------------
def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

# -------------------------
# User Registration & Login
# -------------------------
def test_user_registration_and_login():
    payload = create_unique_user()
    token = login_user(payload)
    assert token is not None

# -------------------------
# Calculations CRUD
# -------------------------
@pytest.fixture
def auth_header():
    payload = create_unique_user()
    token = login_user(payload)
    return {"Authorization": f"Bearer {token}"}

def test_create_calculation(auth_header):
    payload = {
        "type": "addition",
        "inputs": [5, 10]
    }
    response = client.post("/calculations", json=payload, headers=auth_header)
    assert response.status_code == 201
    data = response.json()
    assert data["type"] == "addition"
    assert data["result"] == 15

def test_list_calculations(auth_header):
    # Ensure at least one calculation exists
    payload = {
        "type": "addition",
        "inputs": [1, 2]
    }
    client.post("/calculations", json=payload, headers=auth_header)
    response = client.get("/calculations", headers=auth_header)
    assert response.status_code == 200
    assert len(response.json()) >= 1

def test_get_calculation(auth_header):
    # Create a calculation
    payload = {"type": "multiplication", "inputs": [2, 3]}
    create_resp = client.post("/calculations", json=payload, headers=auth_header)
    calc_id = create_resp.json()["id"]

    # Retrieve the calculation
    response = client.get(f"/calculations/{calc_id}", headers=auth_header)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == calc_id
    assert data["result"] == 6

def test_update_calculation(auth_header):
    payload = {"type": "addition", "inputs": [1, 2]}
    create_resp = client.post("/calculations", json=payload, headers=auth_header)
    calc_id = create_resp.json()["id"]

    update_payload = {"inputs": [10, 20]}
    response = client.put(f"/calculations/{calc_id}", json=update_payload, headers=auth_header)
    assert response.status_code == 200
    data = response.json()
    assert data["result"] == 30

def test_delete_calculation(auth_header):
    payload = {"type": "addition", "inputs": [3, 4]}
    create_resp = client.post("/calculations", json=payload, headers=auth_header)
    calc_id = create_resp.json()["id"]

    response = client.delete(f"/calculations/{calc_id}", headers=auth_header)
    assert response.status_code == 204

    # Confirm deletion
    response = client.get(f"/calculations/{calc_id}", headers=auth_header)
    assert response.status_code == 404

# -------------------------
# Web pages (HTML) test
# -------------------------
@pytest.mark.parametrize("url", [
    "/", "/login", "/register", "/dashboard"
])
def test_web_pages(url):
    response = client.get(url)
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
