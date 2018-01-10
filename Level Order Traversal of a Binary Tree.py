# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 19:53:31 2018

@author: Nitin

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        #Basically a BFS
        queue = []
        visited = {}
        queue.append(root)
        visited[root] = True
        result.append([root.val])
        while queue:
            root = queue.pop(0)
            
            miniresult = []
            if root.left is not None and root.left not in visited.keys():
                    visited[root.left] = True
                    queue.append(root.left)
                    miniresult.append(root.left.val)
            
            if  root.right is not None and root.right not in visited.keys():
                    visited[root.right] = True
                    queue.append(root.right)
                    miniresult.append(root.right.val)
            if miniresult:
                result.append(miniresult)
        return result
                

