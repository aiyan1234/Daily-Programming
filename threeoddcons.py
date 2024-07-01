'''
1550. Three Consecutive Odds

Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.
 
Example 1:

Input: arr = [2,6,4,1]
Output: false
Explanation: There are no three consecutive odds.
Example 2:

Input: arr = [1,2,34,3,4,5,7,23,12]
Output: true
Explanation: [5,7,23] are three consecutive odds.

arr =
[424,915,193,591,923]

Use Testcase
Output
false
Expected
true
 '''
def three_oddcons(arr):
    count=0
    maxc=0
    for i in arr:
        if i%2!=0:
            count+=1
            maxc=max(maxc,count)
        else:
            count=0
    return maxc>=3

arr =[424,915,193,591,923]
print(three_oddcons(arr))