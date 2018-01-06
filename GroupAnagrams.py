# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 21:53:02 2018

@author: Nitin
"""

"""
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note: All inputs will be in lower-case.
"""
import collections
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
def groupAnagramsSorting(strs):
    dic = {}
    for s in strs:
        try:
            dic[''.join(sorted(s))].append(s)
        except KeyError:
            dic[''.join(sorted(s))] = [s]
    result = []
    for key in dic.keys():
        result.append(dic[key])
    return sorted(result)
print(sorted(groupAnagramsSorting(strs)))


def groupAnagramsCounts(strs):
    #maintain counts of each character
        ans = collections.defaultdict(list)
        for s in strs:
            counts = [0]*26
            for ch in s:
                counts[ord(ch) - ord('a')] += 1
            ans[tuple(counts)].append(s)
        return ans.values()
    
print(groupAnagramsCounts(strs))
    
    
