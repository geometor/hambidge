:navigation: header
:order: 10

=====
About
=====

.. rubric:: Extracting Historical Semantic Knowledge & Repurposing It for Exact Symbolic Reasoning

About This Edition
------------------

the theorist of design whose Dynamic Symmetry uncovered root rectangles, whirling squares, and commensurable area proportions in Greek art and phyllotaxis

Primary Digital Scriptorium codex for *The Elements of Dynamic Symmetry* (Jay Hambidge), structured under :ref:`dynamic_symmetry-index` with prosopographical and bibliographic apparatus in :ref:`persons` and :ref:`bibliography`.


The GEOMETOR Mission
--------------------

The GEOMETOR project, directed by **phi ARCHITECT**, is dedicated to the systematic recovery, exact formalization, and dynamic re-expression of foundational geometric and philosophical knowledge:

- **Extracting Historical Semantic Knowledge**: Recovering the deductive structure of classical geometric, axiomatic, and philosophical treatises—elevating verbatim primary prose, primary-source folio scans (``publish folio``), and calibrated ``.euclid-graphic`` diagrams into addressable semantic graphs.
- **Exact Symbolic Grounding (``geometor.model``)**: Anchoring geometric constructions in 100% exact symbolic algebra (``SymPy``) and Rational Trigonometry invariants over closed-form radical fields.
- **Repurposing Knowledge Across Mediums**: Deploying extracted structures across multi-track **Book Codices**, EPUB 3 editions, computable canons, interactive SVG laboratories, and visual broadcasts.

Sources, Provenance & Repository Architecture
---------------------------------------------

- **Python Package**: ``src/geometor/hambidge/`` (Python 3.13)
- **Codex Edition Track**: ``docsrc/dynamic_symmetry/`` (``:layout: book``)
- **Edition Structure Map**: ``resources/dynamic_symmetry/structure_map.json``
- **Archival PDFs & Folios**: ``resources/dynamic_symmetry/pdfs/`` (parsed via ``publish folio-ingest``)
- **Scholarly Apparatus**: ``resources/persons.json``, ``resources/citations.json``, ``resources/glossary.json``
- **Automated Verification**: ``tests/`` (``pytest`` + ``ruff``) and ``docsrc/`` (``publish build``)
