# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 02:01:11 2018

@author: Nitin
"""

"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

def Sum3HashTable(nums):
    nums.sort()
    result = []
    for i in range(len(nums)-2):
        if nums[i] > 0:
            break
        if i == 0 or (i>0 and nums[i] != nums[i-1]):
            low = i+1
            high = len(nums) - 1
            
            while low < high:
                print(low, high)
                if nums[low] + nums[high] + nums[i] == 0:
                    result.append([nums[i], nums[low], nums[high]])
                    while low < high and nums[low] == nums[low+1]:
                        low += 1
                    while low < high and nums[high] == nums[high-1]:
                        high -= 1
                    low += 1
                    high += 1
                elif nums[low] + nums[high] + nums[i] < 0:
                    low += 1
                else:
                    high -= 1
    return result
                        

S = [-1, 0, 1, 2, -1, -4]

result = Sum3HashTable(S)
print(result)




