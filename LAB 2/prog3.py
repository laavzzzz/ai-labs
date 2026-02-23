# Program 3: Find degree of all vertices in an undirected graph
# Supports both adjacency list and adjacency matrix

def degree_adj_list():
    n = int(input("Enter number of vertices: "))
    adj = [[] for _ in range(n)]

    print("Enter adjacency list (neighbours for each vertex):")
    for i in range(n):
        print(f"Enter neighbours of vertex {i} (space separated, empty for none):")
        line = input().strip()
        if line != "":
            neighbours = list(map(int, line.split()))
            adj[i] = neighbours

    print("\nDegree of each vertex (adjacency list):")
    for i in range(n):
        print(f"Degree of vertex {i} =", len(adj[i]))


def degree_adj_matrix():
    n = int(input("Enter number of vertices: "))
    adj = []

    print("Enter adjacency matrix:")
    for i in range(n):
        row = list(map(int, input().split()))
        adj.append(row)

    print("\nDegree of each vertex (adjacency matrix):")
    for i in range(n):
        degree = sum(adj[i])
        print(f"Degree of vertex {i} =", degree)


def main():
    print("Program 3: Degree of all vertices in an undirected graph")
    print("1. Using adjacency list")
    print("2. Using adjacency matrix")
    choice = int(input("Enter your choice (1 or 2): "))

    if choice == 1:
        degree_adj_list()
    elif choice == 2:
        degree_adj_matrix()
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
