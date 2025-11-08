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
