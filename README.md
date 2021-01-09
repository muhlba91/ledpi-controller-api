# Flask API for LED-Pi - Raspberry Pi WS2801 LED Controller

[![](https://img.shields.io/github/license/muhlba91/ledpi-controller-api?style=for-the-badge)](LICENSE)
[![](https://img.shields.io/github/workflow/status/muhlba91/ledpi-controller-api/Python%20package?style=for-the-badge)](https://github.com/muhlba91/ledpi-controller/actions)

This repository contains a **Flask API** to control a **WS2801 LED strip** connected to a Raspberry Pi
using [ledpi-controller](https://github.com/muhlba91/ledpi-controller).

---

## Installation

1) Checkout the repository.
2) Create a configuration file as defined
   per [`ledpi-controller`](https://github.com/muhlba91/ledpi-controller#configuration).
3) Install the dependencies.

```bash
$ pip install poetry
$ poetry install
```

4) Run the application.

```bash
$ poetry run python app/main.py -c path/to/config.yml -s path/to/state.yml
```

---

## Development

The project uses [poetry](https://poetry.eustace.io/) and to install all dependencies and the build environment, run:

```bash
$ pip install poetry
$ poetry install
```

### Testing

1) Install all dependencies as shown above.
2) Run `pytest` by:

```bash
$ poetry run pytest
# or
$ pytest
```

### Linting and Code Style

The project uses [flakehell](https://github.com/life4/flakehell) as a wrapper for flake8,
and [black](https://github.com/psf/black) for automated code style fixing, also
using [pre-commit](https://pre-commit.com/).

1) Install all dependencies as shown above.
2) (Optional) Install pre-commit hooks:

```bash
$ poetry run pre-commit install
```

3) Run black:

```bash
$ poetry run black .
```

4) Run flakehell:

```bash
$ poetry run flakehell lint
```

---

## Contributions

Please feel free to contribute, be it with Issues or Pull Requests! Please read
the [Contribution guidelines](CONTRIBUTING.md)
