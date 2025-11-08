from __future__ import annotations

from typing import TYPE_CHECKING, Any

import griffe

if TYPE_CHECKING:
    from ast import AST


_logger = griffe.get_logger("griffe_runtime_objects")


class RuntimeObjectsExtension(griffe.Extension):
    """Store runtime objects in Griffe objects' `extra` attribute."""

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
