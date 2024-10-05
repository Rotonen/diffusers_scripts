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

real 4m3.882s
user 2m4.826s
sys 1m43.195s

flux-dev-16.py

real 6m19.258s
user 4m49.680s
sys 1m18.687s

flux-dev-8.py

real 5m32.990s
user 9m19.441s
sys 4m32.792s

flux-schnell-16.py

real 0m48.955s
user 0m25.809s
sys 0m14.294s

flux-schnell-8.py

real 2m9.099s
user 7m9.572s
sys 2m21.556s

latte-1.py

real 0m58.887s
user 1m0.014s
sys 0m30.556s

sa-10.py

real 0m58.454s
user 1m5.611s
sys 0m3.884s

sd-21.py

real 0m53.635s
user 0m50.140s
sys 0m15.909s

sd-30.py

real 0m49.789s
user 1m0.705s
sys 0m25.067s

sd-turbo.py

real 0m13.490s
user 0m24.089s
sys 0m14.355s

real 22m48.441s
user 28m9.887s
sys 11m40.295s
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
