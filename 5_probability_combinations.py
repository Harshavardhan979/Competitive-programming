LABSHEET5

k = int(input("Enter the value of k"))
r = int(input("Enter the value of r"))

def comb(val1 , val2):
    res = 1
    if val1-val2 < val2:
        val2 = val1-val1
    for i in range(1,val2+1):
        res = res * ((val1-i+1)/i)
    return res
a = comb(13,r)
b = comb(39,k-r)
c= comb(52,k)
probability = (a*b)/c

print(f"{probability:.6f}")



n = int(input("Enter the value of n"))
d = int(input("Enter the value of d"))
k = int(input("Enter the value of k"))
r = int(input("Enter the value of r"))

def comb(val1 , val2):
    res = 1
    if val1-val2 < val2:
        val2 = val1-val1
    for i in range(1,val2+1):
        res = res * ((val1-i+1)/i)
    return res
a = comb(d,r)
b = comb(n-d,k-r)
c= comb(n,k)
probability = (a*b)/c

print(f"{probability:.6f}")



