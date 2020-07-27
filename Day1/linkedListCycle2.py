# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:

        cur,seen = head, set([head])
        # while there is a cur
        while(cur):
            # set next cur
            cur = cur.next
            # if seen already, reeturn cur
            if cur in seen: return cur
            # if not add to cur
            seen.add(cur)
        return None