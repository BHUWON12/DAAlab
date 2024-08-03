from collections import defaultdict

def topological_sort(graph):
    visited = set()
    stack = []

    def dfs(v):
        visited.add(v)
        for neighbor in graph[v]:
            if neighbor not in visited:
                dfs(neighbor)
        stack.append(v)

    for vertex in graph:
        if vertex not in visited:
            dfs(vertex)

    stack.reverse()
    return stack

if __name__ == "__main__":
    graph = {
        'A': ['C'],
        'B': ['C', 'D'],
        'C': ['E'],
        'D': ['F'],
        'E': ['F'],
        'F': []
    }
    print("Topological Ordering:", topological_sort(graph))
