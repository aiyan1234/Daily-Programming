'''Vowel repetition problem 
Given a string s print the most frequent vowel that is present in the string as a output 
Input Format: 
A single line containing the string s 
The input will be read form the STDIN by the candidate 
Output: 
Print a single character which represent the most frequent vowel in the given string'''


#this method gives recent most rep char
'''s=input("enter the string")
v={'a','A','e','E','i','I','O','o','U','u'}
l=[]
for i in s:
    if i in v:
        l.append(i)
print(l)
count=0
uniq=[]
for i in range(len(l)):
    if i not in uniq:
        x=l.count(i)
        count=max(count,x)
        ch=l[i]
print(ch)'''
#more accurate as it gives first most repeated chr as higest
s=input()
d={}
max_ch=float('-inf')
v='aeiou'
for i in s:
    if i in v:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
        if d[i]>max_ch:
            max_ch=d[i]
            ch=i
print(d)
print(max_ch)
print(ch)
