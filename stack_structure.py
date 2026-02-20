"""
Stack implementation (refactored).

New API:
- class SimpleStack(limit=1000)
  - push_item(x)
  - pop_item()
  - peek_item()
  - is_empty()
  - size()
  - to_list()

Deprecated compatibility aliases:
- class stack
  - push/pop/peek/isEmpty/size/display
"""

from __future__ import annotations


class SimpleStack:
    def __init__(self, limit: int = 1000):
        self._items: list = []
        self._limit = limit

    def push_item(self, value):
        if len(self._items) >= self._limit:
            print("stack is full")
            return -1
        self._items.append(value)

    def pop_item(self):
        if not self._items:
            print("stack is empty")
            return -1
        return self._items.pop()

    def peek_item(self):
        if not self._items:
            print("stack is empty")
            return -1
        return self._items[-1]

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def size(self) -> int:
        return len(self._items)

    def to_list(self) -> list:
        return list(self._items)


# -------------------------
# Deprecated compatibility
# -------------------------

class stack(SimpleStack):  # noqa: N801 (kept for compatibility)
    def push(self, x):  # noqa: D401
        return self.push_item(x)

    def pop(self):
        return self.pop_item()

    def peek(self):
        return self.peek_item()

    def isEmpty(self):  # noqa: N802
        return self.is_empty()

    def display(self):
        print(self.to_list())
