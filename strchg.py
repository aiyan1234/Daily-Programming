'''Problem Statement:
You are given a function,
void *ReplaceCharacter(Char str[], int n, char ch1, char ch2);

The function accepts a string ‘ str’ of length n and two characters ‘ch1’ and ‘ch2’ as its argument.
Implement the function to modify and return the string ‘ str’ in such a way that all occurrences of ‘ch1’ in the original string are replaced by ‘ch2’ and all occurrences of ‘ch2’ in the original string are replaced by ‘ch1’.

Assumption: String Contains only lower-case alphabetical letters.

Note:
Return null if the string is null.
If both characters are not present in the string or both of them are the same , then return the string unchanged.

Example:
Input:
Str: apples
ch1:a
ch2:p

Output:
paales
Explanation:
‘A’ in the original string is replaced with ‘p’ and ‘p’ in the original string is replaced with ‘a’, thus output is paales.'''

def strchange(s,ch1,ch2):
    if s is None:
        return None
    if ch1 not in s and ch2 not in s:
        return s
    if ch1==ch2:
        return s
    s=list(s)
    for i in range(len(s)):
        if s[i]==ch1:
            s[i]=ch2
        elif s[i]==ch2:
            s[i]=ch1
    return ''.join(s)

s=input()
ch1=input()
ch2=input()
print(strchange(s,ch1,ch2))