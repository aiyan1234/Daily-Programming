#making the sum as given value and which give max pro
n=int(input("enter the size"))
arr=list(map(int,input().split()))
m_p=-999
h=0
k=0
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]+arr[j]==18:
            p=arr[i]*arr[j]
            if p>m_p:
                m_p=p
            h=arr[i]
            k=arr[j]
print(h)
print(k)
