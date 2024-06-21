#printing the maximum subarray of maximum sum
#sliding window approch
num=[2,4,3,5,6,3,4,6,7,1,2,5]
k=3
currsum=sum(num[:k])
maxsum=currsum
maxarry=num[:k]
for i in range(1,len(num)-k):
    currsum=currsum+num[i+k-1]-num[i-1]
    if currsum>maxsum:
        maxsum=currsum
        maxarry=num[i:i+k]
print(maxsum)
print(maxarry)
