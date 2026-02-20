

from __future__ import annotations


class CircularQueue:
    def __init__(self, capacity: int = 100):
        if capacity <= 0:
            raise ValueError("capacity must be positive")
        self._data = [None] * capacity
        self._front = -1
        self._rear = -1

    @property
    def capacity(self) -> int:
        return len(self._data)

    def is_empty(self) -> bool:
        return self._front == -1

    def is_full(self) -> bool:
        if self.is_empty():
            return False
        return (self._rear + 1) % self.capacity == self._front

    def enqueue(self, value):
        if self.is_full():
            print("Queue is full")
            return -1

        if self.is_empty():
            self._front = 0
            self._rear = 0
        else:
            self._rear = (self._rear + 1) % self.capacity

        self._data[self._rear] = value
        return 0

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return -1

        value = self._data[self._front]
        if self._front == self._rear:
            # became empty
            self._front = -1
            self._rear = -1
        else:
            self._front = (self._front + 1) % self.capacity
        return value

    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return -1
        return self._data[self._front]

    def to_list(self) -> list:
        if self.is_empty():
            return []
        out = []
        i = self._front
        while True:
            out.append(self._data[i])
            if i == self._rear:
                break
            i = (i + 1) % self.capacity
        return out


# -------------------------
# Deprecated compatibility
# -------------------------

class C_Queue(CircularQueue):  # noqa: N801
    def insert(self, x):
        return self.enqueue(x)

    def delete(self):
        return self.dequeue()

    def display(self):
        print(self.to_list())
