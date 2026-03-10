# AGENTS.md

## Project Goal

This project contains **training materials for learning selected design patterns in Python**.  
The repository should provide **very small programming exercises** that help learners understand the core idea of each pattern.

---

## Design Patterns Covered

The project must include exercises for:

- Observer
- Adapter
- Facade
- Strategy

Each pattern should have **one exercise**.

---

## Repository Structure

- `exercises` - incomplete implementations for learners
- `solutions` - complete working implementations
- `tests` - unit tests validating expected behavior

---

## Functional Requirements

### Exercises

Code should intentionally miss small pieces of logic. The missing parts should be simple and limited in scope. When tests are run against this directory, **they should fail**.

### Solutions

Implementations must be complete and functional. They must satisfy the behavior verified by the tests. When tests are run against this directory, **all tests must pass**.

### Tests

There must be **one test case per design pattern** (4 total). Each test should verify a **single, simple behavior** related to the pattern.

---

## Development Commands

### Running Tests

```bash
python -m pytest                    # Run all tests
python -m pytest -v                # Verbose output
python -m pytest -k "pattern_name" # Run tests matching pattern
python -m pytest tests/test_observer.py::TestPattern::test_behavior  # Single test
```

### Linting

```bash
ruff check .              # Lint
ruff check --fix .       # Lint with auto-fix
ruff format .            # Format
```

### Type Checking

```bash
mypy .
```

### Full CI Checks

```bash
ruff check . && ruff format --check . && mypy . && python -m pytest -v
```

---

## Code Style Guidelines

### General Principles

- Write **clean, minimal code** - this is an educational project
- Focus on **clarity and simplicity** over clever optimizations
- Keep functions **short and focused** (ideally under 30 lines)

### Imports

Group imports in this order: standard library, third-party, local. Use `import module` for standard library, `from module import name` for others. Do not use wildcard imports.

```python
import collections
from typing import List, Optional

import pytest
```

### Formatting

- Use **4 spaces** for indentation (no tabs)
- Maximum line length: **100 characters**
- No trailing whitespace

### Naming Conventions

- **Variables/functions**: `snake_case`
- **Classes**: `PascalCase`
- **Constants**: `UPPER_SNAKE_CASE`
- **Private methods**: prefix with underscore (`_internal_method`)
- Use singular nouns for variables

### Type Annotations

Always use type hints. Use `Optional[X]` instead of `X | None` for Python 3.9 compatibility.

```python
def calculate_total(items: List[float], tax_rate: Optional[float] = None) -> float:
    subtotal = sum(items)
    if tax_rate is None:
        return subtotal
    return subtotal * (1 + tax_rate)
```

### Docstrings

Use **Google-style** docstrings for all public functions and classes.

```python
def add_observer(observer: Observer) -> None:
    """Add an observer to the subject's list.

    Args:
        observer: The observer to add.
    """
    self._observers.append(observer)
```

### Error Handling

- Use **custom exceptions** for domain-specific errors
- Catch specific exceptions rather than using bare `except:`
- Prefer **early returns** to reduce nesting
- Do not swallow exceptions silently

### Testing Guidelines

- Write **one test per behavior** per design pattern
- Keep tests simple and focused on a single assertion
- Use descriptive test names: `test_<pattern>_<behavior>`
- Follow the Arrange-Act-Assert pattern

```python
def test_observer_notifies_on_change(self):
    """Observer should be notified when subject changes."""
    subject = Subject()
    observer = MockObserver()
    subject.attach(observer)
    subject.notify()
    observer.update.assert_called_once()
```

### File Organization

- One class per file (or related classes together)
- File name should match class name (e.g., `observer.py` contains `Observer`)
- Keep module-level code minimal - use `if __name__ == "__main__":` for scripts
- Group related modules in packages (directories with `__init__.py`)

---

## Common Development Tasks

### Adding a New Pattern Exercise

1. Create `exercises/<pattern>.py` with incomplete implementation
2. Create `solutions/<pattern>.py` with complete implementation
3. Create `tests/test_<pattern>.py` with one test case
4. Verify exercises fail and solutions pass
