"""Facade pattern solution."""
from typing import List


class SubsystemA:
    """Subsystem A."""

    def operation_a(self) -> str:
        return "Subsystem A"


class SubsystemB:
    """Subsystem B."""

    def operation_b(self) -> str:
        return "Subsystem B"


class SubsystemC:
    """Subsystem C."""

    def operation_c(self) -> str:
        return "Subsystem C"


class Facade:
    """Facade that simplifies subsystem access."""

    def __init__(self) -> None:
        self._a = SubsystemA()
        self._b = SubsystemB()
        self._c = SubsystemC()

    def operation(self) -> List[str]:
        """Perform complex operation through subsystems."""
        return [
            self._a.operation_a(),
            self._b.operation_b(),
            self._c.operation_c(),
        ]
