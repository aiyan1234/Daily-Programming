'''1796. Second Largest Digit in a String
Solved
Easy
Topics
Companies
Hint
Given an alphanumeric string s, return the second largest numerical digit that appears in s, or -1 if it does not exist.

An alphanumeric string is a string consisting of lowercase English letters and digits.

 

Example 1:

Input: s = "dfa12321afd"
Output: 2
Explanation: The digits that appear in s are [1, 2, 3]. The second largest digit is 2.
Example 2:

Input: s = "abc1111"
Output: -1
Explanation: The digits that appear in s are [1]. There is no second largest digit. 
 '''


def secondHighest(self, s: str) -> int:
        res=[i for i in s if i.isdigit()]
        uni=[]
        for i in res:
            if i not in uni:
                uni.append(i)
        uni.sort()
        if len(uni)>1:
            return int(uni[-2])
        else:
            return -1
'''us={i for i in s if i.isdigit()}
        uni=sorted(us)
        if len(uni)>1:
            return int(uni[-2])
        else:
            return -1'''