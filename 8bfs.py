

from collections import deque
def bfs(graph, start):
    queue= deque([start])
    visited= set([start])

    bfs_order=[]

    while queue:
        vertex=queue.popleft()
        bfs_order.append(vertex)
        for nabour in graph[vertex]:
            if nabour not in visited:
                queue.append(nabour)
                visited.add(nabour)
    return bfs_order

if __name__=="__main__":
    graph={
        'A':['B','C'],
        'B':['A','D','E'],
        'C':['A','D'],
        'D':['B'],
        'E':['B','C'] }
    
    start_node = input("enter a Start NODE: ")

    bfsresult= bfs(graph,start_node)
    print("BFS traversal of given graph is :",bfsresult)

