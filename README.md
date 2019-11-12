# dafsa


[![Build Status](https://travis-ci.org/tresoldi/dafsa.svg?branch=master)](https://travis-ci.org/tresoldi/dafsa)
[![codecov](https://codecov.io/gh/tresoldi/dafsa/branch/master/graph/badge.svg)](https://codecov.io/gh/tresoldi/dafsa)
[![PyPI](https://img.shields.io/pypi/v/dafsa.svg)](https://pypi.org/project/dafsa)

DAFSA is a library for computing [Deterministic Acyclic Finite State Automata](https://en.wikipedia.org/wiki/Deterministic_acyclic_finite_state_automaton), sometimes called "directed acyclic word graphs" (DAWG). DAFSA are data structures derived from [tries](https://en.wikipedia.org/wiki/Trie) that allow to represent a set of sequences (typically character strings or *n*-grams) in the form of a directed acyclic graph with a single source vertex (the `start` symbol of all sequences) and at least one sink edge (`end` symbols, potentially shared by one or more sequences). It is a special case of a finite state recognizer that acts as a deterministic finite state automaton, as it recognizes all and only the sequences it was built upon. Mostly used in computer science for the space-efficient storage of sets of sequences without common compression techniques, such as dictionary or entropy types, or without probabilistic data structures, such as Bloom filters, the automata generated by this library are intended for linguistic exploration, and extend published models by allowing to approximate probability of random observation by carrying information on the weight of each graph edge.

![Trie vs. DAFSA](https://raw.githubusercontent.com/tresoldi/dafsa/master/doc/trie-vs-dafsa.png){width=100%;float=right}

The primary difference between DAFSA and tries is that suffix and infix redundancy is eliminated, as in the example of figure 1 storing the set of strings `"tap"`, `"taps"`, and `"tops"`. Even though DAFSAs cannot be used to store precise frequency information, given that terminal nodes can be reached by multiple paths, they allow to estimate the sampling frequency; being acyclic, they can also reject any sequence not included in the training. Fuzzy extensions will allow to estimate the sampling probability of unobserved sequences.

## Changelog

Version 0.1:

  - First public release.

## Installation

In any standard Python environment, `dafsa` can be installed with:

```
pip install dafsa
```

## How to use

(...)

## Alternatives

(...)

## TODO

(...)

## How to cite

If you use `dafsa`, please cite it as:

> Tresoldi, Tiago (2019). DAFSA, a a library for computing Deterministic Acyclic Finite State Automata.
Version 0.1. Jena. Available at: https://github.com/tresoldi/dafsa

In BibTeX:

```
@misc{Tresoldi2019dafsa,
  author = {Tresoldi, Tiago},
  title = {DAFSA, a a library for computing Deterministic Acyclic Finite State Automata. Version 0.1},
  howpublished = {\url{https://github.com/tresoldi/dafsa}},
  address = {Jena},
  year = {2019},
}
```

## References

(...)

## Author

Tiago Tresoldi (tresoldi@shh.mpg.de)

The author was supported during development by the
[ERC Grant #715618](https://cordis.europa.eu/project/rcn/206320/factsheet/en)
for the project [CALC](http://calc.digling.org)
(Computer-Assisted Language Comparison: Reconciling Computational and Classical
Approaches in Historical Linguistics), led by
[Johann-Mattis List](http://www.lingulist.de).
