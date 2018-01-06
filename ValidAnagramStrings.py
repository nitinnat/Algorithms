# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 21:38:47 2018

@author: Nitin
"""

"""
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""

def validAnagram_nlogn(s,t):
    if len(s) == len(t):
        return True
    if sorted(s) == sorted(t):
        return True
    return False

def validAnagram_n(s,t):
    vec = [0]*256
    for ch in s:
        vec[ord(ch)] += 1
    for ch in t:
        vec[ord(ch)] -= 1
    if vec == [0]*256: return True
    return False

s = "anagram"
t = "nagarams"

print(validAnagram_nlogn(s,t))
print(validAnagram_n(s,t))
