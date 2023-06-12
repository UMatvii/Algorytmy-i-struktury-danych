from Lab9.Vertex_Graph import *


class UnionFind:
    def init(self, vertexes):
        self.parent = {}
        self.rank = {}
        for vertex in vertexes:
            self.parent[vertex] = vertex
            self.rank[vertex] = 0

    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def union(self, vertex1, vertex2):
        korzen1 = self.find(vertex1)
        korzen2 = self.find(vertex2)
        if korzen1 != korzen2:
            if self.rank[korzen1] < self.rank[korzen2]:
                self.parent[korzen1] = korzen2
            elif self.rank[korzen1] > self.rank[korzen2]:
                self.parent[korzen2] = korzen1
            else:
                self.parent[korzen2] = korzen1
                self.rank[korzen1] += 1

def kruskal(graph):
    minimum_rozp_tree = []
    krawedzie = []
    for vertex in graph:
        for neighbor in vertex.getConnections():
            weight = vertex.getWeight(neighbor)
            krawedzie.append((vertex.getId(), neighbor.getId(), weight))

    krawedzie.sort(key=lambda x: x[2])

    vertexes = list(graph.getVertices())
    union_find = UnionFind(vertexes)

    for krawedzies in krawedzie:
        vertex1, vertex2, weight = krawedzies
        if union_find.find(vertex1) != union_find.find(vertex2):
            union_find.union(vertex1, vertex2)
            minimum_rozp_tree.append(krawedzies)

    return minimum_rozp_tree