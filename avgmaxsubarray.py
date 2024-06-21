#maximum average subarray
#sliding window approch
nums=[1,12,-5,-6,50,3]
k=4
cursum=sum(nums[:k])
maxsum=cursum
for i in range(1,len(nums)-k):
    cursum=cursum-nums[i-1]+nums[i+k-1]
    maxsum=max(maxsum,cursum)
print('maxaverage',maxsum/k)