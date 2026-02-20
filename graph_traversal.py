"""
Graph traversal algorithms (refactored).

Graph format: dict[node] -> iterable[neighbor]

New API:
- bfs_traverse(graph, start) -> set[visited]
- dfs_traverse(graph, start) -> set[visited]      (iterative)
- dfs_traverse_recursive(graph, start) -> set     (recursive)

Deprecated compatibility:
- BFS(graph, start)
- DFS(graph, start, visited_dict)
"""

from __future__ import annotations
from collections import deque


def bfs_traverse(graph: dict, start):
    visited = set([start])
    q = deque([start])

    while q:
        vertex = q.popleft()
        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)

    return visited


def dfs_traverse(graph: dict, start):
    visited = set()
    stack = [start]
    while stack:
        v = stack.pop()
        if v in visited:
            continue
        visited.add(v)
        # push neighbors in reverse to mimic typical recursive order
        neighbors = list(graph.get(v, []))
        for n in reversed(neighbors):
            if n not in visited:
                stack.append(n)
    return visited


def dfs_traverse_recursive(graph: dict, start):
    visited = set()

    def _visit(v):
        visited.add(v)
        for n in graph.get(v, []):
            if n not in visited:
                _visit(n)

    _visit(start)
    return visited


# -------------------------
# Deprecated compatibility
# -------------------------

def BFS(graph, start):  # noqa: N802
    return bfs_traverse(graph, start)


def DFS(graph, start, visited):  # noqa: N802
    """
    Original signature used a dict/array 'visited' passed by caller.
    We'll respect that while using recursion.
    """
    visited[start] = True
    for ne in graph.get(start, []):
        if not visited.get(ne, False):
            DFS(graph, ne, visited)
