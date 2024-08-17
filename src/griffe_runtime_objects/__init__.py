"""griffe-runtime-objects package.

Make runtime objects available through `extra`.
"""

from __future__ import annotations

from griffe_runtime_objects._internals.extension import RuntimeObjectsExtension

__all__: list[str] = ["RuntimeObjectsExtension"]
