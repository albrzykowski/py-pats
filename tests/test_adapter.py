"""Tests for Adapter pattern."""
import unittest
from unittest.mock import Mock

from exercises.adapter import LegacyPrinter, ModernPrinter, PrinterAdapter


class TestAdapter(unittest.TestCase):
    """Test cases for Adapter pattern."""

    def test_adapter_calls_legacy_printer(self):
        """Adapter should call legacy printer when print_page is invoked."""
        legacy = Mock(spec=LegacyPrinter)
        adapter = PrinterAdapter(legacy)

        adapter.print_page("test content")

        legacy.print_document.assert_called_once_with("test content")


if __name__ == "__main__":
    unittest.main()
