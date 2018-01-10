# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 03:01:26 2018

@author: Nitin
"""

"""
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.
Example 1:

Input: 1
Output: "1"

Example 2:

Input: 4
Output: "1211"
"""

def countAndSay(n):
    if n == 1:
        return '1'
    count = 0
    out = '1'
    for i in range(1,n):
        prefix = ''
        ptr = 0
        while ptr < len(out)-1:
            while out[ptr] == out[ptr+1]:
                ptr += 1
            
            
    
    
    