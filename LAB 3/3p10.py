# 2D grid representation (1 = free cell, 0 = obstacle)
grid = [
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [0, 1, 1, 1],
    [1, 0, 1, 0]
]

rows = len(grid)
cols = len(grid[0])

# Check if a cell is inside grid boundary
def is_valid(r, c):
    return 0 <= r < rows and 0 <= c < cols

# Print valid neighbours (up, down, left, right)
def print_neighbours(r, c):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    print(f"Valid neighbours of cell ({r}, {c}):")

    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if is_valid(nr, nc):
            cell_type = "Free" if grid[nr][nc] == 1 else "Obstacle"
            print(f"({nr}, {nc}) -> {cell_type}")

# Count obstacles
obstacle_count = 0
for i in range(rows):
    for j in range(cols):
        if grid[i][j] == 0:
            obstacle_count += 1

# Display grid
print("Grid (1 = Free, 0 = Obstacle):")
for row in grid:
    print(row)

print("\nTotal number of obstacles:", obstacle_count)

# Example cell to check neighbours
row = 1
col = 1

if is_valid(row, col):
    print_neighbours(row, col)
else:
    print("Cell is outside grid boundary")
