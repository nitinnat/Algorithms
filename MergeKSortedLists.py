# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 00:29:20 2018

@author: Nitin
"""

"""
Merge k sorted lists

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return lists
        #Merges 2 lists
        def merge(list1,list2):
            if list1 is None:
                return list2
            if list2 is None:
                return list1
            if list1.val <list2.val:
                head = ListNode(list1.val)
                list3 = head
                list1 = list1.next
            else:
                head =  ListNode(list2.val)
                list3 = head
                list2 = list2.next
            
            while True:
                if list1 is None or list2 is None:
                    break
                if list1.val < list2.val:
                    list3.next = list1
                    list3 = list3.next
                    list1 = list1.next
                else:
                    list3.next = list2
                    list3 = list3.next
                    list2 = list2.next
            
            while True:
                if list1 is None:
                    break
                list3.next = list1
                list3 = list3.next
                list1 = list1.next
            while True:
                if list2 is None:
                    break
                list3.next = list2
                list3 = list3.next
                list2 = list2.next
            return head
                
        
        #Now merge k lists
        merged_list = lists[0]
        for i in range(len(lists) - 1):
            merged_list = merge(merged_list,lists[i+1])
            
        return merged_list
            
            