"""Tests for Strategy pattern."""
import unittest

from exercises.strategy import ConcreteStrategyA, ConcreteStrategyB, Context


class TestStrategy(unittest.TestCase):
    """Test cases for Strategy pattern."""

    def test_context_executes_strategy(self):
        """Context should execute the assigned strategy."""
        strategy = ConcreteStrategyA()
        context = Context(strategy)

        result = context.execute_strategy([1, 2, 3, 4, 5])

        self.assertEqual(result, 15)


if __name__ == "__main__":
    unittest.main()
