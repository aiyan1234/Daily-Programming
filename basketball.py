'''Basketball 
You are competing in a basketball .in this contest the score for each successful shot depends on both 
the distance from the basket and position. The ball is shot N times, successfully. You are given an 
array A containing the distance of a player from basket for N shots. The index of array represents 
the position of the player. Score is calculated by multiplying the position with the distance from the 
basket. 
Your task is to find and return an integer value, representing the maximum possible score you can 
achieve by choosing a contiguous subarray of size & from the given array 
Note:A subarray is a contiguous part of array 
Assume 1 based indexing. 
The array contains both negative and positive values. 
Assume the player is standing on a cartesian plane 
Input Format
Input: An Integer value representing the number of shots made by the player 
Input: As Integer & representing the size of subarray 
Input: An array of integers'''

n=int(input("no of shots"))
k=int(input("size of subarray"))
arr=list(map(int,input().strip().split()))
max_s=float('-inf')
for i in range(0,n-k+1):
    sub_arr=arr[i:i+k]
    pos=1
    s=0
    for j in sub_arr:
        s+=j*pos
        pos+=1
    if s>max_s:
        max_s=s
print(max_s)
    