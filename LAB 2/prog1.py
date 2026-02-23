# Program 1: Count number of edges in an undirected graph
# Supports both adjacency list and adjacency matrix

def count_edges_adj_list():
    n = int(input("Enter number of vertices: "))
    adj = [[] for _ in range(n)]

    print("Enter adjacency list (neighbours for each vertex):")
    for i in range(n):
        print(f"Enter neighbours of vertex {i} (space separated, empty for none):")
        line = input().strip()
        if line != "":
            neighbours = list(map(int, line.split()))
            adj[i] = neighbours

    edge_count = 0
    for i in range(n):
        edge_count += len(adj[i])

    edge_count = edge_count // 2      # undirected → each edge counted twice
    print("Number of edges (using adjacency list) =", edge_count)


def count_edges_adj_matrix():
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

    edge_count = edge_count // 2      # undirected → each edge appears twice
    print("Number of edges (using adjacency matrix) =", edge_count)


def main():
    print("Program 1: Count number of edges in an undirected graph")
    print("1. Using adjacency list")
    print("2. Using adjacency matrix")
    choice = int(input("Enter your choice (1 or 2): "))

    if choice == 1:
        count_edges_adj_list()
    elif choice == 2:
        count_edges_adj_matrix()
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
