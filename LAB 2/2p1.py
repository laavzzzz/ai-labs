# Program to count number of edges in an undirected graph

n = int(input("Enter number of vertices: "))

graph = {}

for i in range(n):
    vertex = int(input(f"Enter vertex {i+1}: "))
    adj = list(map(int, input(f"Enter adjacent vertices of {vertex}: ").split()))
    graph[vertex] = adj

edge_count = 0

for v in graph:
    edge_count += len(graph[v])

edge_count = edge_count // 2

print("Number of edges in the undirected graph =", edge_count)
