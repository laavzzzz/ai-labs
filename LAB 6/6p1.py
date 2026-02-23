import heapq
import math

def uniform_cost_search(adj_matrix, start, goal):
    n = len(adj_matrix)
    pq = [(0, start)]          # (cost, node)
    dist = [math.inf] * n
    dist[start] = 0
    parent = [-1] * n
    visited = set()

    while pq:
        cost, node = heapq.heappop(pq)

        if node in visited:
            continue
        visited.add(node)

        if node == goal:
            break

        for neighbor in range(n):
            weight = adj_matrix[node][neighbor]
            if weight > 0 and neighbor not in visited:
                new_cost = cost + weight
                if new_cost < dist[neighbor]:
                    dist[neighbor] = new_cost
                    parent[neighbor] = node
                    heapq.heappush(pq, (new_cost, neighbor))

    path = []
    if dist[goal] != math.inf:
        cur = goal
        while cur != -1:
            path.append(cur)
            cur = parent[cur]
        path.reverse()

    return path, dist[goal]


# -------- MAIN PROGRAM --------

n = int(input("Enter number of nodes: "))

print("Enter adjacency matrix (0 for no edge):")
adj_matrix = []
for _ in range(n):
    adj_matrix.append(list(map(int, input().split())))

start = int(input("Enter start node: "))
goal = int(input("Enter goal node: "))

path, cost = uniform_cost_search(adj_matrix, start, goal)

if cost == math.inf:
    print("No path found")
else:
    print("Shortest Path:", path)
    print("Total Cost:", cost)
