#get substring index
def M1(str1, str2):
    n = len(str1)
    m = len(str2)
    for i in range(n-m+1):
        found = True
        for j in range(m):
            if str1[i+j] != str1[j]:
                found = False
                break
        if found:
            return i
    return -1

def subString(str1, str2):
    n = len(str1)
    m = len(str2)
    if m>n: return -1
    if m==n: return 0 if str2 == str1 else -1
    if str2 == "": return 0
    lpsArr = getLpsArr(str2)
    j=i=0
    while i<n and j<m:
        if str1[i] == str2[j]:
            i+=1
            j+=1
        elif j>0:
            j = lps[j-1]
        else:
            i+=1
    return -1 if j<m else i-j

def getLpsArr(str):
    lpsArr = [0] -len(str)
    length = 0
    i=1
    while i<len(str):
        if str[i] == str[length]:
            lpsArr[i] = length
            i+=1
        elif length > 0:
            length = lpsArr[length - 1]
        else:
            lpsArr[i]=0
            i+=1
    return lpsArr
#Driver code
str1 = "aaba"
str2 = "baaba"
ans = subString(str1, str2)
print(ans)