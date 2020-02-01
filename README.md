# DAFSA

[![PyPI](https://img.shields.io/pypi/v/dafsa.svg)](https://pypi.org/project/dafsa)
[![Build Status](https://travis-ci.org/tresoldi/dafsa.svg?branch=master)](https://travis-ci.org/tresoldi/dafsa)
[![codecov](https://codecov.io/gh/tresoldi/dafsa/branch/master/graph/badge.svg)](https://codecov.io/gh/tresoldi/dafsa)
[![Codacy
Badge](https://api.codacy.com/project/badge/Grade/a2b47483ff684590b1208dbb4bbfc3ee)](https://www.codacy.com/manual/tresoldi/dafsa?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=tresoldi/dafsa&amp;utm_campaign=Badge_Grade)
[![Documentation
Status](https://readthedocs.org/projects/dafsa/badge/?version=latest)](https://dafsa.readthedocs.io/en/latest/?badge=latest)

DAFSA is a library for computing [Deterministic Acyclic Finite State Automata](https://en.wikipedia.org/wiki/Deterministic_acyclic_finite_state_automaton) (also known as "directed acyclic word graphs", or DAWG). DAFSA are data structures derived from [tries](https://en.wikipedia.org/wiki/Trie) that allow to represent a set of sequences (typically character strings or *n*-grams) in the form of a directed acyclic graph with a single source vertex (the `start` symbol of all sequences) and at least one sink edge (`final` symbols, each pointed to by one or more sequences). In the current implementation, a trait of each node expresses whether it can be used a sink.

The primary difference between DAFSA and tries is that the latter eliminates suffix and infix redundancy, as in the example of Figure 1 (from the linked Wikipedia article) storing the set of strings `"tap"`, `"taps"`, `"top"`, and `"tops"`. Even though DAFSAs cannot be used to store precise frequency information, given that multiple paths might reach the same terminal node, they still allow to estimate the sampling frequency; being acyclic, they can also reject any sequence not included in the training. Fuzzy extensions will allow to estimate the sampling probability of unobserved sequences.

![Trie vs. DAFSA](https://raw.githubusercontent.com/tresoldi/dafsa/master/figures/trie-vs-dafsa.png)

This data structure is a special case of a finite state recognizer that acts as a deterministic finite state automaton, as it recognizes all and only the sequences it was built upon. Frequently used in computer science for the space-efficient storage of sets of sequences without common compression techniques, such as dictionary or entropy types, or without probabilistic data structures, such as Bloom filters, the automata generated by this library are intended for linguistic exploration, and extend published models by allowing to approximate probability of random observation by carrying information on the weight of each graph edge.

## Installation and usage

The library can be installed as any standard Python library with
`pip`, and used as demonstrated in the following snippet:

In any standard Python environment, `dafsa` can be installed with:

```bash
$ pip install dafsa
```

Detailed instructions on how to use the library can be found in the
[official documentation](https://dafsa.readthedocs.io/en/latest/quickstart.html).
For most purposes, it is enough to pass a list of sequences to
the `DAFSA` object:

```python
>>> from dafsa import DAFSA
>>> print(DAFSA(["dib", "tip", "tips", "top"]))
DAFSA with 8 nodes and 9 edges (4 inserted sequences)
  +-- #0: 0(#1/4:<d>/1|#4/4:<t>/3) [('t', 4), ('d', 1)]
  +-- #1: n(#2/1:<i>/1) [('i', 2)]
  +-- #2: n(#3/1:<b>/1) [('b', 3)]
  +-- #3: F() []
  +-- #4: n(#5/3:<i>/2|#8/3:<o>/1) [('i', 5), ('o', 8)]
  +-- #5: n(#6/2:<p>/2) [('p', 6)]
  +-- #6: F(#3/2:<s>/1) [('s', 3)]
  +-- #8: n(#3/1:<p>/1) [('p', 3)]
```

Full documentation is available [at ReadTheDocs.io](https://dafsa.readthedocs.io).

## Showcase

* Basic example:

![First example](https://raw.githubusercontent.com/tresoldi/dafsa/master/figures/example.png)

* Output can be textual, GML, DOT, or (via dot and third-party software)
  PNG, PDF, ASCII-art and Unicode-art:

![DNA example](https://raw.githubusercontent.com/tresoldi/dafsa/master/figures/dna.png)

```
                                   G                                A
                               +---------------------+          +----------+
                               |                     v          |          v
      #====#  C   +---+  G   +---+  C   +---+  G   +---+  A   +---+  T   +---+  A   #===#
  +-- H 0  H ---> | 5 | ---> | 6 | ---> | 7 | ---> | 8 | ---> | 9 | ---> | 3 | ---> H 4 H
  |   #====#      +---+      +---+      +---+      +---+      +---+      +---+      #===#
  |     |    A                                                             ^
  | G   +-----------+                                                      |
  |                 v                                                      |
  |   +----+  G   +---+  A   +---+  T                                      |
  +-> | 20 | ---> | 1 | ---> | 2 | ----------------------------------------+
      +----+      +---+      +---+
```

```
                                   G                                A
                               ┌─────────────────────┐          ┌──────────┐
                               │                     ▼          │          ▼
      ╔════╗  C   ┌───┐  G   ┌───┐  C   ┌───┐  G   ┌───┐  A   ┌───┐  T   ┌───┐  A   ╔═══╗
  ┌── ║ 0  ║ ───▶ │ 5 │ ───▶ │ 6 │ ───▶ │ 7 │ ───▶ │ 8 │ ───▶ │ 9 │ ───▶ │ 3 │ ───▶ ║ 4 ║
  │   ╚════╝      └───┘      └───┘      └───┘      └───┘      └───┘      └───┘      ╚═══╝
  │     │    A                                                             ▲
  │ G   └───────────┐                                                      │
  │                 ▼                                                      │
  │   ┌────┐  G   ┌───┐  A   ┌───┐  T                                      │
  └─▶ │ 20 │ ───▶ │ 1 │ ───▶ │ 2 │ ────────────────────────────────────────┘
      └────┘      └───┘      └───┘
```

* With or without single-path joining:

![Phoneme example](https://raw.githubusercontent.com/tresoldi/dafsa/master/figures/phonemes.png)

![Reduced Phoneme example](https://raw.githubusercontent.com/tresoldi/dafsa/master/figures/reduced_phonemes.png)

## Changelog

Version 0.6:
  - Documentation improvements following JOSS review
  - Fixed bug where node finality was not considered in minimization

Version 0.5.1:
  - Minor changes in preparation for submission (including tagged release)

Version 0.5:
  - Improvements in speed, particularly in the `__eq__()` method of
    `DAFSANode` and the `_minimize()` method of `DAFSA`. The computation
    of a DAFSA for the contents of `/usr/share/dict/words` in the test
    machine (99,171 sequences) is now performed in under 8 minutes.
  - Added code from Daciuk's packages in an extra directory, along with
    notes on license

Version 0.4:
  - Full documentation for existing code
  - Added GML, PDF, and SVG export
  - Allow to access all options from command-line

Version 0.3:
  - Allow to join transitions in single sub-paths
  - Allows to export a DAFSA as a `networkx` graph
  - Preliminary documentation at [ReadTheDocs](https://dafsa.readthedocs.io)

Version 0.2.1:

  - Added support for segmented data

Version 0.2:

  - Added support for weighted edges and nodes
  - Added DOT export and Graphviz generation
  - Refined minimization method, which can be skipped if desired (resulting
    in a standard trie)
  - Added examples in the resources, also used for test data

Version 0.1:

  - First public release.

## Roadmap

Version 1.0:
  - Publish in journal


After 1.0:

  - Preliminary generation of minimal regular expressions matching the
    contents of a DAFSA
  - Consider adding support for empty transitions (or depend on the user
    aligning those)
  - Work on options for nicer graphviz output (colors, widths, etc.)

## Community guidelines

While the author can be contacted directly for support, it is recommended
that third parties use GitHub standard features, such as issues and
pull requests, to contribute, report problems, or seek support.

Contributing guidelines, including a code of conduct, can be found in
the CONTRIBUTING.md file.

## Author and citation

The library is developed by Tiago Tresoldi (tresoldi@shh.mpg.de).

The author has received funding from the European Research Council (ERC)
under the European Union’s Horizon 2020 research and innovation
programme (grant agreement
No. [ERC Grant #715618](https://cordis.europa.eu/project/rcn/206320/factsheet/en),
[Computer-Assisted Language Comparison](https://digling.org/calc/).

If you use `dafsa`, please cite it as:

> Tresoldi, Tiago (2019). DAFSA, a a library for computing Deterministic Acyclic Finite State Automata. Version 0.5.1. Jena. Available at: <https://github.com/tresoldi/dafsa>

In BibTeX:

```bibtex
@misc{Tresoldi2019dafsa,
  author = {Tresoldi, Tiago},
  title = {DAFSA, a a library for computing Deterministic Acyclic Finite State Automata. Version 0.5.1.},
  howpublished = {\url{https://github.com/tresoldi/dafsa}},
  address = {Jena},
  year = {2019},
}
```
