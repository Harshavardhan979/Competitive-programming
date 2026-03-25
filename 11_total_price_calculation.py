

LABSHEET11


prices = []
total_sum = 0
n = int(input("Enter the number of items"))
for i in range(0,n):
    a = int(input("Enter the prices"))
    prices.append(a)
for i in prices:
    total_sum = total_sum +i
print(prices)
print(total_sum)


prices = {}
total_sum = 0
n = int(input("Enter the number of items"))

for i in range(0,n):
    price = int(input("Enter the price of items"))
    quantity = int(input("enter the quantity"))
    prices[price]=quantity
for i in prices:
    total_sum = total_sum + (i*prices[i])
print(total_sum)


