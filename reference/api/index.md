# griffe_runtime_objects

griffe-runtime-objects package.

Make runtime objects available through `extra`.

Classes:

- **`RuntimeObjectsExtension`** – Store runtime objects in Griffe objects' extra attribute.

## RuntimeObjectsExtension

Bases: `Extension`

Store runtime objects in Griffe objects' `extra` attribute.

Methods:

- **`on_instance`** – Get runtime object corresponding to Griffe object, store it in extra namespace.

### on_instance

```
on_instance(
    *, node: AST | ObjectNode, obj: Object, **kwargs: Any
) -> None
```

Get runtime object corresponding to Griffe object, store it in `extra` namespace.

Source code in `src/griffe_runtime_objects/_internal/extension.py`

```
def on_instance(self, *, node: AST | griffe.ObjectNode, obj: griffe.Object, **kwargs: Any) -> None:  # noqa: ARG002
    """Get runtime object corresponding to Griffe object, store it in `extra` namespace."""
    if isinstance(node, griffe.ObjectNode):
        runtime_obj = node.obj
    else:
        filepath = obj.package.filepath
        search_paths = [path.parent for path in filepath] if isinstance(filepath, list) else [filepath.parent]
        try:
            runtime_obj = griffe.dynamic_import(obj.path, search_paths)
        except ImportError as error:
            _logger.debug(f"Could not import {obj.path}: {error}")
            return
    obj.extra["runtime-objects"]["object"] = runtime_obj
```
