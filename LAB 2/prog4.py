# Program 4: Check whether a given sequence is a valid path
# and find its length (number of edges)
# Supports both adjacency list and adjacency matrix

def path_adj_list():
    n = int(input("Enter number of vertices: "))
    adj = [[] for _ in range(n)]

    print("Enter adjacency list (neighbours for each vertex):")
    for i in range(n):
        print(f"Enter neighbours of vertex {i} (space separated, empty for none):")
        line = input().strip()
        if line != "":
            neighbours = list(map(int, line.split()))
            adj[i] = neighbours

    k = int(input("Enter number of nodes in the given sequence: "))
    path = list(map(int, input("Enter the sequence of nodes: ").split()))

    if len(path) != k:
        print("Invalid input: sequence length mismatch")
        return

    exists = True
    length = 0

    for i in range(k - 1):
        u = path[i]
        v = path[i + 1]

        if not (0 <= u < n and 0 <= v < n):
            exists = False
            break

        if v not in adj[u]:
            exists = False
            break
        else:
            length += 1

    if exists:
        print("Yes, the given sequence is a valid path (adjacency list).")
        print("Length of the path =", length)
    else:
        print("No, the given sequence is NOT a valid path (adjacency list).")


def path_adj_matrix():
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
        return

    exists = True
    length = 0

    for i in range(k - 1):
        u = path[i]
        v = path[i + 1]

        if not (0 <= u < n and 0 <= v < n):
            exists = False
            break

        if adj[u][v] == 0:
            exists = False
            break
        else:
            length += 1

    if exists:
        print("Yes, the given sequence is a valid path (adjacency matrix).")
        print("Length of the path =", length)
    else:
        print("No, the given sequence is NOT a valid path (adjacency matrix).")


def main():
    print("Program 4: Check given sequence is a valid path and find its length")
    print("1. Using adjacency list")
    print("2. Using adjacency matrix")
    choice = int(input("Enter your choice (1 or 2): "))

    if choice == 1:
        path_adj_list()
    elif choice == 2:
        path_adj_matrix()
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
