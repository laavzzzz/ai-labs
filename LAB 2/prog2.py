# Program 2: Check if two nodes are directly connected
# Supports both adjacency list and adjacency matrix

def check_direct_adj_list():
    n = int(input("Enter number of vertices: "))
    adj = [[] for _ in range(n)]

    print("Enter adjacency list (neighbours for each vertex):")
    for i in range(n):
        print(f"Enter neighbours of vertex {i} (space separated, empty for none):")
        line = input().strip()
        if line != "":
            neighbours = list(map(int, line.split()))
            adj[i] = neighbours

    u = int(input("Enter first node: "))
    v = int(input("Enter second node: "))

    if 0 <= u < n and 0 <= v < n and v in adj[u]:
        print("The nodes are directly connected (adjacency list).")
    else:
        print("The nodes are NOT directly connected (adjacency list).")


def check_direct_adj_matrix():
    n = int(input("Enter number of vertices: "))
    adj = []

    print("Enter adjacency matrix:")
    for i in range(n):
        row = list(map(int, input().split()))
        adj.append(row)

    u = int(input("Enter first node: "))
    v = int(input("Enter second node: "))

    if 0 <= u < n and 0 <= v < n and adj[u][v] == 1:
        print("The nodes are directly connected (adjacency matrix).")
    else:
        print("The nodes are NOT directly connected (adjacency matrix).")


def main():
    print("Program 2: Check if two nodes are directly connected")
    print("1. Using adjacency list")
    print("2. Using adjacency matrix")
    choice = int(input("Enter your choice (1 or 2): "))

    if choice == 1:
        check_direct_adj_list()
    elif choice == 2:
        check_direct_adj_matrix()
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
