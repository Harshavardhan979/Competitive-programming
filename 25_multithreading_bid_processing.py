# Labsheet 25 : LO1
# Find Highest Bid using Multithreading

import threading

# Global highest bid
highest_bid = 0

# Function to place bid
def place_bid(value):
    global highest_bid

    if value > highest_bid:
        highest_bid = value

# Input number of bids
n = int(input())

# Input bid values
bids = [int(input()) for _ in range(n)]

# Create threads
threads = []

for b in bids:
    t = threading.Thread(target=place_bid, args=(b,))

    threads.append(t)
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()

# Print highest bid
print(f"Highest Bid = {highest_bid}")


# Labsheet 25 : LO2
# Thread Safe Highest Bid Processing using Lock

import threading

# Global highest bid
highest_bid = 0

# Create lock
bid_lock = threading.Lock()

# Function to process bid safely
def process_bid(value):
    global highest_bid

    with bid_lock:
        if value > highest_bid:
            highest_bid = value

# Input number of bids
n = int(input())

# Input bid values
bids = [int(input()) for _ in range(n)]

# Create threads
threads = []

for val in bids:
    t = threading.Thread(target=process_bid, args=(val,))

    threads.append(t)
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()

# Print highest bid
print(f"Highest Bid = {highest_bid}")
