# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 23:59:30 2018

@author: Nitin
"""

#Leetcode problem 442
#Find all duplicates in an Array

"""
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]

"""


#This method uses O(n) space and O(n) time
def usingSet(arr):
    tempset = set()
    result = []
    for i,val in enumerate(arr):
        if val not in tempset:
            tempset.add(val)
        else:
            result.append(val)
    return result

inp = [4,3,2,7,8,2,3,1]
op = usingSet(inp)
print(op)


#To do it in O(1) space and O(1) time

def withoutSet(arr):
    result = []
    for x in arr:
        if arr[abs(x)-1] > 0:
            arr[abs(x)-1] = -arr[abs(x)-1]
        else:
            result.append(abs(x))
    return result


inp = [4,3,2,7,8,2,3,1]
op = withoutSet(inp)
print(op)                

