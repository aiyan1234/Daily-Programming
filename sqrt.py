'''69. Sqrt(x)
Hint
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 

Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

#approch

Start with the number you want to find the square root of, say 
𝑁
N.
Subtract successive odd numbers from 
𝑁
N until you reach zero or a negative number.
The number of subtractions you performed before reaching zero or going negative is the square root of 
𝑁
N

'''
def mySqrt(x):
        count=0
        i=1
        while x-i>=0:
            x=x-i
            i=i+2
            count=count+1
        return count
x = 16
print(mySqrt(x))