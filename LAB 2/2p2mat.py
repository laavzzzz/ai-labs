n = int(input("Enter number of vertices: "))
adj = []

print("Enter adjacency matrix:")
for i in range(n):
    row = list(map(int, input().split()))
    adj.append(row)

u = int(input("Enter first node: "))
v = int(input("Enter second node: "))

if adj[u][v] == 1:
    print("The nodes are directly connected.")
else:
    print("The nodes are NOT directly connected.")
