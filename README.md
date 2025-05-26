# Development tools for MicroPython

This repository provides tools to assist with MicroPython development.


## Setup

Create a `Makefile` with the following minimal contents:

```
SRC_COMMON = ...

SRC_CHECKED = $(SRC_COMMON) ...
SRC_COMPILED = $(SRC_COMMON) ...
SRC_EXTRA = ...

include Makefile.in
```

where `...` above should be replaced with the names of your MicroPython
source files.


## Dependencies

All external tools have a variable with prefix `TOOL` in its name,
e.g. `TOOL_MYPY`, which can be overridden if necessary.

In additon to standard Python development tools, two special MicroPython
tools are used: 
[`mpy-cross`](https://github.com/micropython/micropython/tree/master/mpy-cross) 
for compiling, and 
[`pyboard.py`](https://github.com/micropython/micropython/blob/master/tools/pyboard.py)
for uploading.
These are part of the MicroPython source code and should be obtained from
there.


### MyPy stubs for MicroPython

MyPy stubs are provided for a small selection of the most common
MicroPython-specific libraries.
These `.pyi` files need to be copied to your directory for MyPy to use them.

An example `pyproject.toml` for enabling the strictest _feasible_ set of
MyPy checks is provided as well.
Since MicroPython does not provide a `typing` module runtime it is not
feasible to providate type annotations for all objects, and for some reason
MyPy with `--strict` does not even allow in-code suppressions for these
unavoidable `no-untyped-def` cases.


## Use

`make init` initializes the directory structure needed by the Makefile.

`make` or `make static-checks` analyzes the code in `SRC_CHECKED`.

`make upload` compiles the files in `SRC_COMPILED` and uploads the resulting
`.mpy` files, in combination with the files in `SRC_EXTRA`, to the target
device.

`make help` provides more information for other targets, and comments
in `Makefile.in` provides information about variables that can be overridden.
