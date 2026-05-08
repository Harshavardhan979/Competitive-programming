# Labsheet 18 : LO1
# Graph Representation using Adjacency Matrix and Adjacency List

from collections import defaultdict

# Input number of nodes and edges
n, e = map(int, input().split())

# Create adjacency matrix
matrix = [[0] * n for _ in range(n)]

# Create adjacency list
adj_list = defaultdict(list)

# Input edges
for _ in range(e):
    u, v = map(int, input().split())

    matrix[u][v] = 1
    matrix[v][u] = 1

    adj_list[u].append(v)
    adj_list[v].append(u)

# Print adjacency matrix
print("Adjacency Matrix")
for row in matrix:
    print(*(row))

# Print adjacency list
print("Adjacency List")
for node in range(n):
    neighbors = " ".join(map(str, sorted(adj_list[node])))
    print(f"{node} → {neighbors}")


# Labsheet 18 : LO2
# Check Path Existence in Graph using DFS

# Input source and destination
source, destination = map(int, input().split())

visited = set()

# DFS function to check path
def has_path(node):
    if node == destination:
        return True

    visited.add(node)

    for neighbor in adj_list[node]:
        if neighbor not in visited:
            if has_path(neighbor):
                return True

    return False

# Print result
if has_path(source):
    print("Path Exists")
else:
    print("No Path Exists")
