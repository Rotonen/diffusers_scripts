# Various Trivial Diffuers Scripts for Personal Use

Collection of various local use convenience scripts for playing around with diffusers.

## Level of Support Offered

I'll just offer a parable: "When selling a used car, the warrantly ends when the car moves under its own power and the
merchant is able to see the tail lights."

## Development Environment

I'm working on a Debian Bookworm box with an Nvidia RTX A4000.

If you have a functional Python 3.11 installation, `uv run --locked` should have you covered /wrt local setup.

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

* Python formatting: ruff
* Python linting: ruff
* MarkDown linting: pymarkdownlnt

## Scripts Provided

Every script provided has default values for every parameter, so you can try them out without having to dive in deeper.

### Stable Diffusion Turbo 16bit

* `uv run --locked sd-turbo.py`
* `uv run --locked sd-turbo.py --help`

A fast model, which produces something at a single step. Not terrible, not great.

### Stable Diffusion 2.1 16bit

* `uv run --locked sd-21.py`
* `uv run --locked sd-21.py --help`

The memory use is not horrible and it's not too slow. The output is not too bad, but not great either.

### Stable Diffusion 3.0 16bit

* `uv run --locked sd-30.py`
* `uv run --locked sd-30.py --help`

Medium quality and speed.

### Flux.1 Schnell 16bit

* `uv run --locked flux-schnell-16.py`
* `uv run --locked flux-schnell-16.py --help`

Good quality and very fast. Somewhat memory hungry.

### Flux.1 Schnell 8bit

* `uv run --locked flux-schnell-8.py`
* `uv run --locked flux-schnell-8.py --help`

Good quality and very fast. Somewhat less memory hungry.

### Flux.1 Dev 16bit

* `uv run --locked flux-dev-16.py`
* `uv run --locked flux-dev-16.py --help`

Good quality and somewhat slow. Memory hungry.

### Flux.1 Dev 8bit

* `uv run --locked flux-dev-8.py`
* `uv run --locked flux-dev-8.py --help`

Good quality and somewhat less slow. Somewhat less memory hungry.

### Stable Audio 1.0

* `uv run --locked sa-10.py`
* `uv run --locked sa-10.py --help`

Very mixed results. Not too slow. Not too memory hungry.

### Latte-1

* `uv run --locked latte-1.py`
* `uv run --locked latte-1.py --help`

Very bad results. Not too slow. Somewhat memory hungry. I'm probably using it wrong.
