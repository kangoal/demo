"""
Command-line interface for the demo service.
"""

import argparse
import sys

from demo.server import run_server


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(description="Demo PyPI Service CLI")
    parser.add_argument(
        "--host",
        default="0.0.0.0",
        help="Host to bind the server to (default: 0.0.0.0)"
    )
    parser.add_argument(
        "--port",
        type=int,
        default=8000,
        help="Port to bind the server to (default: 8000)"
    )
    parser.add_argument(
        "--reload",
        action="store_true",
        help="Enable auto-reload for development"
    )

    args = parser.parse_args()

    try:
        run_server(host=args.host, port=args.port, reload=args.reload)
    except KeyboardInterrupt:
        print("\nShutting down...")
        sys.exit(0)


if __name__ == "__main__":
    main()
