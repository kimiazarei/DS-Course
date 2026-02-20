

from __future__ import annotations


class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left: BinaryTreeNode | None = None
        self.right: BinaryTreeNode | None = None


def count_leaves(root: BinaryTreeNode | None) -> int:
    """Return number of leaf nodes in a binary tree."""
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    return count_leaves(root.left) + count_leaves(root.right)


# -------------------------
# Deprecated compatibility
# -------------------------

class Tree_Node(BinaryTreeNode):  # noqa: N801
    def __init__(self, x):
        super().__init__(x)
        self.Data = self.value
        self.Lchild = None
        self.Rchild = None

    # Keep original child attribute names in sync if used.
    @property
    def Lchild(self):
        return self.left

    @Lchild.setter
    def Lchild(self, v):
        self.left = v

    @property
    def Rchild(self):
        return self.right

    @Rchild.setter
    def Rchild(self, v):
        self.right = v


def Count_leaves(root):  # noqa: N802
    return count_leaves(root)
