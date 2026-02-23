# Program to find the degree of all vertices in an undirected graph

n = int(input("Enter number of vertices: "))

graph = {}

for i in range(n):
    vertex = int(input(f"Enter vertex {i+1}: "))
    adj = list(map(int, input(f"Enter adjacent vertices of {vertex}: ").split()))
    graph[vertex] = adj

print("\nDegree of each vertex:")
for v in graph:
    print(f"Degree of vertex {v} =", len(graph[v]))
