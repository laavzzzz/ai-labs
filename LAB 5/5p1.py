from collections import deque

# Jug capacities
A = 4
B = 3

# All valid operations
def get_next_states(x, y):
    states = []

    # Fill A
    states.append((A, y))
    # Fill B
    states.append((x, B))

    # Empty A
    states.append((0, y))
    # Empty B
    states.append((x, 0))

    # Pour A → B
    transfer = min(x, B - y)
    states.append((x - transfer, y + transfer))

    # Pour B → A
    transfer = min(y, A - x)
    states.append((x + transfer, y - transfer))

    return states


def generate_state_space():
    visited = set()
    queue = deque()
    graph = {}

    start = (0, 0)
    queue.append(start)
    visited.add(start)

    while queue:
        state = queue.popleft()
        graph[state] = []

        for next_state in get_next_states(*state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append(next_state)
            graph[state].append(next_state)

    return graph


# Generate state space
graph = generate_state_space()

# Print state space diagram (Adjacency List)
print("STATE SPACE DIAGRAM (Adjacency List):\n")
for state in graph:
    print(state, "→", graph[state])
