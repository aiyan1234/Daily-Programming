'''7. Reverse Integer
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 

Constraints:

-231 <= x <= 231 - 1'''




def reverse(x):
        if x>=(-2**31) and x< (2**31) - 1:
            if x==0:
                return 0
            r=rem(x)
            s = str(r)
            if s:
                if s[0]=='-':
                    res1=-int(s[:0:-1])
                else:
                    res1=int(s[::-1])
                if res1>=(-2**31) and res1< (2**31) - 1:
                    return res1
                else:
                    return 0
            else:
                return 0
        else:
            return 0

def rem(x):
    if x % 10 != 0:
        return x
    else:
        return rem(x // 10)
x=int(input())
print(reverse(x))