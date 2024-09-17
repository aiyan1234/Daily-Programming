'''Question : 17
Instructions: You are required to write the code. You can click on compile and run anytime to check compilation/execution status. The code should be logically/syntactically correct.

Question: Write a program in C such that it takes a lower limit and upper limit as inputs and print all the intermediate palindrome numbers.

Test Cases:

TestCase 1:
Input :
10 , 80
Expected Result:
11 , 22 , 33 , 44 , 55 , 66 , 77.

Test Case 2:
Input:
100,200
Expected Result:
101 , 111 , 121 , 131 , 141 , 151 , 161 , 171 , 181 , 191.'''
def checkpalindrome(strt,end):
    res=[]
    for i in range(strt,end+1):
        if str(i)==str(i)[::-1]:
            res.append(i)
    return res
        
    
strt=int(input())
end=int(input())
res=checkpalindrome(strt,end)
for i in range(len(res)):
    if i==len(res)-1:
        print(res[i],'')
    else:
        print(res[i],end=', ')