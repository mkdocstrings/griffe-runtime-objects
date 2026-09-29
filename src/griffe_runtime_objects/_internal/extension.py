# SPDX-License-Identifier: ISC
#
# ISC License
#
# Copyright (c) 2024, Timothée Mazzucotelli and contributors
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

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
