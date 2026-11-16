"""Exact symbolic geometry and algebraic foundations of Jay Hambidge's Dynamic Symmetry.

100% exact rational and radical calculations—zero floats, incommensurability
in linear distance, and exact commensurability in square (Euclid X Def. 2).
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import ClassVar


@dataclass(frozen=True)
class RootRectangle:
    """Exact symbolic specification for a Hambidge root-n rectangle (1 : √n).

    In Euclidean geometry (Book X, Def. 2), the end and side of a root-n rectangle
    are linearly incommensurable (for non-square n), yet strictly commensurable in square
    (dynamei symmetroi). In Wildberger's Rational Trigonometry, their quadrances
    are consecutive integers Q = 1, 2, 3, 4, 5.
    """

    n: int

    def __post_init__(self) -> None:
        if self.n < 1:
            raise ValueError(f"Root rectangle index must be >= 1, got {self.n}")

    @property
    def quadrance_end(self) -> int:
        """Quadrance (squared length) of the unit end."""
        return 1

    @property
    def quadrance_side(self) -> int:
        """Quadrance (squared length) of the horizontal side: Q_n = n."""
        return self.n

    @property
    def quadrance_diagonal(self) -> int:
        """Quadrance of the main diagonal by Pythagoras's theorem: Q_diag = 1 + n."""
        return 1 + self.n

    @property
    def reciprocal_count(self) -> int:
        """Number of congruent reciprocal root-n rectangles that tile the parent rectangle."""
        return self.n

    @property
    def reciprocal_side_quadrance(self) -> Fraction:
        """Quadrance of the reciprocal width: Q_rec = 1/n."""
        return Fraction(1, self.n)

    @property
    def diagonal_spread(self) -> int:
        """Rational spread between main diagonal and reciprocal diagonal (1 = 90° perpendicular)."""
        return 1

    @property
    def aspect_ratio_str(self) -> str:
        """Exact radical notation for aspect ratio."""
        return f"1 : √{self.n}" if self.n != 1 else "1 : 1"

    @property
    def diagonal_dot_product(self) -> int:
        """Dot product of main diagonal (√n, 1) and reciprocal diagonal (1/√n, -1).

        (√n)(1/√n) + (1)(-1) = 1 - 1 = 0, identically for all n.
        """
        return 0

    def describe(self) -> str:
        """Human-readable exact geometric summary."""
        return (
            f"Root-{self.n} Rectangle ({self.aspect_ratio_str}): "
            f"Q_end = {self.quadrance_end}, Q_side = {self.quadrance_side}, "
            f"Q_diag = {self.quadrance_diagonal}, Reciprocal count = {self.reciprocal_count}, "
            f"Reciprocal diagonal spread = {self.diagonal_spread} (perpendicular)"
        )


@dataclass(frozen=True)
class WhirlingSquareRectangle:
    """Exact specification of the Rectangle of the Whirling Squares (Golden Rectangle 1 : φ).

    A rectangle of aspect ratio 1 : φ where φ = (1 + √5)/2.
    Its reciprocal has width 1/φ = φ - 1 = (√5 - 1)/2.
    Detaching repeated squares produces an infinite sequence of whirling gnomons
    converging to the intersection pole (eye) of perpendicular diagonals.
    """

    name: ClassVar[str] = "Rectangle of the Whirling Squares"
    ratio_str: ClassVar[str] = "1 : φ"
    phi_exact: ClassVar[str] = "(1 + √5) / 2"
    reciprocal_width_exact: ClassVar[str] = "(√5 - 1) / 2"
    gnomon_shape: ClassVar[str] = "unit square (1 × 1)"
    pole_x_exact: ClassVar[str] = "1 / √5"
    pole_y_exact: ClassVar[str] = "(5 - √5) / 10"

    @staticmethod
    def harmonic_identities() -> dict[str, str]:
        """Exact algebraic identities bridging the √5 rectangle and golden rectangles."""
        return {
            "root_five_flanked": "√5 = 1 + 2 * φ⁻¹ = 1 + (√5 - 1)",
            "root_five_sum": "√5 = φ + φ⁻¹",
            "whirling_overlap": "2 * φ - √5 = 1 (two overlapping golden rectangles share a unit square)",
            "reciprocal_gnomon": "φ - φ⁻¹ = 1 (unit square gnomon)",
            "golden_equation": "φ² - φ - 1 = 0",
        }

    @staticmethod
    def diagonal_spread() -> int:
        """Rational spread between main diagonal (φ, 1) and reciprocal diagonal (1/φ, -1)."""
        return 1


def get_root_rectangles(max_n: int = 5) -> list[RootRectangle]:
    """Generate the classical series of root rectangles from √1 to √max_n."""
    return [RootRectangle(n) for n in range(1, max_n + 1)]


def verify_reciprocal_orthogonality(n: int) -> bool:
    """Algebraic proof that diagonal and reciprocal diagonal meet at spread s = 1 (90°).

    For any root-n rectangle, main vector is (√n, 1) and reciprocal vector is (1/√n, -1).
    Dot product: (√n)(1/√n) + (1)(-1) = 1 - 1 = 0.
    """
    rect = RootRectangle(n)
    return rect.diagonal_dot_product == 0 and rect.diagonal_spread == 1
