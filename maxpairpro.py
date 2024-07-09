'''Maximize Pair Product 
Noah is given an integer array A of length N. He must perform the following operations: 
• Select any Integer pair having sum equal to 18 from the array. 
• Select the pair with maximum product such that the first element of the pair is greater than the 
second element of the pair. 
• Your task is to help Noah find and return a pair in the form of an integer array, which satisfies the 
mentioned conditions. 
Input Specification: 
Input1: An Integer value N, representing the size of array A. 
Input2: An integer array A. 
Output Specification: 
Return a pair in the form of an integer array, which satisfies the mentioned'''

n = int(input("Enter the size: "))
arr = list(map(int, input().split()))
m_p = -999
h = 0
k = 0

for i in range(n):
    for j in range(i + 1, n):
        if arr[i] + arr[j] == 18 and arr[i] > arr[j]:
            p = arr[i] * arr[j]
            if p > m_p:
                m_p = p
                h = arr[i]
                k = arr[j]

if m_p != -999:
    print([h, k])
else:
    print("No valid pair found")