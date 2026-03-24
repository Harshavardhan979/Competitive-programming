
LABSHEET1
totalamount = float(input("Enter Total amount"))
if totalamount < 1000 :
    print(f"No discount applied your toatal amount is {totalamount}")
elif totalamount >= 1000 and totalamount <5000:
    totalamount = totalamount - (totalamount * 0.1)
    print(f"Your toatal amount after applying discount is: {totalamount} ")
elif totalamount >= 5000 and totalamount <10000:
    totalamount = totalamount - (totalamount * 0.2)
    print(f"Your toatal amount after applying discount is: {totalamount} ")
else:
    totalamount = totalamount - (totalamount * 0.25) - 500
    print(f"Your toatal amount after applying discount is: {totalamount} ")




numofitems = int(input("Enter the number of items"))
total_amount = 0
for i in range(0,numofitems):
    item = float(input("enter item price"))
    discount = float(input("enter item discount"))
    discount = discount/100
    discount_price = item - item*discount
    total_amount = total_amount + discount_price
if total_amount > 500 and total_amount < 1000 :
    total_amount = total_amount - (total_amount * 0.1)  
elif total_amount >= 1000 :
    total_amount = total_amount - 150

print(f"Your toatal amount is {total_amount}")
