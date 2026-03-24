LABSHEET2

numele = int(input("Enter number of elements"))
mod = int(input("Enter the modulo"))
arr = []
sum = 0
print("Enter the elements of array")
for i in range(0,numele):
    arr.append(int(input()))
for i in arr:
    sum = sum + i
print(sum%mod)



a = int(input("Enter number "))
m = int(input("Enter the power"))
p = int(input("Enter the modulo"))
res = 1
while m > 0:
    if m%2 != 0:
        res = (res*a)
        m=m-1
    else:
        a=a*a
        m = m/2
print(res%p)
    