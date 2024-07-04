#taking an array of distance multiplying with its position to form score array and finding the max sum


n=int(input("no of shots"))
k=int(input("size of subarray"))
arr_distance=list(map(int,input().strip().split()))
scores=[(i+1)*arr_distance[i] for i in range(len(arr_distance))]
print(scores)
curr_s=sum(scores[:k])
max_s=curr_s
for i in range(1,n-k+1):
    curr_s=curr_s+scores[i+k-1]-scores[i-1]
    max_s=max(curr_s,max_s)
print(max_s)