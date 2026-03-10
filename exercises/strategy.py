"""Strategy pattern exercise."""
from typing import List


class Strategy:
    """Base strategy interface."""

    def execute(self, data: List[int]) -> int:
        """Execute strategy on data."""
        raise NotImplementedError


class ConcreteStrategyA(Strategy):
    """Strategy that sums values."""

    def execute(self, data: List[int]) -> int:
        return sum(data)


class ConcreteStrategyB(Strategy):
    """Strategy that returns max value."""

    def execute(self, data: List[int]) -> int:
        return max(data)


class Context:
    """Context that uses a strategy."""

    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def set_strategy(self, strategy: Strategy) -> None:
        """Set the strategy."""
        self._strategy = strategy

    def execute_strategy(self, data: List[int]) -> int:
        """Execute the current strategy."""
        # TODO: Execute the strategy on the data
        return 0
