import heapq

def best_first_search(grid, start, goal):

    rows, cols = len(grid), len(grid[0])
    
    def manhattan_distance(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    # Priority queue to store cells to visit, prioritized by heuristic
    # (heuristic, current_path)
    open_list = [(manhattan_distance(start, goal), [start])]
    heapq.heapify(open_list)
    
    # Set to keep track of visited cells
    visited = {start}

    while open_list:
        _, path = heapq.heappop(open_list)
        current_cell = path[-1]

        if current_cell == goal:
            return path  # Treasure found

        r, c = current_cell
        
        # Explore neighbors
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc

            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                visited.add((nr, nc))
                new_path = path + [(nr, nc)]
                heuristic_value = manhattan_distance((nr, nc), goal)
                heapq.heappush(open_list, (heuristic_value, new_path))
    
    return None # Treasure not found

def print_grid_with_path(grid, path):
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if (r, c) in path:
                print("*", end=" ")
            else:
                print(cell, end=" ")
        print()

if __name__ == "__main__":
    # Define the grid, start, and goal
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 2]
    ]
    start_pos = tuple(map(int, input("Enter start position (row,col): ").split(',')))
    goal_pos = tuple(map(int, input("Enter goal position (row,col): ").split(',')))
    
    # Find the path
    path = best_first_search(grid, start_pos, goal_pos)

    if path:
        print("Treasure found! Path:")
        print_grid_with_path(grid, path)
        print("\nPath coordinates:", path)
    else:
        print("Treasure not found.")


