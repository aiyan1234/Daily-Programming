nums = [-1,2,3,10,-4,7,2,-5]
k=4
currsum=sum(nums[:k])
maxsub=nums[:k]
maxsum=float('-inf')
for i in range(k,len(nums)):
    currsum+=nums[i]-nums[i-k]
    if currsum>maxsum:
        maxsum=currsum
        maxsub=nums[i-k+1:i+1]
print(maxsum)
print(maxsub)