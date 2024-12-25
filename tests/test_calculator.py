import pytest
from src.calculator import multiply, divide

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-2, 3) == -6
    assert multiply(0, 5) == 0
    assert multiply(2.5, 2) == 5.0

def test_divide():
    assert divide(6, 2) == 3
    assert divide(-6, 2) == -3
    assert divide(0, 5) == 0
    assert divide(5, 2) == 2.5
    
    # Test division by zero
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(6, 0)