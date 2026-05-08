# Labsheet 24 : LO1
# Minimum Moves to Reach Target Position using BFS

from collections import deque

# Input board size
n = int(input())

# Input starting position
start = tuple(map(int, input().split()))

# Input target position
target = tuple(map(int, input().split()))

# If start and target are same
if start == target:
    print(0)

else:
    # Queue stores position and distance
    queue = deque([(start, 0)])

    # Visited positions
    visited = {start}

    # BFS Traversal
    while queue:
        (r, c), dist = queue.popleft()

        # If target reached
        if (r, c) == target:
            print(dist)
            break

        # Possible directions
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for dr, dc in directions:
            for step in range(1, n):

                nr = r + dr * step
                nc = c + dc * step

                if 0 <= nr < n and 0 <= nc < n:

                    if (nr, nc) == target:
                        print(dist + 1)
                        exit()

                    if (nr, nc) not in visited:
                        visited.add((nr, nc))
                        queue.append(((nr, nc), dist + 1))

                else:
                    break


# Labsheet 24 : LO2
# Find All Reachable Squares on Chessboard

# Input board size
n = int(input())

# Input current position
r, c = map(int, input().split())

# Store reachable positions
reachable = []

# Possible directions
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# Find reachable squares
for dr, dc in directions:
    for step in range(1, n):

        nr = r + dr * step
        nc = c + dc * step

        if 0 <= nr < n and 0 <= nc < n:
            reachable.append(f"{nr} {nc}")

        else:
            break

# Print reachable squares
print("Reachable Squares")

for pos in reachable:
    print(pos)
