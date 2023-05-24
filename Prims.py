# Function to find the vertex with the minimum key value
def min_key(vertices, keys, mst_set):
    min_val = float('inf')
    min_index = -1
    for i in range(vertices):
        if keys[i] < min_val and not mst_set[i]:
            min_val = keys[i]
            min_index = i
    return min_index

# Function to print the constructed MST
def print_mst(parent, graph):
    print("Edge \tWeight")
    for i in range(1, len(graph)):
        print(parent[i], "-", i, "\t", graph[i][parent[i]])

# Function to construct and print MST for a graph
def prim_mst(graph):
    vertices = len(graph)
    # Store the constructed MST
    parent = [None] * vertices
    # Key values used to pick minimum weight edge in cut
    keys = [float('inf')] * vertices
    # To represent set of vertices included in MST
    mst_set = [False] * vertices

    # Always include the first vertex in MST
    keys[0] = 0
    parent[0] = -1

    for _ in range(vertices-1):
        # Pick the minimum key vertex from the set of vertices not yet included in MST
        u = min_key(vertices, keys, mst_set)
        # Add the picked vertex to the MST set
        mst_set[u] = True
        # Update key values and parent index of the adjacent vertices
        for v in range(vertices):
            if graph[u][v] > 0 and not mst_set[v] and graph[u][v] < keys[v]:
                keys[v] = graph[u][v]
                parent[v] = u

    print_mst(parent, graph)


# Read the number of vertices
vertices = int(input("Enter the number of vertices: "))

# Initialize an empty graph
graph = [[0] * vertices for _ in range(vertices)]

# Read the adjacency matrix of the graph
print("Enter the adjacency matrix:")
for i in range(vertices):
    for j in range(vertices):
        graph[i][j] = int(input())

# Call the Prim's MST function
prim_mst(graph)
