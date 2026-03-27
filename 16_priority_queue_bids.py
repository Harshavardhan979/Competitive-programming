
LABSHEET16


import heapq

n = int(input("Enter number of bids: "))
pq = []
for i in range(n):
    bid = int(input(f"Enter bid {i+1}: "))
    heapq.heappush(pq, -bid)   
highest_bid = -heapq.heappop(pq)
print("Highest bid amount:", highest_bid)
second_highest = -heapq.heappop(pq)
print("Second highest bid amount:", second_highest)



