"""
Tests for the calculator module.
"""

import pytest
from src import Calculator


class TestCalculator:
    """Test cases for Calculator class."""

    def test_add(self):
        """Test addition operation."""
        assert Calculator.add(2, 3) == 5
        assert Calculator.add(-1, 1) == 0
        assert Calculator.add(0.5, 0.5) == 1.0

    def test_subtract(self):
        """Test subtraction operation."""
        assert Calculator.subtract(5, 3) == 2
        assert Calculator.subtract(1, -1) == 2
        assert Calculator.subtract(0.5, 0.3) == 0.2

    def test_multiply(self):
        """Test multiplication operation."""
        assert Calculator.multiply(3, 4) == 12
        assert Calculator.multiply(-2, 3) == -6
        assert Calculator.multiply(0.5, 4) == 2.0

    def test_divide(self):
        """Test division operation."""
        assert Calculator.divide(6, 2) == 3
        assert Calculator.divide(5, 2) == 2.5
        assert Calculator.divide(-6, 3) == -2

    def test_divide_by_zero(self):
        """Test division by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            Calculator.divide(5, 0)

    def test_power(self):
        """Test power operation."""
        assert Calculator.power(2, 3) == 8
        assert Calculator.power(5, 0) == 1
        assert Calculator.power(4, 0.5) == 2.0

    def test_sqrt(self):
        """Test square root operation."""
        assert Calculator.sqrt(4) == 2
        assert Calculator.sqrt(9) == 3
        assert Calculator.sqrt(0) == 0

    def test_sqrt_negative(self):
        """Test square root of negative number raises ValueError."""
        with pytest.raises(ValueError, match="Cannot calculate square root of negative number"):
            Calculator.sqrt(-1)
