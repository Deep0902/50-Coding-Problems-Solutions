#First repeating char

#method 1

def firstRepeating(str):
    for i in range(len(str)):
        for j in range(i):
            if str[i] == str [j]:
                return(str[i])
    return ("Not found")

#method 2
def firstRepeatingHash(str):
    visited = {}
    for ch in str:
        if visited.get(ch):
            return ch
        else:
            visited[ch] = True
    return "Not Found"

str = "abcdefghijkl"
ans = firstRepeatingHash(str)
print(ans)