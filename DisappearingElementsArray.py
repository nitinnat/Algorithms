# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 00:31:43 2018

@author: Nitin
"""

"""
448. Find All Numbers Disappeared in an Array

Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
"""

def withoutSet(arr):
    result = []
    for x in arr:
        if arr[abs(x) -1] > 0:
            arr[abs(x)-1] = -arr[abs(x)-1]
    for i,x in enumerate(arr):
        if x > 0:
            result.append(i+1)
    return result

inp = [4,3,2,7,8,2,3,1]
op = withoutSet(inp)
print(op)