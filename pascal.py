'''118. Pascal's Triangle
Solved
Easy
Topics
Companies
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
 

Constraints:

1 <= numRows <= 30'''

def generate(numRows: int) -> list[list[int]]:
        def fact(n):
            fact=1
            for i in range(2,n+1):
                fact*=i
            return fact
        n=numRows
        m=[]
        for i in range(0,n):
            h=[]
            for j in range(0,i+1):
                h.append(fact(i)//(fact(j)*fact(i-j)))
            m.append(h)
        return m
numRows = 5
print(generate(numRows))