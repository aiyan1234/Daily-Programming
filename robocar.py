arr=[1,-2,3,4]
s=0
far=0
for i in arr:
    s+=i
    far=max(far,abs(s))
print(far)

