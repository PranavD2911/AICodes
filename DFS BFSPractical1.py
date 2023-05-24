class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj_list = [[] for _ in range(self.V)]
        
    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)
        
    def DFS(self, v, visited):
        visited[v] = True
        print(v, end=' ')
        
        for neighbor in self.adj_list[v]:
            if not visited[neighbor]:
                self.DFS(neighbor, visited)
                
    def DFS_main(self, start):
        visited = [False] * self.V
        self.DFS(start, visited)


# Example usage
vertices = int(input("Enter the number of vertices in the graph: "))
g = Graph(vertices)

edges = int(input("Enter the number of edges in the graph: "))
print("Enter the edges in the format 'u v' (space-separated):")
for _ in range(edges):
    u, v = map(int, input().split())
    g.add_edge(u, v)

start_vertex = int(input("Enter the starting vertex for DFS traversal: "))
print("DFS traversal:")
g.DFS_main(start_vertex)

#******************************************************************************************

from collections import deque

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj_list = [[] for _ in range(self.V)]
        
    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)
        
    def BFS(self, start):
        visited = [False] * self.V
        queue = deque()
        queue.append(start)
        visited[start] = True
        
        while queue:
            vertex = queue.popleft()
            print(vertex, end=' ')
            
            for neighbor in self.adj_list[vertex]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True

# Example usage
vertices = int(input("Enter the number of vertices in the graph: "))
g = Graph(vertices)

edges = int(input("Enter the number of edges in the graph: "))
print("Enter the edges in the format 'u v' (space-separated):")
for _ in range(edges):
    u, v = map(int, input().split())
    g.add_edge(u, v)

start_vertex = int(input("Enter the starting vertex for BFS traversal: "))
print("BFS traversal:")
g.BFS(start_vertex)
