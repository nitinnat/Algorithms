# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 19:21:52 2018

@author: Nitin
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
Value of Counter            Subset
    000                    -> Empty set
    001                    -> a
    010                    -> b
    011                    -> ab
    100                    -> c
    101                    -> ac
    110                    -> bc
    111                    -> abc
    
Depending on which bit is high, you append it.
So if 0, don't append that number. Iterate outer loop for 2^n, and inner loop
for n times. n is the size of the input array.

"""

def subsets(nums):
    
    result = []
    power_set_size = pow(2,len(nums))
    set_size = len(nums)
    for i in range(power_set_size):
        cur_result = []
        for j in range(set_size):
            
            if i & (1<<j):
                cur_result.append(nums[j])
        result.append(cur_result)
    return result
        

print(subsets([1,2,3]))
