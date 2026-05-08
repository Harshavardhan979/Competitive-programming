# Labsheet 19 : LO1
# Find Shortest Distance using Dijkstra Algorithm

import heapq
from collections import defaultdict

# Input number of nodes and edges
n, e = map(int, input().split())

# Create graph
graph = defaultdict(list)

# Input weighted edges
for _ in range(e):
    u, v, w = map(int, input().split())

    graph[u].append((v, w))
    graph[v].append((u, w))

# Input source node
source = int(input())

# Initialize distances
distances = {i: float("inf") for i in range(n)}
distances[source] = 0

# Priority queue
pq = [(0, source)]

# Dijkstra Algorithm
while pq:
    current_dist, current_node = heapq.heappop(pq)

    if current_dist > distances[current_node]:
        continue

    for neighbor, weight in graph[current_node]:
        distance = current_dist + weight

        if distance < distances[neighbor]:
            distances[neighbor] = distance
            heapq.heappush(pq, (distance, neighbor))

# Print shortest distances
print(f"Shortest distances from source node {source}")

for node in range(n):
    print(f"{node} → {distances[node]}")


# Labsheet 19 : LO2
# Find Shortest Connection Cost between Two Nodes

# Input source and destination
source, destination = map(int, input().split())

# Reset distances
distances = {i: float("inf") for i in range(n)}
distances[source] = 0

# Priority queue
pq = [(0, source)]

path_found = False

# Dijkstra Algorithm
while pq:
    current_cost, current_user = heapq.heappop(pq)

    if current_user == destination:
        path_found = True
        break

    if current_cost > distances[current_user]:
        continue

    for neighbor, weight in graph[current_user]:
        cost = current_cost + weight

        if cost < distances[neighbor]:
            distances[neighbor] = cost
            heapq.heappush(pq, (cost, neighbor))

# Print result
if path_found:
    print(f"Shortest connection cost: {distances[destination]}")
else:
    print("No Connection Found")
