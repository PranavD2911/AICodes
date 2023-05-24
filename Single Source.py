import sys

# Function to find the vertex with the minimum distance value,
# from the set of vertices not yet included in the shortest path tree
def min_distance(distances, visited):
    min_dist = sys.maxsize
    min_index = -1

    for v in range(len(distances)):
        if distances[v] < min_dist and not visited[v]:
            min_dist = distances[v]
            min_index = v

    return min_index

# Function to print the shortest path from the source to the target vertex
def print_path(parents, target):
    if parents[target] == -1:
        print(target, end=' ')
        return
    print_path(parents, parents[target])
    print(target, end=' ')

# Function to implement Dijkstra's algorithm
def dijkstra(graph, source):
    num_vertices = len(graph)
    distances = [sys.maxsize] * num_vertices
    parents = [-1] * num_vertices
    visited = [False] * num_vertices

    distances[source] = 0

    for _ in range(num_vertices):
        u = min_distance(distances, visited)
        visited[u] = True

        for v in range(num_vertices):
            if graph[u][v] > 0 and not visited[v] and distances[v] > distances[u] + graph[u][v]:
                distances[v] = distances[u] + graph[u][v]
                parents[v] = u

    # Print the shortest paths
    for v in range(num_vertices):
        print("Shortest path from", source, "to", v, ":", end=' ')
        print_path(parents, v)
        print("Distance:", distances[v])

# Get input from the user
num_vertices = int(input("Enter the number of vertices in the graph: "))
graph = [[0] * num_vertices for _ in range(num_vertices)]

# Get the adjacency matrix representing the graph
for i in range(num_vertices):
    for j in range(num_vertices):
        if i != j:
            weight = int(input(f"Enter the weight between vertex {i} and {j} (or 0 if no edge exists): "))
            graph[i][j] = weight

source_vertex = int(input("Enter the source vertex: "))

# Call Dijkstra's algorithm
dijkstra(graph, source_vertex)
