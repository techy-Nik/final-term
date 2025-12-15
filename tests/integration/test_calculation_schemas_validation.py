import pytest
from uuid import uuid4
from datetime import datetime
from pydantic import ValidationError

from app.schemas.calculation import (
    CalculationBase,
    CalculationCreate,
    CalculationUpdate,
    CalculationResponse,
)

# -------------------------------------------------------------------
# CalculationBase – type validation
# -------------------------------------------------------------------

def test_invalid_type_not_string():
    with pytest.raises(ValidationError):
        CalculationBase(type=123, inputs=[1, 2])

def test_invalid_type_not_supported():
    with pytest.raises(ValidationError, match="Type must be one of"):
        CalculationBase(type="unsupported", inputs=[1, 2])

# -------------------------------------------------------------------
# CalculationBase – inputs must be list
# -------------------------------------------------------------------

def test_inputs_not_a_list():
    with pytest.raises(ValidationError, match="valid list"):
        CalculationBase(type="addition", inputs="not-a-list")

# -------------------------------------------------------------------
# Multi-input operations (< 2 inputs)
# -------------------------------------------------------------------

@pytest.mark.parametrize(
    "calc_type",
    [
        "addition",
        "subtraction",
        "multiplication",
        "division",
        "exponentiation",
        "modulus",
    ],
)
def test_multi_input_ops_require_two_inputs(calc_type):
    with pytest.raises(ValidationError, match="requires at least two"):
        CalculationBase(type=calc_type, inputs=[1])

# -------------------------------------------------------------------
# Single-input operation (square_root)
# -------------------------------------------------------------------

def test_square_root_requires_exactly_one_input():
    with pytest.raises(ValidationError, match="requires exactly one"):
        CalculationBase(type="square_root", inputs=[1, 2])

def test_square_root_negative_number():
    with pytest.raises(ValidationError, match="square root"):
        CalculationBase(type="square_root", inputs=[-4])

# -------------------------------------------------------------------
# Two-input operation (logarithm)
# -------------------------------------------------------------------

def test_logarithm_requires_two_inputs():
    with pytest.raises(ValidationError, match="requires exactly two"):
        CalculationBase(type="logarithm", inputs=[10])

def test_logarithm_value_not_positive():
    with pytest.raises(ValidationError, match="value must be positive"):
        CalculationBase(type="logarithm", inputs=[0, 10])

def test_logarithm_invalid_base():
    with pytest.raises(ValidationError, match="base must be positive"):
        CalculationBase(type="logarithm", inputs=[10, 1])

# -------------------------------------------------------------------
# Division & Modulus specific checks
# -------------------------------------------------------------------

def test_division_by_zero():
    with pytest.raises(ValidationError, match="divide by zero"):
        CalculationBase(type="division", inputs=[10, 0])

def test_modulus_by_zero():
    with pytest.raises(ValidationError, match="modulus with zero"):
        CalculationBase(type="modulus", inputs=[10, 0])

# -------------------------------------------------------------------
# Exponentiation – large exponent guard
# -------------------------------------------------------------------

def test_exponentiation_exponent_too_large():
    with pytest.raises(ValidationError, match="Exponent too large"):
        CalculationBase(type="exponentiation", inputs=[2, 5000])

# -------------------------------------------------------------------
# CalculationUpdate validation
# -------------------------------------------------------------------

def test_calculation_update_empty_inputs_list():
    with pytest.raises(ValidationError, match="at least 1 item"):
        CalculationUpdate(inputs=[])


def test_calculation_update_valid():
    update = CalculationUpdate(inputs=[42])
    assert update.inputs == [42]

# -------------------------------------------------------------------
# CalculationCreate & CalculationResponse happy paths
# (covers remaining config + from_attributes lines)
# -------------------------------------------------------------------

def test_calculation_create_valid():
    data = {
        "type": "addition",
        "inputs": [1, 2],
        "user_id": uuid4(),
    }
    calc = CalculationCreate(**data)
    assert calc.type.value == "addition"

def test_calculation_response_valid():
    data = {
        "id": uuid4(),
        "user_id": uuid4(),
        "type": "subtraction",
        "inputs": [10, 5],
        "result": 5.0,
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow(),
    }
    resp = CalculationResponse(**data)
    assert resp.result == 5.0
