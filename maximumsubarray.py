def maxsubarrsum(arr):
    maxsum=float('-inf')
    curr=0
    for i in arr:
        curr+=i
        maxsum=max(maxsum,curr)
        if curr<0:
            curr=0
    return maxsum
arr=[-1,2,3,10,-4,7,2,-5]
print(maxsubarrsum(arr))