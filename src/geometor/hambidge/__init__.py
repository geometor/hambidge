"""Public package interface for ``geometor.hambidge``."""

from __future__ import annotations

from .app import main, run
from .model import (
    RootRectangle,
    WhirlingSquareRectangle,
    get_root_rectangles,
    verify_reciprocal_orthogonality,
)

__version__ = "0.1.0"

__all__ = [
    "RootRectangle",
    "WhirlingSquareRectangle",
    "__version__",
    "get_root_rectangles",
    "main",
    "run",
    "verify_reciprocal_orthogonality",
]
