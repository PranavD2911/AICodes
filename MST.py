import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edge(self, u, v, weight):
        self.graph[u][v] = weight
        self.graph[v][u] = weight

    def print_mst(self, parent):
        print("Edge\tWeight")
        for i in range(1, self.V):
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]])

    def greedy_mst(self):
        key = [sys.maxsize] * self.V
        parent = [None] * self.V
        key[0] = 0  # Start from the first vertex
        mst_set = [False] * self.V

        for _ in range(self.V):
            # Find the vertex with the minimum key value from the set of vertices not yet included in MST
            u = self.min_key(key, mst_set)
            mst_set[u] = True

            # Update key values and parent index of the adjacent vertices of the picked vertex
            for v in range(self.V):
                if self.graph[u][v] > 0 and not mst_set[v] and self.graph[u][v] < key[v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        self.print_mst(parent)

    def min_key(self, key, mst_set):
        min_value = sys.maxsize
        min_index = -1

        for v in range(self.V):
            if not mst_set[v] and key[v] < min_value:
                min_value = key[v]
                min_index = v

        return min_index


# Taking input from the user
vertices = int(input("Enter the number of vertices: "))
edges = int(input("Enter the number of edges: "))

graph = Graph(vertices)

print("Enter edge details in the format 'u v weight':")

for _ in range(edges):
    u, v, weight = map(int, input().split())
    graph.add_edge(u, v, weight)

print("Minimum Spanning Tree:")
graph.greedy_mst()
