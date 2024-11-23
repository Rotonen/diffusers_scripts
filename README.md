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

real 3m28.897s
user 1m51.189s
sys 1m33.229s

flux-dev-16.py

real 5m53.187s
user 4m44.218s
sys 0m56.602s

flux-schnell-16.py

real 0m53.866s
user 0m25.260s
sys 0m14.718s

sa-10.py

real 0m56.052s
user 1m5.661s
sys 0m5.822s

sd-21.py

real 0m55.068s
user 0m52.917s
sys 0m15.861s

sd-30.py

real 0m59.950s
user 1m11.507s
sys 0m26.018s

sd-35.py

real 2m36.829s
user 2m13.813s
sys 0m32.909s

sd-35-turbo.py

real 0m36.307s
user 0m35.386s
sys 0m19.100s

sdxl-turbo.py

real 0m13.382s
user 0m24.129s
sys 0m13.887s

real 16m33.539s
user 13m24.080s
sys 4m38.145s
```

## CI

* Python formatting: ruff
* Python linting: ruff
* MarkDown linting: pymarkdownlnt
* Reviewdog Shellcheck

## Scripts Provided

Every script provided has default values for every parameter, so you can try them out without having to dive in deeper.

### Stable Diffusion XL Turbo 16bit

* `uv run --locked sdxl-turbo.py`
* `uv run --locked sdxl-turbo.py --help`

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

### Flux.1 Dev 16bit

* `uv run --locked flux-dev-16.py`
* `uv run --locked flux-dev-16.py --help`

Good quality and somewhat slow. Memory hungry.

### Stable Audio 1.0

* `uv run --locked sa-10.py`
* `uv run --locked sa-10.py --help`

Very mixed results. Not too slow. Not too memory hungry.

### CogVideoX

* `uv run --locked cogvideox.py`
* `uv run --locked cogvideox.py --help`

Surprisingly good results. Surprisingly fast. Surprisingly not too memory hungry.

### Stable Diffusion 3.5 16bit

* `uv run --locked sd-35.py`
* `uv run --locked sd-35.py --help`

Sorta fast and excellent results.

### Stable Diffusion 3.5 Turbo 16bit

* `uv run --locked sd-35-turbo.py`
* `uv run --locked sd-35-turbo.py --help`

Hella fast for the quality and very good results.
