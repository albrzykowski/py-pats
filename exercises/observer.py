"""Observer pattern exercise."""
from typing import List


class Observer:
    """Base observer interface."""

    def update(self, message: str) -> None:
        """Receive update from subject."""
        raise NotImplementedError


class Subject:
    """Subject that notifies observers."""

    def __init__(self) -> None:
        self._observers: List[Observer] = []
        self._state: str = ""

    def attach(self, observer: Observer) -> None:
        """Attach an observer."""
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        """Detach an observer."""
        self._observers.remove(observer)

    def notify(self) -> None:
        """Notify all observers."""
        # TODO: Implement notification to all observers
        pass

    def set_state(self, state: str) -> None:
        """Set state and notify observers."""
        self._state = state
        self.notify()

    def get_state(self) -> str:
        """Get current state."""
        return self._state
