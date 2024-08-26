'''Problem Statement:
You are required to input the size of the matrix then the elements of matrix, then you have to divide the main matrix in two sub matrices (even and odd)
in such a way that element at 0 index will be considered as even and element at 1st index will be considered as odd and so on.
Then you have sort the even and odd matrices in ascending order then print the sum of second largest number from both the matrices.
Example:
enter the size of array : 5
enter element at 0 index : 3
enter element at 1 index : 4
enter element at 2 index : 1
enter element at 3 index : 7
enter element at 4 index : 9
Sorted even array : 1 3 9
Sorted odd array : 4 7
7'''
arr=list(map(int,input().split()))
evn=[]
odd=[]
for i in range(len(arr)):
    if i%2==0:
        evn.append(arr[i])
    else:
        odd.append(arr[i])
evn.sort()
odd.sort()
print(evn)
print(odd)
print(evn[-2]+odd[-2])


'''
# Input the size of the matrix
n = int(input("Enter the size of array: "))

# Initialize lists for even and odd indexed elements
even = []
odd = []

# Collect elements based on index parity
for i in range(n):
    element = int(input(f"Enter element at {i} index: "))
    if i % 2 == 0:
        even.append(element)
    else:
        odd.append(element)

# Sort the even and odd lists
even.sort()
odd.sort()

# Print sorted even and odd lists
print("Sorted even array:", even)
print("Sorted odd array:", odd)

# Find the second largest elements in both lists
# Check to ensure that there are at least 2 elements in each list
if len(even) > 1 and len(odd) > 1:
    result = even[-2] + odd[-2]
    print("Sum of second largest elements from both arrays:", result)
else:
    print("Not enough elements to find the second largest in both arrays.")'''
