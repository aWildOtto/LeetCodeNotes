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
        lol = result = ListNode(0)
        carry = 0

        while(l1 or l2 or carry == 1):
            if not l1:
                l1val = 0
            else:
                l1val = l1.val
                l1 = l1.next
            if not l2:
                l2val = 0
            else:
                l2val = l2.val
                l2 = l2.next
            sum = l1val + l2val + carry
            if sum > 9:
                sum %= 10
                carry = 1
                result.next = ListNode(sum)
            else:
                result.next = ListNode(sum)
                carry = 0
            result = result.next
            
            
   
        return lol.next