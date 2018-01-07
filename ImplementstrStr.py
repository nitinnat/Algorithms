# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 03:28:06 2018

@author: Nitin
"""

"""

Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
"""

def strStr(haystack, needle):
    if len(haystack) < len(needle):
        return -1
    if len(haystack) == len(needle):
        if haystack == needle: return 0
        else: return -1
    
    for i in range(len(haystack)-len(needle)+1):
        print(i, print(haystack[i:i+len(needle)]))
        if haystack[i:i+len(needle)] == needle:
            return i
        
    return -1

print(strStr("mississippi","pi"))