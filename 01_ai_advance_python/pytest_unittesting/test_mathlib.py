""" 
Note: You have to add test_<fx_name> before every function name in order to test the function with pytest
    pytest command flags:
    - use -k flag followed by the function name.
    - use -v for verbose output and -q for quiet mode.
"""
import mathlib
import pytest

def test_add():
    assert mathlib.add(5, 5) == 10
    assert mathlib.add(1,10) == 11

def test_sub():
    assert mathlib.sub(5, 5) == 0

# testing all the multiply cases with different corner cases
def test_mult_int():
    assert mathlib.multiply(5, 5) == 25
    
def test_mult_float():
    assert mathlib.multiply(5.5, 4.5) == 24.3

def test_mult_negative():
    assert mathlib.multiply(-5, -5) == 25

def test_mult_float():
    assert mathlib.multiply(2.5, 4) == 10.0

def test_mult_non_numeric():
    with pytest.raises(TypeError):
        mathlib.multiply("5", 2)

def test_divide():
    assert mathlib.divide(5, 5) == 1
    with pytest.raises(ZeroDivisionError):
        mathlib.divide(5, 0)
    
def test_power():
    assert mathlib.power(2, 4) == 16




