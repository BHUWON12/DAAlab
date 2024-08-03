def warshall_algorithm(graph):
    n = len(graph)
    reach = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            reach[i][j] = graph[i][j]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                reach[i][j] = reach[i][j] or (reach[i][k] and reach[k][j])

    return reach

if __name__ == "__main__":
    graph = [
        [1, 1, 0, 1],
        [0, 1, 1, 0],
        [0, 0, 1, 1],
        [0, 0, 0, 1]
    ]
    transitive_closure = warshall_algorithm(graph)
    print("Transitive Closure:")
    for row in transitive_closure:
        print(row)
