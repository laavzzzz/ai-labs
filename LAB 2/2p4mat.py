# Program to check whether a given sequence is a valid path
# and find its length using adjacency matrix

n = int(input("Enter number of vertices: "))

adj = []

print("Enter adjacency matrix:")
for i in range(n):
    row = list(map(int, input().split()))
    adj.append(row)

k = int(input("Enter number of nodes in the given sequence: "))
path = list(map(int, input("Enter the sequence of nodes: ").split()))

if len(path) != k:
    print("Invalid input: sequence length mismatch")
else:
    exists = True
    length = 0

    for i in range(k - 1):
        u = path[i]
        v = path[i + 1]

        if adj[u][v] == 0:
            exists = False
            break
        else:
            length += 1

    if exists:
        print("Yes, the given sequence is a valid path.")
        print("Length of the path =", length)
    else:
        print("No, the given sequence is NOT a valid path.")
