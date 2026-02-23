class WaterJugState:
    def __init__(self, x, y):
        self.x = x  # water in jug A
        self.y = y  # water in jug B

    def __str__(self):
        return f"({self.x}, {self.y})"

initial_state = WaterJugState(0, 0)
goal_state = WaterJugState(0, 4)

print("Initial State:", initial_state)
print("Goal State:", goal_state)
print("Actions: Fill, Empty, Pour")
