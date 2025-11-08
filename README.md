# griffe-runtime-objects

[![ci](https://github.com/mkdocstrings/griffe-runtime-objects/workflows/ci/badge.svg)](https://github.com/mkdocstrings/griffe-runtime-objects/actions?query=workflow%3Aci)
[![documentation](https://img.shields.io/badge/docs-mkdocs-708FCC.svg?style=flat)](https://mkdocstrings.github.io/griffe-runtime-objects/)
[![pypi version](https://img.shields.io/pypi/v/griffe-runtime-objects.svg)](https://pypi.org/project/griffe-runtime-objects/)
[![gitter](https://img.shields.io/badge/matrix-chat-4DB798.svg?style=flat)](https://app.gitter.im/#/room/#griffe-runtime-objects:gitter.im)

Make runtime objects available through `extra`.

## Installation

```bash
pip install griffe-runtime-objects
```

## Usage

[Enable](https://mkdocstrings.github.io/griffe/guide/users/extending/#using-extensions) the `griffe_runtime_objects` extension. Now all Griffe objects will have access to the corresponding runtime objects in their `extra` attribute, under the `runtime-objects` namespace:

```pycon
>>> import griffe
>>> griffe_data = griffe.load("griffe", extensions=griffe.load_extensions("griffe_runtime_objects"), resolve_aliases=True)
>>> griffe_data["parse"].extra
defaultdict(<class 'dict'>, {'runtime-objects': {'object': <function parse at 0x78685c951260>}})
>>> griffe_data["Module"].extra
defaultdict(<class 'dict'>, {'runtime-objects': {'object': <class '_griffe.models.Module'>}})
```

This extension can be useful in custom templates of mkdocstrings-python, to iterate on an object value or attributes.

With MkDocs:

```yaml
plugins:
- mkdocstrings:
    handlers:
      python:
        options:
          extensions:
          - griffe_runtime_objects
```

## Sponsors

<!-- sponsors-start -->
<!-- sponsors-end -->
