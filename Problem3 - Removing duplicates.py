#Removing duplicates
#own
def removeDuplicates(arr):
    sortedArr = []
    visited = {}
    for i in range(len(arr)):
        if visited.get(arr[i]):
            continue
        else:
            sortedArr.append(arr[i])
            visited[arr[i]] = True
    return sortedArr
#Method 1
def removeDuplicatesM1(arr):
    newArr = []
    for i in arr:
        if i not in newArr:
            newArr.append(i)
    return newArr
#method 2
def removeDuplicatesM2(arr):
    newArr = [arr[0]]
    arr.sort()
    for i in range(1, len(arr)):
        if arr[i]!=arr[i-1]:
            newArr.append(arr[i])
    return newArr

#method best
def removeDuplicatesM3(arr):
    visited = {}
    for i in arr:
        visited[i] = True
    return list(visited.keys())


arr = [1,6,3,8,2,6,6,6]
ARR = removeDuplicatesM3(arr)
print(ARR)