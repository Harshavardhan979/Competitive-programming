# Labsheet 23 : LO1
# Shopping Cart with Item Discounts

# Input number of cart items
n = int(input())

# Store cart items
cart_items = []

for _ in range(n):
    name, price = input().split()

    cart_items.append([name, int(price)])

# Input number of discounts
d = int(input())

# Store discounts
discounts = {}

for _ in range(d):
    name, pct = input().split()

    discounts[name] = int(pct)

# Calculate total price
total_price = 0

for name, price in cart_items:
    discount_pct = discounts.get(name, 0)

    final_price = price * (1 - discount_pct / 100)

    total_price += final_price

    print(f"{name} {int(final_price)}")

# Print total price
print(f"Total Price = {int(total_price)}")


# Labsheet 23 : LO2
# Shopping Cart with Discounts and Coupon

# Input number of cart items
n = int(input())

# Store cart items
cart_items = []

for _ in range(n):
    name, price = input().split()

    cart_items.append([name, int(price)])

# Input number of discounts
d = int(input())

# Store discounts
discounts = {}

for _ in range(d):
    name, pct = input().split()

    discounts[name] = int(pct)

# Input coupon value and threshold
coupon_val, threshold = map(int, input().split())

# Calculate price after item discounts
total_after_discount = 0

for name, price in cart_items:
    discount_pct = discounts.get(name, 0)

    item_final = price * (1 - discount_pct / 100)

    total_after_discount += item_final

    print(f"{name} {int(item_final)}")

# Print discounted price
print(f"Price After Discount = {int(total_after_discount)}")

# Apply coupon if eligible
final_price = total_after_discount

if total_after_discount >= threshold:
    final_price -= coupon_val

# Print final cart price
print(f"Final Cart Price = {int(final_price)}")
