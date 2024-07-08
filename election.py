'''Problem Statement:
You are the head of the election committee in your village. Each political party is associated with a unique number and the votes are represented as an integer array 
𝐴
A where each element contains the party number voted for by the villagers. For a party to win, they must have a majority of votes. Your task is to find and return an integer value denoting the winning party's number. Return -1 if there is no party with a majority.

Note: If only one vote is there, he is the winner.

Input Format:

input1: An integer value representing the number of voters.
input2: An integer array 
𝐴
A representing the votes of the voters.'''

def voter(n, arr):
    d = {}
    if n == 1:
        return arr[0]
    for i in arr:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    x = sorted(d.items(), key=lambda x: x[1], reverse=True)
    if x[0][1] == x[1][1]:
        return -1
    else:
        return x[0][0]

n = int(input())
arr = list(map(int, input().split()))
print(voter(n, arr))


'''
# majority should be more than half condition is must
def voter(n, arr):
    d = {}
    if n == 1:
        return arr[0]
    
    # Count the votes for each party
    for i in arr:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    
    max_v = max(d.values())
    l = [party for party, votes in d.items() if votes == max_v]
    
    # Check if max votes constitute a majority
    if len(l) > 1 or max_v <= n // 2:
        return -1
    else:
        return l[0]

n = int(input())
arr = list(map(int, input().split()))
print(voter(n, arr))
'''

