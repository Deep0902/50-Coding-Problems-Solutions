#peak finding problem
def peakFinding(arr):
    maxValue = -9999
    index = -1
    for i in range(len(arr)):
        if i == 0:
            if (arr[i] >= arr[i+1] and arr[i] > maxValue):
                maxValue = arr[i]
                index = i
        elif i == len(arr)-2:
            if (arr[i] > arr[i+1] and arr[i] > maxValue):
                maxValue = arr[i]
                index = i
        
    return maxValue

#Method 1
def peakFindingM2(arr):
    newArr = arr
    newArr.sort()
    s = len(arr)
    return newArr[s-1]

def peakFindingM3(arr, left, right):
    if left >= right:
        return int(left)
    mid = (left + right)/2
    if(arr[mid] < arr[mid+1]):
        return peakFindingM3(arr, mid + 1, right)
    else:
        return peakFindingM3(arr, left, mid)
        
def M3(arr):
    return peakFindingM3(arr, 0, len(arr)-1)

def M4(arr):
    return max(arr) 
#Driver code
arr = [1,4,6,7,3,9,8]
ans = M4(arr)
print(ans)