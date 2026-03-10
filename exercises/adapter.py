"""Adapter pattern exercise."""
from typing import List


class LegacyPrinter:
    """Legacy printer with old interface."""

    def print_document(self, text: str) -> None:
        """Print document using legacy method."""
        print(f"Legacy: {text}")


class ModernPrinter:
    """Modern printer interface."""

    def print_page(self, content: str) -> None:
        """Print a page."""
        raise NotImplementedError


class PrinterAdapter(ModernPrinter):
    """Adapter that wraps LegacyPrinter to use ModernPrinter interface."""

    def __init__(self, legacy: LegacyPrinter) -> None:
        self._legacy = legacy

    def print_page(self, content: str) -> None:
        """Adapt modern interface to legacy."""
        # TODO: Adapt the call to legacy printer
        pass
