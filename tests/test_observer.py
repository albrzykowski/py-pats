"""Tests for Observer pattern."""
import unittest
from unittest.mock import Mock

from exercises.observer import Observer, Subject


class TestObserver(unittest.TestCase):
    """Test cases for Observer pattern."""

    def test_observer_notified_on_state_change(self):
        """Observer should be notified when subject state changes."""
        subject = Subject()
        observer = Mock(spec=Observer)
        subject.attach(observer)

        subject.set_state("new state")

        observer.update.assert_called_once_with("new state")


if __name__ == "__main__":
    unittest.main()
