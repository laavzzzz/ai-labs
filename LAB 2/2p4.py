# Program to check whether a given sequence is a valid path
# and find its length using adjacency list

n = int(input("Enter number of vertices: "))

graph = {}

for i in range(n):
    v = int(input(f"Enter vertex {i + 1}: "))
    adj = list(map(int, input(f"Enter adjacent vertices of {v}: ").split()))
    graph[v] = adj

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

        if v not in graph[u]:
            exists = False
            break
        else:
            length += 1

    if exists:
        print("Yes, the given sequence is a valid path.")
        print("Length of the path =", length)
    else:
        print("No, the given sequence is NOT a valid path.")
