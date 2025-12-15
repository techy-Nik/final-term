import uuid
import pytest

from app.models.calculation import (
    AbstractCalculation,
    Addition,
    Subtraction,
    Multiplication,
    Division,
    Exponentiation,
    Modulus,
    SquareRoot,
    Logarithm,
)

# -------------------------------------------------------------------
# Factory method coverage
# -------------------------------------------------------------------

def test_factory_unsupported_calculation_type():
    with pytest.raises(ValueError, match="Unsupported calculation type"):
        AbstractCalculation.create(
            calculation_type="invalid_type",
            user_id=uuid.uuid4(),
            inputs=[1, 2]
        )

# -------------------------------------------------------------------
# Addition
# -------------------------------------------------------------------

def test_addition_inputs_not_list():
    calc = Addition(user_id=uuid.uuid4(), inputs="not-a-list")
    with pytest.raises(ValueError):
        calc.get_result()

def test_addition_not_enough_inputs():
    calc = Addition(user_id=uuid.uuid4(), inputs=[1])
    with pytest.raises(ValueError):
        calc.get_result()

# -------------------------------------------------------------------
# Subtraction
# -------------------------------------------------------------------

def test_subtraction_inputs_not_list():
    calc = Subtraction(user_id=uuid.uuid4(), inputs="not-a-list")
    with pytest.raises(ValueError):
        calc.get_result()

def test_subtraction_not_enough_inputs():
    calc = Subtraction(user_id=uuid.uuid4(), inputs=[10])
    with pytest.raises(ValueError):
        calc.get_result()

# -------------------------------------------------------------------
# Multiplication
# -------------------------------------------------------------------

def test_multiplication_inputs_not_list():
    calc = Multiplication(user_id=uuid.uuid4(), inputs="not-a-list")
    with pytest.raises(ValueError):
        calc.get_result()

def test_multiplication_not_enough_inputs():
    calc = Multiplication(user_id=uuid.uuid4(), inputs=[2])
    with pytest.raises(ValueError):
        calc.get_result()

# -------------------------------------------------------------------
# Division
# -------------------------------------------------------------------

def test_division_inputs_not_list():
    calc = Division(user_id=uuid.uuid4(), inputs="not-a-list")
    with pytest.raises(ValueError):
        calc.get_result()

def test_division_not_enough_inputs():
    calc = Division(user_id=uuid.uuid4(), inputs=[10])
    with pytest.raises(ValueError):
        calc.get_result()

def test_division_by_zero():
    calc = Division(user_id=uuid.uuid4(), inputs=[10, 0])
    with pytest.raises(ValueError, match="divide by zero"):
        calc.get_result()

# -------------------------------------------------------------------
# Exponentiation
# -------------------------------------------------------------------

def test_exponentiation_inputs_not_list():
    calc = Exponentiation(user_id=uuid.uuid4(), inputs="not-a-list")
    with pytest.raises(ValueError):
        calc.get_result()

def test_exponentiation_not_enough_inputs():
    calc = Exponentiation(user_id=uuid.uuid4(), inputs=[2])
    with pytest.raises(ValueError):
        calc.get_result()

def test_exponentiation_overflow():
    calc = Exponentiation(
        user_id=uuid.uuid4(),
        inputs=[10.0, 10_000]
    )
    with pytest.raises(ValueError, match="overflow"):
        calc.get_result()

# -------------------------------------------------------------------
# Modulus
# -------------------------------------------------------------------

def test_modulus_inputs_not_list():
    calc = Modulus(user_id=uuid.uuid4(), inputs="not-a-list")
    with pytest.raises(ValueError):
        calc.get_result()

def test_modulus_not_enough_inputs():
    calc = Modulus(user_id=uuid.uuid4(), inputs=[10])
    with pytest.raises(ValueError):
        calc.get_result()

def test_modulus_by_zero():
    calc = Modulus(user_id=uuid.uuid4(), inputs=[10, 0])
    with pytest.raises(ValueError, match="modulus with zero"):
        calc.get_result()

# -------------------------------------------------------------------
# Square Root
# -------------------------------------------------------------------

def test_square_root_inputs_not_list():
    calc = SquareRoot(user_id=uuid.uuid4(), inputs="not-a-list")
    with pytest.raises(ValueError):
        calc.get_result()

def test_square_root_more_than_one_input():
    calc = SquareRoot(user_id=uuid.uuid4(), inputs=[4, 9])
    with pytest.raises(ValueError):
        calc.get_result()

def test_square_root_negative_number():
    calc = SquareRoot(user_id=uuid.uuid4(), inputs=[-4])
    with pytest.raises(ValueError, match="negative"):
        calc.get_result()

# -------------------------------------------------------------------
# Logarithm
# -------------------------------------------------------------------

def test_logarithm_inputs_not_list():
    calc = Logarithm(user_id=uuid.uuid4(), inputs="not-a-list")
    with pytest.raises(ValueError):
        calc.get_result()

def test_logarithm_wrong_number_of_inputs():
    calc = Logarithm(user_id=uuid.uuid4(), inputs=[10])
    with pytest.raises(ValueError):
        calc.get_result()

def test_logarithm_value_not_positive():
    calc = Logarithm(user_id=uuid.uuid4(), inputs=[-10, 10])
    with pytest.raises(ValueError):
        calc.get_result()

def test_logarithm_invalid_base():
    calc = Logarithm(user_id=uuid.uuid4(), inputs=[10, 1])
    with pytest.raises(ValueError, match="base must be positive"):
        calc.get_result()
