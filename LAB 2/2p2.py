# Program to check if two nodes are directly connected

n = int(input("Enter number of vertices: "))

graph = {}

for i in range(n):
    vertex = int(input(f"Enter vertex {i+1}: "))
    adj = list(map(int, input(f"Enter adjacent vertices of {vertex}: ").split()))
    graph[vertex] = adj

u = int(input("Enter first node: "))
v = int(input("Enter second node: "))

if u in graph and v in graph[u]:
    print("The nodes are directly connected.")
else:
    print("The nodes are NOT directly connected.")
