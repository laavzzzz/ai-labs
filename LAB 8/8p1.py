import heapq
from collections import defaultdict

GOAL = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

MOVES = {
    0: [1, 3],
    1: [0, 2, 4],
    2: [1, 5],
    3: [0, 4, 6],
    4: [1, 3, 5, 7],
    5: [2, 4, 8],
    6: [3, 7],
    7: [4, 6, 8],
    8: [5, 7]
}


# ---------- Heuristics ----------

def h1_misplaced(state):
    return sum(1 for i in range(9) if state[i] != 0 and state[i] != GOAL[i])


def h2_manhattan(state):
    dist = 0
    for i in range(9):
        tile = state[i]
        if tile == 0:
            continue
        goal_pos = GOAL.index(tile)
        dist += abs(i // 3 - goal_pos // 3) + abs(i % 3 - goal_pos % 3)
    return dist


# ---------- A* Search ----------

def astar(start, heuristic):
    pq = []
    heapq.heappush(pq, (heuristic(start), 0, start))
    
    visited = set()
    g_cost = {start: 0}

    nodes_expanded = 0

    while pq:
        f, g, state = heapq.heappop(pq)

        if state == GOAL:
            return g, nodes_expanded

        if state in visited:
            continue

        visited.add(state)
        nodes_expanded += 1

        zero = state.index(0)

        for move in MOVES[zero]:
            new_state = list(state)
            new_state[zero], new_state[move] = new_state[move], new_state[zero]
            new_state = tuple(new_state)

            new_g = g + 1

            if new_state not in g_cost or new_g < g_cost[new_state]:
                g_cost[new_state] = new_g
                f_cost = new_g + heuristic(new_state)
                heapq.heappush(pq, (f_cost, new_g, new_state))

    return None, None


# ---------- Run Comparison ----------

if __name__ == "__main__":

    # Example start state (change this)
    start = (1, 2, 3,
             4, 0, 6,
             7, 5, 8)

    depth1, nodes1 = astar(start, h1_misplaced)
    depth2, nodes2 = astar(start, h2_manhattan)

    print("A* with H1 (Misplaced Tiles)")
    print("Solution depth:", depth1)
    print("Nodes expanded:", nodes1)

    print("\nA* with H2 (Manhattan Distance)")
    print("Solution depth:", depth2)
    print("Nodes expanded:", nodes2)

    print("\nPerformance Comparison:")
    print(f"H1 expanded {nodes1} nodes")
    print(f"H2 expanded {nodes2} nodes")
    print("Manhattan is better (always ≤ nodes in practice)")