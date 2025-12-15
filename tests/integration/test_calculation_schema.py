import pytest
from pydantic import ValidationError
from uuid import uuid4
from datetime import datetime

from app.schemas.calculation import (
    CalculationCreate,
    CalculationUpdate,
    CalculationResponse
)

# -------------------- CREATE --------------------

def test_calculation_create_valid():
    data = {
        "type": "addition",
        "inputs": [10.5, 3.0],
        "user_id": uuid4()
    }
    calc = CalculationCreate(**data)
    assert calc.type == "addition"
    assert calc.inputs == [10.5, 3.0]
    assert calc.user_id is not None

def test_calculation_create_missing_type():
    data = {
        "inputs": [10.5, 3.0],
        "user_id": uuid4()
    }
    with pytest.raises(ValidationError) as exc_info:
        CalculationCreate(**data)
    assert "required" in str(exc_info.value).lower()

def test_calculation_create_missing_inputs():
    data = {
        "type": "multiplication",
        "user_id": uuid4()
    }
    with pytest.raises(ValidationError) as exc_info:
        CalculationCreate(**data)
    assert "required" in str(exc_info.value).lower()

def test_calculation_create_invalid_inputs():
    data = {
        "type": "division",
        "inputs": "not-a-list",
        "user_id": uuid4()
    }
    with pytest.raises(ValidationError) as exc_info:
        CalculationCreate(**data)
    assert "valid list" in str(exc_info.value).lower()

# ✅ FIXED: unsupported type is now REALLY unsupported
def test_calculation_create_unsupported_type():
    data = {
        "type": "random_math",  # ❌ truly unsupported
        "inputs": [25],
        "user_id": uuid4()
    }
    with pytest.raises(ValidationError) as exc_info:
        CalculationCreate(**data)

    error_message = str(exc_info.value).lower()
    assert "one of" in error_message or "not a valid" in error_message

# -------------------- UPDATE --------------------

def test_calculation_update_valid():
    data = {
        "inputs": [42.0, 7.0]
    }
    calc_update = CalculationUpdate(**data)
    assert calc_update.inputs == [42.0, 7.0]

def test_calculation_update_no_fields():
    calc_update = CalculationUpdate()
    assert calc_update.inputs is None

# -------------------- RESPONSE --------------------

def test_calculation_response_valid():
    data = {
        "id": uuid4(),
        "user_id": uuid4(),
        "type": "square_root",
        "inputs": [25],
        "result": 5.0,
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow(),
    }
    calc_response = CalculationResponse(**data)

    assert calc_response.id is not None
    assert calc_response.user_id is not None
    assert calc_response.type == "square_root"
    assert calc_response.inputs == [25]
    assert calc_response.result == 5.0
