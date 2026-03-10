"""Tests for Facade pattern."""
import unittest

from exercises.facade import Facade


class TestFacade(unittest.TestCase):
    """Test cases for Facade pattern."""

    def test_facade_aggregates_subsystem_results(self):
        """Facade should aggregate results from all subsystems."""
        facade = Facade()

        results = facade.operation()

        self.assertEqual(len(results), 3)
        self.assertIn("Subsystem A", results)
        self.assertIn("Subsystem B", results)
        self.assertIn("Subsystem C", results)


if __name__ == "__main__":
    unittest.main()
