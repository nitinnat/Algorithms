# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 03:04:49 2018

@author: Nitin
"""

"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
def twoSum(nums,target):
    if len(nums) < 2:
        return []
    dic = {}
    for i,num in enumerate(nums):
        if num in dic:
            return [dic[num],i]
        else:
            dic[target - num] = i
    

nums = [3,2,4]
tgt = 6
print(twoSum(nums,tgt))
    