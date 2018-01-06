# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 03:09:12 2018

@author: Nitin
"""

"""
Implement pow(x, n).
Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
"""

def power(x,n):
    a = 1
    if n == 0:
        return 1
    
    def power_helper(y,m):
        if m == 1:
            return y
        if m == 0:
            return 1
        if m%2 == 1:
            return y*power_helper(y,m-1)
        else:
            b = power_helper(y,m/2)
            return b*b
        
    a = power_helper(x,abs(n))
    if n < 0:
        return 1/a
    else:
        return a
        
0.00001
2147483647
print(power(0.00001,2147483647))
