import pytest
import uuid
import math

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

def dummy_user_id():
    return uuid.uuid4()

# -------------------- BASIC OPERATIONS --------------------

def test_addition_get_result():
    calc = Addition(user_id=dummy_user_id(), inputs=[10, 5, 3.5])
    assert calc.get_result() == 18.5

def test_subtraction_get_result():
    calc = Subtraction(user_id=dummy_user_id(), inputs=[20, 5, 3])
    assert calc.get_result() == 12

def test_multiplication_get_result():
    calc = Multiplication(user_id=dummy_user_id(), inputs=[2, 3, 4])
    assert calc.get_result() == 24

def test_division_get_result():
    calc = Division(user_id=dummy_user_id(), inputs=[100, 2, 5])
    assert calc.get_result() == 10

def test_division_by_zero():
    calc = Division(user_id=dummy_user_id(), inputs=[10, 0])
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.get_result()

# -------------------- NEW OPERATIONS --------------------

def test_exponentiation():
    calc = Exponentiation(user_id=dummy_user_id(), inputs=[2, 3])
    assert calc.get_result() == 8

def test_exponentiation_chain():
    calc = Exponentiation(user_id=dummy_user_id(), inputs=[2, 3, 2])
    assert calc.get_result() == 64

def test_modulus():
    calc = Modulus(user_id=dummy_user_id(), inputs=[10, 3])
    assert calc.get_result() == 1

def test_modulus_by_zero():
    calc = Modulus(user_id=dummy_user_id(), inputs=[10, 0])
    with pytest.raises(ValueError, match="modulus with zero"):
        calc.get_result()

def test_square_root():
    calc = SquareRoot(user_id=dummy_user_id(), inputs=[25])
    assert calc.get_result() == 5

def test_square_root_negative():
    calc = SquareRoot(user_id=dummy_user_id(), inputs=[-4])
    with pytest.raises(ValueError, match="negative"):
        calc.get_result()

def test_logarithm_base_10():
    calc = Logarithm(user_id=dummy_user_id(), inputs=[100, 10])
    assert calc.get_result() == 2

def test_logarithm_base_2():
    calc = Logarithm(user_id=dummy_user_id(), inputs=[8, 2])
    assert calc.get_result() == 3

def test_logarithm_invalid_base():
    calc = Logarithm(user_id=dummy_user_id(), inputs=[10, 1])
    with pytest.raises(ValueError, match="base"):
        calc.get_result()

# -------------------- FACTORY TESTS --------------------

@pytest.mark.parametrize(
    "calc_type, inputs, expected_class",
    [
        ("addition", [1, 2], Addition),
        ("subtraction", [5, 2], Subtraction),
        ("multiplication", [3, 4], Multiplication),
        ("division", [10, 2], Division),
        ("exponentiation", [2, 3], Exponentiation),
        ("modulus", [10, 3], Modulus),
        ("square_root", [16], SquareRoot),
        ("logarithm", [100, 10], Logarithm),
    ]
)
def test_calculation_factory(calc_type, inputs, expected_class):
    calc = Calculation.create(
        calculation_type=calc_type,
        user_id=dummy_user_id(),
        inputs=inputs,
    )
    assert isinstance(calc, expected_class)

def test_calculation_factory_invalid_type():
    with pytest.raises(ValueError, match="Unsupported calculation type"):
        Calculation.create(
            calculation_type="random_math",
            user_id=dummy_user_id(),
            inputs=[1, 2],
        )

# -------------------- INPUT VALIDATION --------------------

def test_inputs_not_list():
    calc = Addition(user_id=dummy_user_id(), inputs="not-a-list")
    with pytest.raises(ValueError):
        calc.get_result()

def test_insufficient_inputs():
    calc = Multiplication(user_id=dummy_user_id(), inputs=[5])
    with pytest.raises(ValueError):
        calc.get_result()
