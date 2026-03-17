import random
import pandas as pd

# Objective function
def f(x):
    return x**2

# Initial population (1 to 31)
population = list(range(1, 32))

results = []

# Tournament Selection
def tournament(pop):
    a, b = random.sample(pop, 2)
    return a if f(a) > f(b) else b

for i in range(10):   # number of iterations
    x = random.choice(population)
    fx = f(x)

    # Tournament Selection
    ts = tournament(population)

    # Crossover (average of two parents)
    parent2 = random.choice(population)
    co = (ts + parent2) // 2

    # Mutation (small random change)
    mutation = co + random.choice([-1, 0, 1])
    mutation = max(1, min(31, mutation))  # keep in range

    results.append([x, fx, ts, co, mutation])

# Create table
df = pd.DataFrame(results, columns=["x", "f(x)", "TS", "CO", "Mutation"])

print(df)

# Best solution
best_x = max(population, key=f)
print("\nBest Solution:")
print("x =", best_x)
print("f(x) =", f(best_x))