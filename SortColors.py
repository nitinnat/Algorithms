# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 18:19:26 2018

@author: Nitin
Given an array with n objects colored red, white or blue, sort them so that 
objects of the same color are adjacent, with the colors in the order 
red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, 
and blue respectively.

Note:
You are not supposed to use the library's sort function for this problem.
"""

def sortColors(nums):
    red = blue = white = 0
    if not nums:
        return nums
    for i in range(len(nums)):
        if nums[i] == 0:
            red += 1
        elif nums[i] == 1:
            white += 1
        else:
            blue += 1

    nums[0:red] = [0]*red
    nums[red:red+white+1] = [1]*white
    nums[red+white:red+white+blue+1] = [2]*blue
    return nums

nums = [1,0,0,2,2]
sortColors(nums)
print(nums)
    

