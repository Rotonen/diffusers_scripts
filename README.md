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
* shellcheck

Refer to `pyproject.toml` for details on which linters are enabled and how they are set up.

### Smoketest

The nature of these scripts does not allow for properly checking for correctness of operation and/or output. For this
purpose a manual smoketest script is provided for assessing if any manual version bumps broke anything.

```console
$ ./smoketest.sh

cogvideox.py

real 3m30.494s
user 1m49.866s
sys 1m31.353s

flux-dev-16.py

real 6m9.287s
user 4m33.234s
sys 1m20.181s

flux-dev-8.py

real 4m53.429s
user 8m9.986s
sys 3m33.157s

flux-schnell-16.py

real 0m55.208s
user 0m23.858s
sys 0m14.999s

flux-schnell-8.py

real 2m17.038s
user 6m45.482s
sys 2m9.343s

sa-10.py

real 0m47.443s
user 0m53.694s
sys 0m5.526s

sd-21.py

real 0m50.465s
user 0m46.988s
sys 0m15.534s

sd-30.py

real 0m46.716s
user 0m58.262s
sys 0m24.008s

sd-turbo.py

real 0m13.690s
user 0m23.808s
sys 0m12.784s

real 20m23.770s
user 24m45.179s
sys 9m46.885s
```

## CI

* Python formatting: ruff
* Python linting: ruff
* MarkDown linting: pymarkdownlnt
* Reviewdog Shellcheck

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

### CogVideoX

* `uv run --locked cogvideox.py`
* `uv run --locked cogvideox.py --help`

Surprisingly good results. Surprisingly fast. Surprisingly not too memory hungry.
