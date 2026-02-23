from collections import deque

def three_jug_problem():
    capacities = (12, 7.5, 4.5)
    start = (12, 0, 0)

    visited = set()
    queue = deque([(start, [])])

    while queue:
        state, path = queue.popleft()

        if 6 in state:
            return path + [state]

        if state in visited:
            continue
        visited.add(state)

        for i in range(3):
            for j in range(3):
                if i != j and state[i] > 0 and state[j] < capacities[j]:
                    amount = min(state[i], capacities[j] - state[j])
                    new_state = list(state)
                    new_state[i] -= amount
                    new_state[j] += amount
                    queue.append((tuple(new_state), path + [state]))

result = three_jug_problem()
print(result)
