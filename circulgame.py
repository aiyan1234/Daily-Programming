'''1823. Find the Winner of the Circular Game
Companies
Hint
There are n friends that are playing a game. The friends are sitting in a circle and are numbered from 1 to n in clockwise order. More formally, moving clockwise from the ith friend brings you to the (i+1)th friend for 1 <= i < n, and moving clockwise from the nth friend brings you to the 1st friend.

The rules of the game are as follows:

Start at the 1st friend.
Count the next k friends in the clockwise direction including the friend you started at. The counting wraps around the circle and may count some friends more than once.
The last friend you counted leaves the circle and loses the game.
If there is still more than one friend in the circle, go back to step 2 starting from the friend immediately clockwise of the friend who just lost and repeat.
Else, the last friend in the circle wins the game.
Given the number of friends, n, and an integer k, return the winner of the game.

 

Example 1:


Input: n = 5, k = 2
Output: 3
Explanation: Here are the steps of the game:
1) Start at friend 1.
2) Count 2 friends clockwise, which are friends 1 and 2.
3) Friend 2 leaves the circle. Next start is friend 3.
4) Count 2 friends clockwise, which are friends 3 and 4.
5) Friend 4 leaves the circle. Next start is friend 5.
6) Count 2 friends clockwise, which are friends 5 and 1.
7) Friend 1 leaves the circle. Next start is friend 3.
8) Count 2 friends clockwise, which are friends 3 and 5.
9) Friend 5 leaves the circle. Only friend 3 is left, so they are the winner.
Example 2:

Input: n = 6, k = 5
Output: 1
Explanation: The friends leave in this order: 5, 4, 6, 2, 3. The winner is friend 1.
 '''

def findTheWinner(n,k):
        a=[i for i in range(1,n+1)]
        g=0
        while len(a)>1:
            g=(g+k-1)%len(a)  
            a.pop(g)
        return a[0]
n = 5
k = 2
print(findTheWinner(n,k))



'''the line g = (g + k - 1) % len(a) is crucial for correctly calculating the next index to remove. Here’s a breakdown of why it works:

Current Index (g): Starts from 0.
Increment by k-1: Since the counting starts from the current position and includes the current position, we need to increment by k-1 to get to the k-th person.
Modulo Operation: The % len(a) ensures that the index wraps around to the beginning of the list if it exceeds the current length of the list.'''