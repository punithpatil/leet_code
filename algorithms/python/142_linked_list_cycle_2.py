# https://leetcode.com/problems/linked-list-cycle-ii/

# Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

# Note: Do not modify the linked list.

# Follow up:
# Can you solve it without using extra space?

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # https://en.wikipedia.org/wiki/Cycle_detection
        # Check for empty list
        if head is None:
            return None
        tortoise = hare = head
        
        # First detect cycle
        
        while True:
            # If no cycle exists
            if hare is None or hare.next is None :
                return None
            tortoise = tortoise.next
            hare = hare.next.next
            if tortoise is hare:
                break
                
        # Now reset tortoise, both jump one step till they meet
        # They will meet at the start of the cycle
        tortoise = head
        
        while tortoise is not hare:
            tortoise = tortoise.next
            hare = hare.next
            
        return tortoise 