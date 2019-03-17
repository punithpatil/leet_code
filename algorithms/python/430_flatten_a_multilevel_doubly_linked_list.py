# https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/submissions/

# You are given a doubly linked list which in addition to the next and previous pointers, it could have a child pointer, which may or may not point to a separate doubly linked list. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure, as shown in the example below.

# Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given the head of the first level of the list.

 

# Example:

# Input:
#  1---2---3---4---5---6--NULL
#          |
#          7---8---9---10--NULL
#              |
#              11--12--NULL

# Output:
# 1-2-3-7-8-11-12-9-10-4-5-6-NULL

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        current = head
        next_ = None
        while current:
            if current.child:
                child_pointer = child_head = current.child # store head for later
                while child_pointer.next:   # move to the last node of the child
                    child_pointer = child_pointer.next
                if current.next:    # edge case if current is the last node and has a child
                    # connect child end to current.next
                    child_pointer.next = current.next
                    current.next.prev = child_pointer
                # connect current to child
                current.child = None
                child_head.prev = current
                current.next = child_head

            # No child, go forward    
            current = current.next
        return head
                