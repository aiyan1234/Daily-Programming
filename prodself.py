'''238. Product of Array Except Self
Hint
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]'''
 
def productExceptSelf(nums):
        z=0
        for i in nums:
            if i==0:
                z+=1
        if z>=2:
            return [0]*len(nums)
  
        pro=1
        res=[]
        for i in nums:
            if i!=0:
                pro=pro*i
        if z==1:
            for i in nums:
                if i!=0:
                    res.append(0)
                else:
                    res.append(pro)
        else:
            for i in range(len(nums)):
                res.append(pro//nums[i])
        return res
nums = [-1,1,0,-3,3]
print(productExceptSelf(nums))