#Finding the duplicate
#Method 1
def findDuplicateM1(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                return arr[i]
    
#Method 2
def findDuplicateM2(arr):
    arr.sort()
    for i in range(len(arr)):
        if arr[i] == arr[i+1]:
            return arr[i]

#Method 3
def findDuplicateM3(arr):
    visited = {}
    for i in range(len(arr)):
        if visited.get(arr[i]):
            return arr[i]
        else:
            visited[arr[i]] = True

#Method 4 tortoise and hare method
def findDuplicateM4(arr):
    tortoise = arr[0]
    hare = arr[arr[0]]
    while(tortoise != hare):
        tortoise = arr[tortoise]
        hare = arr[arr[hare]]
    tortoise = 0
    while tortoise != hare:
        tortoise = arr[tortoise]
        hare = arr[hare]
    return tortoise

arr = [1,3,7,2,7,9,3]
ans = findDuplicateM3(arr)
print(ans)