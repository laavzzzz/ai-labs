from collections import deque

def find_path_bfs(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    if not (0 <= start[0] < rows and 0 <= start[1] < cols and
            0 <= end[0] < rows and 0 <= end[1] < cols):
        print("Start or end coordinates are out of bounds.")
        return None

    if grid[start[0]][start[1]] == 0 or grid[end[0]][end[1]] == 0:
        print("Start or end position is on an obstacle.")
        return None

    queue = deque([([start])])  # Queue stores paths
    visited = {start}

    # Possible moves: up, down, left, right
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        path = queue.popleft()
        current_pos = path[-1]

        if current_pos == end:
            return path

        for move in moves:
            next_row, next_col = current_pos[0] + move[0], current_pos[1] + move[1]
            next_pos = (next_row, next_col)

            # Check if the next position is valid
            if (0 <= next_row < rows and
                    0 <= next_col < cols and
                    grid[next_row][next_col] == 1 and
                    next_pos not in visited):
                
                visited.add(next_pos)
                new_path = list(path)
                new_path.append(next_pos)
                queue.append(new_path)

    return None # No path found

def main():
    try:
        rows = int(input("Enter the number of rows for the grid: "))
        cols = int(input("Enter the number of columns for the grid: "))

        grid = []
        print("Enter the grid row by row (e.g., '1 0 1'):")
        for i in range(rows):
            while True:
                row_input = input(f"Row {i}: ").split()
                if len(row_input) == cols:
                    try:
                        grid.append([int(cell) for cell in row_input])
                        break
                    except ValueError:
                        print("Invalid input. Please enter only 0s and 1s.")
                else:
                    print(f"Please enter exactly {cols} values separated by spaces.")

        start_row = int(input("Enter the starting row: "))
        start_col = int(input("Enter the starting column: "))
        end_row = int(input("Enter the destination row: "))
        end_col = int(input("Enter the destination column: "))

        start_pos = (start_row, start_col)
        end_pos = (end_row, end_col)

        print("\nGrid:")
        for row in grid:
            print(" ".join(map(str, row)))
        
        print(f"\nSearching for a path from {start_pos} to {end_pos}...")
        
        path = find_path_bfs(grid, start_pos, end_pos)

        if path:
            print("\nPath found!")
            print(" -> ".join(map(str, path)))
            
            # Create a visual representation of the path
            path_grid = [list(row) for row in grid]
            for r, c in path:
                if (r, c) == start_pos:
                    path_grid[r][c] = 'S'
                elif (r, c) == end_pos:
                    path_grid[r][c] = 'E'
                else:
                    path_grid[r][c] = '*'
            
            print("\nPath Visualization:")
            for row in path_grid:
                print(" ".join(map(str, row)))

        else:
            print("\nNo path found from start to destination.")

    except ValueError:
        print("\nInvalid input. Please enter valid integers for rows, columns, and coordinates.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()