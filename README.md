# Various Trivial Diffuers Scripts for Personal Use

Collection of various local use convenience scripts for playing around with diffusers.

## Level of Support Offered

I'll just offer a parable: "When selling a used car, the warrantly ends when the car moves under its own power and the
merchant is able to see the tail lights."

## Development Environment

I'm working on a Debian Bookworm box.

Some of this stuff also works on macOS. Please refer to the disclaimer above.

### Editorconfig

* UTF-8
* LF
* Managed whitespace
* Lines are 120 characters long

The line length is inherited by all other configs.

### Formatting

* ruff

### Linting

* ruff
* pymarkdown

Refer to `pyproject.toml` for details on which linters are enabled and how they are set up.

## CI

* Formatting: ruff
* Python linting: ruff
* MarkDown linting: pymarkdownlnt
