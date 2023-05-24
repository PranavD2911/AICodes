class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = []
        rank = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while e < self.V - 1:
            u, v, w = self.graph[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e += 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        print("Minimal Spanning Tree:")
        for u, v, weight in result:
            print(f"{u} -- {v} => {weight}")


# Get the number of vertices from the user
V = int(input("Enter the number of vertices: "))

# Create a graph object
graph = Graph(V)

# Get the edges and their weights from the user
while True:
    u, v, weight = input("Enter an edge and its weight (u v weight), or 'done' to finish: ").split()
    if u == "done" or v == "done" or weight == "done":
        break
    graph.add_edge(int(u), int(v), int(weight))

# Find the Minimal Spanning Tree using Kruskal's algorithm
graph.kruskal()
