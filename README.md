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

real 10m33.656s
user 1m54.323s
sys 1m37.042s

cogview3.py

real 2m50.749s
user 2m44.942s
sys 0m22.819s

flux-dev-16.py

real 5m56.333s
user 4m39.890s
sys 1m3.114s

flux-schnell-16.py

real 0m53.507s
user 0m24.947s
sys 0m15.274s

sa-10.py

real 0m53.894s
user 1m0.818s
sys 0m5.792s

sd-21.py

real 0m52.081s
user 0m48.094s
sys 0m16.067s

sd-30.py

real 0m52.228s
user 1m2.891s
sys 0m24.934s

sd-35.py

real 2m26.211s
user 2m5.938s
sys 0m35.565s

sd-35-turbo.py

real 0m37.089s
user 0m34.860s
sys 0m20.907s

sdxl-turbo.py

real 0m16.304s
user 0m30.315s
sys 0m13.901s

real 26m12.051s
user 15m47.018s
sys 5m15.414s
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

### Cogview3-plus 16bit

* `uv run --locked sd-35-turbo.py`
* `uv run --locked sd-35-turbo.py --help`

Not slow. Very saturated and poppy results. I sorta like it, it's different.
