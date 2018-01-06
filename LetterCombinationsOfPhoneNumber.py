# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 22:45:08 2018

@author: Nitin
"""

"""
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.



Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

"""
mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
               '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

def letterCombinations(digits):
    digits = list(str(digits))
    if len(digits) == 0:
        return []
    if len(digits) == 1:
        return list(mapping[digits[0]])
    previous = letterCombinations(digits[:-1])
    additional = mapping[digits[-1]]
    return [s + c for s in previous for c in additional]

digits = 968
print(letterCombinations(digits))