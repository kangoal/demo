"""
Calculator module providing basic mathematical operations.
"""

from typing import Union


class Calculator:
    """A simple calculator class for basic mathematical operations."""
    
    @staticmethod
    def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Add two numbers."""
        return a + b
    
    @staticmethod
    def subtract(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Subtract b from a."""
        return a - b
    
    @staticmethod
    def multiply(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Multiply two numbers."""
        return a * b
    
    @staticmethod
    def divide(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Divide a by b."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    @staticmethod
    def power(base: Union[int, float], exponent: Union[int, float]) -> Union[int, float]:
        """Calculate base raised to the power of exponent."""
        return base ** exponent
    
    @staticmethod
    def sqrt(number: Union[int, float]) -> Union[int, float]:
        """Calculate the square root of a number."""
        if number < 0:
            raise ValueError("Cannot calculate square root of negative number")
        return number ** 0.5