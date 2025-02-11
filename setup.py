"""
Setup script for `dafsa`
"""

# Import Python standard libraries
import pathlib
from setuptools import setup, find_packages

# The directory containing this file
LOCAL_PATH = pathlib.Path(__file__).parent

# The text of the README file
README_FILE = (LOCAL_PATH / "README.md").read_text(encoding="utf-8")

# Load requirements, so they are listed in a single place
with open("requirements.txt", encoding="utf-8") as fp:
    install_requires = [dep.strip() for dep in fp.readlines()]

# This call to setup() does all the work
setup(
    author="Tiago Tresoldi",
    author_email="tiago.tresoldi@lingfil.uu.se",
    classifiers=[
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Topic :: Text Processing :: Indexing",
        "Topic :: Text Processing :: Linguistic",
    ],
    description="Library for computing Deterministic Acyclic Finite State Automata (DAFSA)",
    entry_points={"console_scripts": ["dafsa=dafsa.__main__:main"]},
    extras_require={
        "dev": ["black", "flake8", "twine", "wheel"],
        "test": ["pytest"],
    },
    include_package_data=True,
    install_requires=install_requires,
    keywords=[
        "dafsa",
        "dawg",
        "finite state automata",
        "deterministic acyclic finite state automaton",
        "directed acyclic word graph",
    ],
    license="MIT",
    long_description=README_FILE,
    long_description_content_type="text/markdown",
    name="dafsa",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.6",
    project_urls={
        "Documentation": "https://dafsa.readthedocs.io",
    },
    test_suite="tests",
    tests_require=[],
    url="https://github.com/tresoldi/dafsa",
    version="2.0",  # remember to sync with __init__.py
    zip_safe=False,
)
