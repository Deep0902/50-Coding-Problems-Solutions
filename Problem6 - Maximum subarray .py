#Maximum subarray 
#Method 1
def maxSubArrayM1(arr):
    maxSum = -9999
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            actualSum = 0
            for k in range(i,j):
                actualSum = actualSum + arr[k]
            maxSum = max(maxSum, actualSum)
    return maxSum

#Method 2
def maxSubArrayM2(arr):
    maxSum = -9999
    for i in range(len(arr)):
        cumulativeSum = 0
        for j in range(i, len(arr)):
            cumulativeSum = cumulativeSum + arr[j]
        maxSum = max(maxSum, cumulativeSum)
    return maxSum

#Method 3
def maxSubArrayM3(arr):
    globalSum = -9999
    localSum = 0
    for i in range(len(arr)):
        localSum = max(arr[i], localSum + arr[i])
        globalSum = max(localSum, globalSum)
        print("\nlocal = "+str(localSum)+" global = "+str(globalSum))
    return globalSum

arr = [1,-6,5,-44,4]
ans = maxSubArrayM3(arr)
print(ans)