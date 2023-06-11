from queue import Queue

def BFS(graph, start):
    n = len(graph)
    visited = [False] * n
    d = [-1] * n
    p = [-1] * n

    visited[start] = True
    d[start] = 0
    Q = Queue()
    Q.put(start)

    while not Q.empty():
        u = Q.get()

        for v in range(n):
            if graph[u][v] == 1 and not visited[v]:
                visited[v] = True
                d[v] = d[u] + 1
                p[v] = u
                Q.put(v)

    return visited, d, p


graph = [
    [0,1,0,1,0,0],
    [0,0,0,0,1,0],
    [0,0,0,0,1,1],
    [1,0,0,0,0,0],
    [0,0,0,1,0,0],
    [0,0,0,0,0,1]
]

start_V = 3
visited, distance, parent=(BFS(graph, start_V))
for v in range(len(graph)):
    print(f"Wierzchołek {v}: visited = {visited[v]}, "
          f"disance = {distance[v]}, parent={parent[v]}")