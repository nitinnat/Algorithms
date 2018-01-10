# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 03:40:29 2018

@author: Nitin
"""

"""
Given a string S, you are allowed to convert it to a palindrome by adding characters in front of it. 
Find and return the shortest palindrome you can find by performing this transformation.

For example:

Given "aacecaaa", return "aaacecaaa".

Given "abcd", return "dcbabcd".
"""

"""
First idea 
Compare last two elements of the string.
If unequal, add the last element to the front and recurse on s[1:-1]

"""


def shortestPalindrome(s):
    if len(s) == 1:
        return s
    if len(s) == 0:
        return ''
    start = 0
    end = len(s) -1
    while start < end:
        
        if s[start] == s[end]:
            start += 1
            end -= 1
        else:
            prefix = s[0:start]
            suffix = s[end:len(s)]
            s = prefix + s[end] + s[start:end+1] + suffix
            start += 1
            end -= 1
        print(s)
    return s


#shortestPalindrome("abcd")
  


def shortestPalidromeRecursion(s,prefix,suffix):
    print("Prefix: %s, String: %s, Suffix: %s"%(prefix,s,suffix))
    if len(s) == "":
        return prefix + suffix
    else:
        print(s)
        if len(s) > 1:
            while True:
                try:
                    if s[0] == s[-1]:
                        prefix = prefix + s[0]
                        suffix = s[-1] + suffix
                        s = s[1:len(s)-1]
                    else:
                        break
                except IndexError:
                    break
        
        if len(s) == 1:
            return prefix + s + suffix
        if len(s) == 0:
            return prefix + suffix[1:]
        else:
            prefix = prefix + s[-1]
            suffix = s[-1] + suffix 
            return shortestPalidromeRecursion(s[0:len(s)-1],prefix,suffix)
                
        print("After speedup, Prefix: %s, String: %s, Suffix: %s"%(prefix,s,suffix))
       
            
        
        
print(shortestPalidromeRecursion("aacecaaa","",""))