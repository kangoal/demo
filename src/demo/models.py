"""
Pydantic models for API request/response handling.
"""

from typing import Union
from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    """Health check response model."""
    status: str = Field(..., description="Service status")
    version: str = Field(..., description="Package version")
    timestamp: str = Field(..., description="Current timestamp")


class CalculationRequest(BaseModel):
    """Calculation request model."""
    operation: str = Field(..., description="Mathematical operation to perform")
    a: Union[int, float] = Field(..., description="First operand")
    b: Union[int, float] = Field(None, description="Second operand (optional for some operations)")


class CalculationResponse(BaseModel):
    """Calculation response model."""
    operation: str = Field(..., description="Operation performed")
    operands: dict = Field(..., description="Input operands")
    result: Union[int, float] = Field(..., description="Calculation result")
    success: bool = Field(..., description="Whether the operation was successful")
    error: str = Field(None, description="Error message if operation failed")