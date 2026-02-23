# Program to find number of misplaced tiles in 3x3 puzzle

print("Enter initial state:")
initial = []
for i in range(3):
    row = list(map(int, input().split()))
    initial.append(row)

print("Enter goal state:")
goal = []
for i in range(3):
    row = list(map(int, input().split())) #makes each string into int
    goal.append(row)

misplaced = 0

for i in range(3):
    for j in range(3):
        if initial[i][j] != 0 and initial[i][j] != goal[i][j]:
            misplaced += 1

print("Number of misplaced tiles:", misplaced)
