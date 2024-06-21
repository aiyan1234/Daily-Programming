#max no of vowels in in substring of given length
#sliding approch
#s='abciiidef'
s='aeiou'
k=2
#k=3
vowels={'a','e','i','o','u'}
currv=sum(1 for i in s[:k] if i in vowels)
maxv=currv
for i in range(1,len(s)-k):
    currv+=(s[i+k-1] in vowels)-(s[i-1] in vowels)
    if currv>maxv:
        maxv=currv
print(maxv)