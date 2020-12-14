# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        dummy = ListNode(x-1, head)
        left = dummy
        while left.next and left.next.val < x: left = left.next
            
        # if there is valid insert point
        if left.next:
            connect = left.next
            node = left.next
            
            while node.next:
                
                if node.next.val < x: 
                    # remove this invalid node
                    to_move = node.next
                    node.next = node.next.next
                    
                    # insert this invalid node to insert point
                    left.next = to_move
                    left = to_move
                else:
                    node = node.next
            left.next = connect
        return dummy.next
                    