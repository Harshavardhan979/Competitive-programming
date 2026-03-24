
LABSHEET3

n = int(input("Enter number of value"))
p = int(input("Enter the modulo number"))
sum = 0
res =1

for i in range(0,n):
    a = int(input("Enter the value of a"))
    m = int(input("Enter the value of m"))
    while m > 0:
        if m%2 != 0:
            res = (res*a)
            m=m-1
        else:
            a=a*a
            m = m/2

    sum = sum + res
    res = 1
print(sum%p)





a = int(input("Enter the value"))
b = int(input("Enter the value"))
p= int(input("Enter the modulo"))
k= int(input("Enter the value of k"))
pro = (a*b)%p
if pro % k == 0:
    print("Divisible")
else:
    print("Not Divisible")

