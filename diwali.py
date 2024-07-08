'''
Diwali party 
Max is planning to take part in a Diwali contest at a Diwali Party that will begin at 8 PM and will 
run until midnight (12 AM) l.e., for 4 hours. He also needs to travel to the party venue within this 
time which takes him P minutes. The contest comprises of N problems that are arranged in order of 
difficulty, with problem 1 being the simplest and problem N being the most difficult. Max is aware 
that he will require 5*1 minutes to solve the problem. 
Your task is help Max find and return an integer value, representing the number of problems Max 
can solve and reach the party venue within the given time frame of 4 hours. 
Note: Max will leave his home at exactly B PM to reach the party venue. 
Input Format: 
Input: An integer value N, representing the total number of problems. 
Input2: An integer value P, Representing the time to travel in minutes from his home to the party 
venue.'''
n=int(input("enter the total problem: "))
p=int(input("enter the time taken to travel"))
tr=(4*60)-p
p=0
i=1
while i<=n and tr>5*i: #tr>=5*i
    p=p+1
    tr-=5*i
    i=i+1
print(p)
