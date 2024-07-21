'''228. Summary Ranges
Solved
Easy
Topics
Companies
You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
 

Example 1:

Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
Example 2:

Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"

'''
def summaryRanges(nums):
        curr=0
        l=[]
        i=curr
        while curr<len(nums)-1:
            if nums[curr+1]-nums[curr]==1:
                curr+=1
            else:
                if i==curr:
                    l.append(str(nums[i]))
                else:
                    l.append(str(nums[i])+'->'+str(nums[curr]))
                curr+=1
                i=curr
        if curr<len(nums):
            if nums[curr]-nums[curr-1]==1:
                l.append(str(nums[i])+'->'+str(nums[curr]))
            else:
                l.append(str(nums[curr]))
        print(l)
        return l
nums = [0,2,3,4,6,8,9]
print(summaryRanges(nums))

'''
def summaryRanges(self, nums: List[int]) -> List[str]:
    if not nums:
        return []

    ranges = []
    start = nums[0]

    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1] + 1:
            if start == nums[i - 1]:
                ranges.append(str(start))
            else:
                ranges.append(f"{start}->{nums[i - 1]}")
            start = nums[i]

    if start == nums[-1]:
        ranges.append(str(start))
    else:
        ranges.append(f"{start}->{nums[-1]}")

    return ranges'''