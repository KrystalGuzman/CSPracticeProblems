# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = l1
        carry = 0
        while l2:
            #adds values
            sums = l1.val + l2.val +carry
            #save remainder as value
            l1.val = sums % 10
            #save what to carry as carry
            carry = sums // 10
            #check next of l1 is None
            if l1.next is None:
                l1.next = l2.next
                break
            #check next of l2 is None
            if l2.next is None:
                break
            #set nexts
            l1=l1.next
            l2=l2.next
        #while remainder
        while carry>0:
            #check if there is a next
            if l1.next is None:
                #set l1.next to ListNode(0)
                l1.next = ListNode(0)
            l1 = l1.next
            #set sums as carry+ l1.val
            sums = carry + l1.val
            #save remainder
            l1.val = sums % 10
            #save what to carry
            carry = sums // 10
        return head