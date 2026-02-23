# Program to count number of edges in an undirected graph using adjacency matrix

n = int(input("Enter number of vertices: "))

adj = []

print("Enter adjacency matrix:")
for i in range(n):
    row = list(map(int, input().split()))
    adj.append(row)

edge_count = 0

for i in range(n):
    for j in range(n):
        if adj[i][j] == 1:
            edge_count += 1

edge_count = edge_count // 2   # divide by 2 for undirected graph

print("Number of edges in the undirected graph =", edge_count)
