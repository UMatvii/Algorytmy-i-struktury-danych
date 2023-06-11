from Vertex_Graph import *


def create_graph():
    g = Graph()

    num_vertices = int(input("Podaj ilość wierzchołków: "))
    for i in range(num_vertices):
        key = input("Podaj identyfikatory wierzchołków: ")
        g.addVertex(key)

    num_edges = int(input("Podaj ilość krawędzi: "))
    for i in range(num_edges):
        from_vertex = input("Podaj wierzchołek początkowy: ")
        to_vertex = input("Podaj wierzchołek końcowy: ")
        cost = int(input("Podaj wagę krawędzi: "))
        g.addEdge(from_vertex, to_vertex, cost)

    return g


graph = create_graph()

print("Wierzchołki: ")
for vertex in graph.getVertices():
    print(vertex)

print("Krawędzi: ")
for vertex in graph:
    for neighbor in vertex.getConnections():
        print(f"{vertex.getId()} --> {neighbor.getId()} (waga: {vertex.getWeight(neighbor)})")