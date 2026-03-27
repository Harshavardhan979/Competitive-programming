
labsheet15


text = input("Enter Text: ")
pat = input("Enter Pattern: ")

m = len(pat)
n = len(text)


lps = [0] * m
length = 0
i = 1
while i < m:
    if pat[i] == pat[length]:
        length += 1
        lps[i] = length
        i += 1
    else:
        if length != 0:
            length = lps[length - 1]
        else:
            lps[i] = 0
            i += 1


i = 0  
j = 0  
found = False
while i < n:
    if text[i] == pat[j]:
        i += 1
        j += 1

    if j == m:
        print(i - j)
        j = lps[j - 1]
        found = True
    elif i < n and text[i] != pat[j]:
        if j != 0:
            j = lps[j - 1]
        else:
            i += 1

if not found:
    print("Pattern Not Found")

