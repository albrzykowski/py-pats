"""Facade pattern exercise."""
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
        # TODO: Return results from all subsystem operations
        return []
