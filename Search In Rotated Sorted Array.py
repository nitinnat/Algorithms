# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 02:24:39 2018

@author: Nitin
"""
"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

"""

def rotatedSortedArray(nums,target):
    
    def binarySearch(arr,target):
        low = 0
        high = len(arr)-1
        
        while low <= high:
            mid = int((low+high)/2)
            if target == arr[mid]:
                return mid
            if target < arr[mid]:
                high = mid - 1
            if target > arr[mid]:
                low = mid + 1
        return -1
        
    if not nums: return -1
    if len(nums) <= 2:
        if target in nums:
            return nums.index(target)
        else:
            return -1
    
    rot = -1
    #Need to find the point of rotation, can be done in O(n) time
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            #Point of rotation found
            rot = i+1
            break
    print(rot)
    if rot == -1:
        #Array is not rotated. Find using binary search O(lgn)
        return binarySearch(nums,target)
    if target == nums[rot]:
        return rot
    else:
        if target > nums[rot] and target < nums[0]:
            print("Entered here...")
            loc = binarySearch(nums[rot:],target)
            if loc == -1:
                return loc
            else:
                return rot + loc
        elif target >= nums[0]:
            loc = binarySearch(nums[0:rot],target)
            if loc == -1: 
                return loc
            else:
                return loc
        
            

print(rotatedSortedArray([3,5,1],3))
