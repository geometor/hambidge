"""Comprehensive test suite for ``geometor.hambidge``."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import xml.etree.ElementTree as ET

import pytest

from geometor.hambidge import (
    RootRectangle,
    WhirlingSquareRectangle,
    __version__,
    get_root_rectangles,
    run,
    verify_reciprocal_orthogonality,
)

REPO_ROOT = Path(__file__).resolve().parents[1]
RESOURCES_DIR = REPO_ROOT / "resources"
FIGURES_DIR = REPO_ROOT / "docsrc" / "_static" / "figures"


def test_version_and_cli() -> None:
    """Verify initial semantic version and clean zero-argument CLI execution."""
    assert __version__ == "0.1.0"
    assert run([]) == 0


def test_cli_help_exits_cleanly() -> None:
    """Verify ``--help`` exits cleanly with code ``0``."""
    with pytest.raises(SystemExit) as exc_info:
        run(["--help"])
    assert exc_info.value.code == 0


def test_root_rectangles_exact_symbolic_properties() -> None:
    """Verify exact Euclidean and Rational Trigonometry properties for root rectangles 1..5."""
    rects = get_root_rectangles(5)
    assert len(rects) == 5

    for rect in rects:
        n = rect.n
        assert rect.quadrance_end == 1
        assert rect.quadrance_side == n
        assert rect.quadrance_diagonal == 1 + n
        assert rect.reciprocal_count == n
        assert rect.diagonal_dot_product == 0
        assert rect.diagonal_spread == 1
        assert verify_reciprocal_orthogonality(n) is True

    # Check root-5 specific properties
    r5 = rects[4]
    assert r5.n == 5
    assert r5.quadrance_side == 5
    assert r5.quadrance_diagonal == 6
    assert r5.aspect_ratio_str == "1 : √5"


def test_whirling_squares_harmonic_identities() -> None:
    """Verify Whirling Square Golden Rectangle identities."""
    identities = WhirlingSquareRectangle.harmonic_identities()
    assert "root_five_flanked" in identities
    assert "root_five_sum" in identities
    assert "whirling_overlap" in identities
    assert WhirlingSquareRectangle.diagonal_spread() == 1


def test_sources_manifest_sha256_and_attestation() -> None:
    """Verify SHA-256 digests and 100% public-domain attestation for Hambidge sources."""
    manifest_path = RESOURCES_DIR / "sources_manifest.json"
    assert manifest_path.is_file()

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    work = manifest["work"]
    assert work["primary_author"] == "Jay Hambidge"
    assert "Public Domain" in work["copyright_attestation"]

    sources = manifest["sources"]
    assert len(sources) == 2
    for item in sources:
        fpath = REPO_ROOT / item["filename"]
        assert fpath.is_file(), f"Missing source file: {fpath}"
        content = fpath.read_bytes()
        digest = hashlib.sha256(content).hexdigest()
        assert digest == item["sha256"], f"SHA-256 mismatch for {item['id']}"


def test_apparatus_json_validity() -> None:
    """Verify persons.json, citations.json, and glossary.json are valid JSON with expected entries."""
    persons = json.loads((RESOURCES_DIR / "persons.json").read_text(encoding="utf-8"))
    assert "hambidge" in persons
    assert "church" in persons
    assert "euclid" in persons

    citations = json.loads((RESOURCES_DIR / "citations.json").read_text(encoding="utf-8"))
    assert "hambidge:1920-diagonal" in citations
    assert "hambidge:1920-vase" in citations
    assert "church:1904" in citations
    assert "euclid:elements" in citations

    glossary = json.loads((RESOURCES_DIR / "glossary.json").read_text(encoding="utf-8"))
    assert "dynamic-symmetry" in glossary
    assert "commensurable-in-square" in glossary
    assert "root-rectangle" in glossary
    assert "whirling-square-rectangle" in glossary


def test_svg_figures_euclid_graphic_contract() -> None:
    """Verify SVG figures parse as XML, have .euclid-graphic class and dark-mode styles."""
    for svg_name in ("fig_hambidge_root_rectangles.svg", "fig_golden_gnomon_spiral.svg"):
        svg_path = FIGURES_DIR / svg_name
        assert svg_path.is_file(), f"Missing SVG figure: {svg_path}"
        raw_svg = svg_path.read_text(encoding="utf-8")
        root = ET.fromstring(raw_svg)
        assert "euclid-graphic" in root.attrib.get("class", "")
        assert "prefers-color-scheme: dark" in raw_svg
