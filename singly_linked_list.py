
from __future__ import annotations


class SinglyNode:
    def __init__(self, value):
        self.value = value
        self.next: SinglyNode | None = None


class SinglyLinkedList:
    def __init__(self):
        self.head: SinglyNode | None = None

    def insert_first(self, value):
        new_node = SinglyNode(value)
        new_node.next = self.head
        self.head = new_node

    def insert_last(self, value):
        if self.head is None:
            self.head = SinglyNode(value)
            return
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = SinglyNode(value)

    def delete_first(self):
        if self.head is None:
            print("list is empty")
            return -1
        value = self.head.value
        self.head = self.head.next
        return value

    def delete_last(self):
        if self.head is None:
            print("list is empty")
            return -1
        if self.head.next is None:
            value = self.head.value
            self.head = None
            return value
        prev = self.head
        cur = self.head.next
        while cur.next is not None:
            prev, cur = cur, cur.next
        prev.next = None
        return cur.value

    def search(self, value) -> bool:
        cur = self.head
        while cur is not None:
            if cur.value == value:
                return True
            cur = cur.next
        return False

    def to_list(self) -> list:
        out = []
        cur = self.head
        while cur is not None:
            out.append(cur.value)
            cur = cur.next
        return out


# -------------------------
# Deprecated compatibility
# -------------------------

class node:  # noqa: N801
    def __init__(self, d):
        self.Data = d
        self.next = None


class linked_list(SinglyLinkedList):  # noqa: N801
    # keep old head semantics but adapt between node <-> SinglyNode
    def __init__(self):
        super().__init__()

    def _wrap(self, new_head: SinglyNode | None):
        # expose as 'node' instances for legacy access patterns
        if new_head is None:
            self.head = None
            return
        legacy_head = node(new_head.value)
        cur_new = new_head.next
        cur_legacy = legacy_head
        while cur_new is not None:
            nxt = node(cur_new.value)
            cur_legacy.next = nxt
            cur_legacy = nxt
            cur_new = cur_new.next
        self.head = legacy_head

    def _unwrap(self) -> SinglyNode | None:
        if self.head is None:
            return None
        new_head = SinglyNode(self.head.Data)
        cur_legacy = self.head.next
        cur_new = new_head
        while cur_legacy is not None:
            cur_new.next = SinglyNode(cur_legacy.Data)
            cur_new = cur_new.next
            cur_legacy = cur_legacy.next
        return new_head

    # legacy misspelling preserved
    def insert_frist(self, x):  # noqa: N802
        tmp = self._unwrap()
        new_list = SinglyLinkedList()
        new_list.head = tmp
        new_list.insert_first(x)
        self._wrap(new_list.head)

    def insert_last(self, x):  # already same name in original
        tmp = self._unwrap()
        new_list = SinglyLinkedList()
        new_list.head = tmp
        new_list.insert_last(x)
        self._wrap(new_list.head)

    def del_frist(self):  # noqa: N802
        tmp = self._unwrap()
        new_list = SinglyLinkedList()
        new_list.head = tmp
        val = new_list.delete_first()
        self._wrap(new_list.head)
        return val

    def del_last(self):  # noqa: N802
        tmp = self._unwrap()
        new_list = SinglyLinkedList()
        new_list.head = tmp
        val = new_list.delete_last()
        self._wrap(new_list.head)
        return val

    def search(self, x):
        tmp = self._unwrap()
        new_list = SinglyLinkedList()
        new_list.head = tmp
        return new_list.search(x)

    def display(self):
        print(self.to_list())
