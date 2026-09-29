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

"""Test extension."""

import griffe

namespace = "runtime-objects"


def test_static_analysis() -> None:
    """Runtime objects are added to Griffe objects during static analysis."""
    with griffe.temporary_visited_module(
        """
        a = 0
        b = "hello"
        def c(): ...
        class d:
            def e(self): ...
            f = True
            def __init__(self):
                self.g = 0.1
        """,
        extensions=griffe.load_extensions("griffe_runtime_objects"),
    ) as module:
        assert module["a"].extra[namespace]["object"] == 0
        assert module["b"].extra[namespace]["object"] == "hello"
        assert module["c"].extra[namespace]["object"].__name__ == "c"
        assert module["d"].extra[namespace]["object"].__name__ == "d"
        assert module["d.e"].extra[namespace]["object"].__name__ == "e"
        assert module["d.f"].extra[namespace]["object"] is True
        assert namespace not in module["d.g"].extra


def test_dynamic_analysis() -> None:
    """Runtime objects are added to Griffe objects during dynamic analysis."""
    with griffe.temporary_inspected_module(
        """
        a = 0
        b = "hello"
        def c(): ...
        class d:
            def e(self): ...
            f = True
            def __init__(self):
                self.g = 0.1
        """,
        extensions=griffe.load_extensions("griffe_runtime_objects"),
    ) as module:
        assert module["a"].extra[namespace]["object"] == 0
        assert module["b"].extra[namespace]["object"] == "hello"
        assert module["c"].extra[namespace]["object"].__name__ == "c"
        assert module["d"].extra[namespace]["object"].__name__ == "d"
        assert module["d.e"].extra[namespace]["object"].__name__ == "e"
        assert module["d.f"].extra[namespace]["object"] is True
        assert "g" not in module["d"].members
