# This is our file to be tested with pytest
def add(a: float, b: float) -> float:
    """Return the sum of a and b."""
    return a + b

def sub(a: float, b: float) -> float:
    """Return the difference of a and b."""
    return a - b

def divide(a: float, b: float) -> float:
    """Return the quotient of a and b. Raises ValueError on division by zero."""
    return a / b

def multiply(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Inputs must be numeric")
    return a * b

def power(a: float, b: float) -> float:
    """Return a raised to the power of b."""
    return a ** b

def square(a: float) -> float:
    return a*a
