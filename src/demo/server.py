"""
FastAPI HTTP server implementation.
"""

import time
from typing import Any, Dict
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from demo import __version__
from demo.calculator import Calculator
from demo.models import HealthResponse, CalculationResponse, CalculationRequest


def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""
    app = FastAPI(
        title="Demo PyPI Service",
        description="A demo PyPI package with HTTP service capabilities",
        version=__version__,
    )

    # Add CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app


app = create_app()


@app.get("/", response_model=Dict[str, Any])
async def root():
    """Root endpoint providing basic service information."""
    return {
        "message": "Welcome to Demo PyPI Service",
        "version": __version__,
        "docs": "/docs",
        "health": "/health"
    }


@app.get("/health", response_model=HealthResponse)
async def health_check():
    """Health check endpoint."""
    return HealthResponse(
        status="healthy",
        version=__version__,
        timestamp=str(int(time.time()))
    )


@app.post("/calculate", response_model=CalculationResponse)
async def calculate(request: CalculationRequest):
    """Perform a mathematical calculation."""
    try:
        calculator = Calculator()
        operation = request.operation.lower()

        if operation == "add":
            result = calculator.add(request.a, request.b)
        elif operation == "subtract":
            result = calculator.subtract(request.a, request.b)
        elif operation == "multiply":
            result = calculator.multiply(request.a, request.b)
        elif operation == "divide":
            result = calculator.divide(request.a, request.b)
        elif operation == "power":
            result = calculator.power(request.a, request.b)
        elif operation == "sqrt":
            result = calculator.sqrt(request.a)
        else:
            raise HTTPException(
                status_code=400,
                detail=f"Unsupported operation: {request.operation}"
            )

        operands = {"a": request.a}
        if request.b is not None:
            operands["b"] = request.b

        return CalculationResponse(
            operation=operation,
            operands=operands,
            result=result,
            success=True,
            error=""
        )

    except ValueError as e:
        return CalculationResponse(
            operation=request.operation,
            operands={"a": request.a, "b": request.b},
            result=None,
            success=False,
            error=str(e)
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/operations")
async def list_operations():
    """List available mathematical operations."""
    return {
        "operations": [
            {
                "name": "add",
                "description": "Add two numbers",
                "parameters": ["a", "b"],
                "example": {"operation": "add", "a": 5, "b": 3}
            },
            {
                "name": "subtract",
                "description": "Subtract b from a",
                "parameters": ["a", "b"],
                "example": {"operation": "subtract", "a": 10, "b": 4}
            },
            {
                "name": "multiply",
                "description": "Multiply two numbers",
                "parameters": ["a", "b"],
                "example": {"operation": "multiply", "a": 6, "b": 7}
            },
            {
                "name": "divide",
                "description": "Divide a by b",
                "parameters": ["a", "b"],
                "example": {"operation": "divide", "a": 15, "b": 3}
            },
            {
                "name": "power",
                "description": "Calculate a raised to the power of b",
                "parameters": ["a", "b"],
                "example": {"operation": "power", "a": 2, "b": 3}
            },
            {
                "name": "sqrt",
                "description": "Calculate the square root of a",
                "parameters": ["a"],
                "example": {"operation": "sqrt", "a": 16}
            }
        ]
    }


def run_server(host: str = "0.0.0.0", port: int = 8000, reload: bool = False):
    """Run the FastAPI server."""
    import uvicorn
    uvicorn.run(
        "demo.server:app",
        host=host,
        port=port,
        reload=reload
    )


if __name__ == "__main__":
    run_server()
