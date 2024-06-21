
#kadne algorithm for max sum of subarray
num=[-2,4,3,5,-6,3,4,6,-7,1,2,5]
currsum=0
maxsum=float('-inf')
for i in num:
    currsum=currsum+i
    maxsum=max(currsum,maxsum)
    if currsum<0:
        currsum=0
print(maxsum)