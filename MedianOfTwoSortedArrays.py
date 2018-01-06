# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 22:20:23 2018

@author: Nitin
"""

"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""

def medianOfTwoSortedArrays(nums1,nums2):
    nums = nums1 + nums2
    first = 0
    second = len(nums1)/2
    third = 