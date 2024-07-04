arr=[4111,9,345,1,4,64444,3]
count=[0]*(max(arr)+1)
for i in arr:
    count[i]+=1
j=0
for i in range(len(count)):
    while count[i]>0:
        arr[j]=i
        j=j+1
        count[i]-=1

print(arr)
