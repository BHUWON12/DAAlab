import heapq

def prim(graph, start_node):
    mst = []
    visited = set([start_node])
    edges = [(cost, start_node, to) for to, cost in graph[start_node].items()]
    heapq.heapify(edges)

    while edges:
        cost, frm, to = heapq.heappop(edges)
        if to not in visited:
            visited.add(to)
            mst.append((frm, to, cost))

            for next_to, next_cost in graph[to].items():
                if next_to not in visited:
                    heapq.heappush(edges, (next_cost, to, next_to))

    return mst

if __name__ == "__main__":
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }
    start_node = 'A'
    mst = prim(graph, start_node)
    print("Minimum Spanning Tree:", mst)
