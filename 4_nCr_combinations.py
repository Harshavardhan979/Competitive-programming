
LABSHEET4
n = int(input())
k = int(input())
nk = n-k
def factorial(val):
    fact = 1
    if n == 0:
        fact = 1
    else:
        for i in range(1,val+1):
            fact = fact * i
    return fact
nfact = factorial(n)
kfact = factorial(k)
nkfact = factorial(nk)
print(nfact/(kfact*nkfact))


n = int(input())
k = int(input())
res = 1
if n-k < k:
    k = n-k
for i in range(1,k+1):
    res = res * ((n-i+1)/i)
print(res)

