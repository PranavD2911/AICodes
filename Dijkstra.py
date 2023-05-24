import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0] * vertices for _ in range(vertices)]

    def min_key(self, key, mst_set):
        min_value = sys.maxsize
        min_index = -1

        for v in range(self.V):
            if key[v] < min_value and not mst_set[v]:
                min_value = key[v]
                min_index = v

        return min_index

    def prim_mst(self):
        key = [sys.maxsize] * self.V
        parent = [None] * self.V
        mst_set = [False] * self.V

        key[0] = 0  # Starting vertex
        parent[0] = -1  # Root of MST

        for _ in range(self.V):
            u = self.min_key(key, mst_set)
            mst_set[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and not mst_set[v] and self.graph[u][v] < key[v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        self.print_mst(parent)

    def print_mst(self, parent):
        print("Edge \tWeight")
        for i in range(1, self.V):
            print(f"{parent[i]} - {i}\t{self.graph[i][parent[i]]}")


# Taking input from the user
V = int(input("Enter the number of vertices: "))
graph = Graph(V)

print("Enter the adjacency matrix (space-separated values):")
for i in range(V):
    row = list(map(int, input().split()))
    for j in range(V):
        graph.graph[i][j] = row[j]

graph.prim_mst()
