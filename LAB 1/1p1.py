# Taking number of vertices from user
V = int(input("Enter number of vertices: "))

# Taking number of edges from user
E = int(input("Enter number of edges: "))

# Creating adjacency matrix filled with 0
adjmatrix = [[0] * V for _ in range(V)]

# Creating empty adjacency list
adjlist = {i: [] for i in range(V)}

# Taking edge inputs
print("Enter edges:")
for i in range(E):
    u, v = map(int, input().split())

    adjmatrix[u][v] = 1
    adjmatrix[v][u] = 1

    adjlist[u].append(v)
    adjlist[v].append(u)

# Printing adjacency matrix
print("\nAdjacency Matrix:")
for row in adjmatrix:
    print(row)

# Printing adjacency list
print("\nAdjacency List:")
for key in adjlist:
    print(key, "->", adjlist[key])
