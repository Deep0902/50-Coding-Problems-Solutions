#longest substring without repeating characters
def withoutRepeating(str):
    visited = [False] * 128
    for ch in str:
        if visited[ord(ch)]:    #ord is get the ascii value
            return False
        else:
            visited[ord(ch)] = True
    return True

def longestSub(str):
    maxLength = 0
    for i in range(len(str)):
        for j in range(i,len(str)):
            substr = str[i:j+1]
            if withoutRepeating(substr) and len(substr) > maxLength:
                maxLength = len(substr)
    return maxLength

def longestSubM2(str):
    maxLength = 0
    start = 0
    indexes = [-1]*128
    for i in range(len(str)):
        if indexes[ord(str[i])] >= start:
            start = indexes[ord(str[i])]
        indexes[ord(str[i])] = i
        maxLength = max(maxLength, i-start+1)
    return maxLength - 1
#Driver code
str = "abccdefghijklmmnop"
ans = longestSubM2(str)
print(ans)