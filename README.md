# griffe-runtime-objects

[![documentation](https://img.shields.io/badge/docs-mkdocs-708FCC.svg?style=flat)](https://mkdocstrings.github.io/griffe-runtime-objects/)
[![gitpod](https://img.shields.io/badge/gitpod-workspace-708FCC.svg?style=flat)](https://gitpod.io/#https://github.com/mkdocstrings/griffe-runtime-objects)
[![gitter](https://badges.gitter.im/join%20chat.svg)](https://app.gitter.im/#/room/#griffe-runtime-objects:gitter.im)

Make runtime objects available through `extra`.

## Installation

This project is available to sponsors only, through my Insiders program.
See Insiders [explanation](https://mkdocstrings.github.io/griffe-runtime-objects/insiders/)
and [installation instructions](https://mkdocstrings.github.io/griffe-runtime-objects/insiders/installation/).

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