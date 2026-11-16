========
hambidge
========

the theorist of design whose Dynamic Symmetry uncovered root rectangles, whirling squares, and commensurable area proportions in Greek art and phyllotaxis

Edition Overview
----------------

- **Treatise**: *The Elements of Dynamic Symmetry*
- **Author**: Jay Hambidge
- **Primary Edition Track**: ``docsrc/dynamic_symmetry/`` (``:layout: book``)
- **Apparatus**: ``resources/persons.json``, ``resources/citations.json``, ``resources/glossary.json``
Installation & Verification
---------------------------

Managed with ``uv`` on Python 3.13:

.. code-block:: bash

   uv run --no-sync pytest
   ruff check src tests demos
   publish build

Usage
-----

.. code-block:: bash

   hambidge --help

Links
-----

- **Documentation**: https://geometor.github.io/hambidge
- **Repository**: https://github.com/geometor/hambidge
- **Issues**: https://github.com/geometor/hambidge/issues

License
-------

Licensed under the MIT License. See ``LICENSE`` for details.
