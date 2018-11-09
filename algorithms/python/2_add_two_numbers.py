# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        s = 0
        carry = 0
        multiplier = 1
        output= []
        while l1 != None and l2 != None:
            s = l1.val + l2.val+ carry
            carry = s/10
            s %= 10
            l1 = l1.next
            l2 = l2.next
            output.append(s)
        if  l1 == None and l2 == None and carry != 0:
            output.append(carry)
        elif l1 == None and l2 != None:
            while l2:
                s = l2.val+carry
                carry = s/10
                s %= 10
                l2 = l2.next
                output.append(s)
            if carry != 0:
                output.append(carry)
        elif l2 == None and l1 != None:
            while l1:
                s = l1.val+carry
                carry = s/10
                s %= 10
                l1 = l1.next
                output.append(s)
            if carry != 0:
                output.append(carry)
        
        return output
