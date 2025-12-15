import pytest
import uuid

from app.models.calculation import (
    Calculation,
    Addition,
    Subtraction,
    Multiplication,
    Division,
    Exponentiation,
    Modulus,
    SquareRoot,
    Logarithm,
)

def uid():
    return uuid.uuid4()

# -------------------- ABSTRACT --------------------

def test_abstract_get_result_not_implemented():
    calc = Calculation(user_id=uid(), inputs=[1, 2])
    with pytest.raises(NotImplementedError):
        calc.get_result()

# -------------------- INPUT TYPE ERRORS --------------------

@pytest.mark.parametrize(
    "cls",
    [Addition, Subtraction, Multiplication, Division, Exponentiation, Modulus]
)
def test_inputs_not_list(cls):
    calc = cls(user_id=uid(), inputs="not-a-list")
    with pytest.raises(ValueError, match="list of numbers"):
        calc.get_result()

# -------------------- LENGTH VALIDATION --------------------

def test_subtraction_single_value():
    calc = Subtraction(user_id=uid(), inputs=[10])
    with pytest.raises(ValueError):
        calc.get_result()

def test_division_single_value():
    calc = Division(user_id=uid(), inputs=[10])
    with pytest.raises(ValueError):
        calc.get_result()

def test_exponentiation_single_value():
    calc = Exponentiation(user_id=uid(), inputs=[2])
    with pytest.raises(ValueError):
        calc.get_result()

def test_square_root_multiple_inputs():
    calc = SquareRoot(user_id=uid(), inputs=[4, 9])
    with pytest.raises(ValueError, match="exactly one"):
        calc.get_result()

# -------------------- MATH EDGE CASES --------------------

def test_modulus_not_list():
    calc = Modulus(user_id=uid(), inputs="bad")
    with pytest.raises(ValueError):
        calc.get_result()

def test_division_zero_middle():
    calc = Division(user_id=uid(), inputs=[10, 2, 0])
    with pytest.raises(ValueError, match="divide by zero"):
        calc.get_result()

def test_modulus_zero_middle():
    calc = Modulus(user_id=uid(), inputs=[10, 5, 0])
    with pytest.raises(ValueError, match="modulus"):
        calc.get_result()

def test_square_root_negative():
    calc = SquareRoot(user_id=uid(), inputs=[-9])
    with pytest.raises(ValueError, match="negative"):
        calc.get_result()

# -------------------- LOGARITHM ERRORS --------------------

def test_logarithm_wrong_input_length():
    calc = Logarithm(user_id=uid(), inputs=[10])
    with pytest.raises(ValueError, match="exactly two"):
        calc.get_result()

def test_logarithm_value_not_positive():
    calc = Logarithm(user_id=uid(), inputs=[-10, 2])
    with pytest.raises(ValueError, match="value must be positive"):
        calc.get_result()

def test_logarithm_invalid_base_zero():
    calc = Logarithm(user_id=uid(), inputs=[10, 0])
    with pytest.raises(ValueError, match="base"):
        calc.get_result()

def test_logarithm_invalid_base_one():
    calc = Logarithm(user_id=uid(), inputs=[10, 1])
    with pytest.raises(ValueError, match="base"):
        calc.get_result()

# -------------------- FACTORY ERROR --------------------

def test_factory_invalid_type():
    with pytest.raises(ValueError, match="Unsupported calculation type"):
        Calculation.create(
            calculation_type="not_supported",
            user_id=uid(),
            inputs=[1, 2]
        )
