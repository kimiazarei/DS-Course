
from __future__ import annotations


class DoublyNode:
    def __init__(self, value):
        self.value = value
        self.next: DoublyNode | None = None
        self.prev: DoublyNode | None = None


class DoublyLinkedList:
    def __init__(self):
        self.head: DoublyNode | None = None
        self.tail: DoublyNode | None = None

    def insert_first(self, value):
        new_node = DoublyNode(value)
        if self.head is None:
            self.head = self.tail = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def insert_last(self, value):
        new_node = DoublyNode(value)
        if self.tail is None:
            self.head = self.tail = new_node
            return
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def delete_after(self, value):
        """Delete the node after the first node whose value == `value`."""
        if self.head is None:
            print("error")
            return -1

        cur = self.head
        while cur is not None and cur.value != value:
            cur = cur.next

        if cur is None:
            print("not found")
            return -1

        target = cur.next
        if target is None:
            print("no node after given value")
            return -1

        nxt = target.next
        cur.next = nxt
        if nxt is not None:
            nxt.prev = cur
        else:
            self.tail = cur
        return target.value

    def to_list_forward(self) -> list:
        out = []
        cur = self.head
        while cur is not None:
            out.append(cur.value)
            cur = cur.next
        return out

    def to_list_backward(self) -> list:
        out = []
        cur = self.tail
        while cur is not None:
            out.append(cur.value)
            cur = cur.prev
        return out


# -------------------------
# Deprecated compatibility
# -------------------------

class dnode:  # noqa: N801
    def __init__(self, x):
        self.Data = x
        self.next = None
        self.back = None


class dlinked_list(DoublyLinkedList):  # noqa: N801
    def ins_frist(self, x):  # noqa: N802
        return self.insert_first(x)

    def del_after(self, x):  # signature kept
        return super().delete_after(x)

    def display(self):
        print(self.to_list_forward())
