class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def is_safe(self, v, color, c):
        for i in range(self.vertices):
            if self.graph[v][i] == 1 and color[i] == c:
                return False
        return True

    def graph_coloring(self, m):
        color = [-1] * self.vertices
        color[0] = 0
        return self.graph_coloring_util(m, color, 1)

    def graph_coloring_util(self, m, color, v):
        if v == self.vertices:
            return color

        for c in range(m):
            if self.is_safe(v, color, c):
                color[v] = c
                result = self.graph_coloring_util(m, color, v + 1)
                if result is not None:
                    return result
                color[v] = -1

        return None


# Helper function to print the graph coloring
def print_graph_coloring(graph, colors):
    print("Vertex\tColor")
    for i in range(graph.vertices):
        print(f"{i}\t\t{colors[i]}")


# Input the number of vertices and edges from the user
num_vertices = int(input("Enter the number of vertices: "))
num_edges = int(input("Enter the number of edges: "))

# Create an empty graph with the given number of vertices
graph = Graph(num_vertices)

# Input the edges from the user
for _ in range(num_edges):
    src = int(input("Enter the source vertex of the edge: "))
    dest = int(input("Enter the destination vertex of the edge: "))
    graph.graph[src][dest] = 1
    graph.graph[dest][src] = 1

# Input the maximum number of colors from the user
num_colors = int(input("Enter the maximum number of colors: "))

# Solve the graph coloring problem using Branch and Bound with Backtracking
colors = graph.graph_coloring(num_colors)

# Print the result
if colors is None:
    print("No valid coloring exists.")
else:
    print_graph_coloring(graph, colors)
