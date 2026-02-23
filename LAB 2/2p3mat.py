# Program to find degree of all vertices using adjacency matrix

n = int(input("Enter number of vertices: "))
adj = []

print("Enter adjacency matrix:")
for i in range(n):
    row = list(map(int, input().split()))
    adj.append(row)

print("\nDegree of each vertex:")
for i in range(n):
    degree = sum(adj[i])
    print(f"Degree of vertex {i} =", degree)
