from Lab9.Vertex_Graph import *


def dfs(graph):
    for vertex in graph.getVertices():
        vertex.p = -1
        vertex.visited = False

    czas = 0

    for vertex in graph.getVertices():
        if not vertex.visited:
            czas = dfs_explore(vertex, czas)


def dfs_explore(vertex, czas):
    czas += 1
    vertex.time_1 = czas
    vertex.visited = True

    for sasiad in vertex.getConnections():
        if not sasiad.visited:
            sasiad.p = vertex
            czas = dfs_explore(sasiad, czas)

    czas += 1
    vertex.time_2 = czas

    return czas     