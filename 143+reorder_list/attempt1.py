# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        self.hasNext(head, head, 1)
        
    
    def hasNext(self, head, curr_node, cnt):
        cur_cnt = 0
        max_cnt = cnt
        
        if curr_node and curr_node.next:
            head, cur_cnt, max_cnt = self.hasNext(head, curr_node.next, cnt+1)
            
        # if recursion already finished
        if head == None: return None, cur_cnt, max_cnt

        # current node is last one
        if cur_cnt + 1 == max_cnt: 
            head.next = None
            return None, cur_cnt + 1, max_cnt
        
        next_head = head.next
        head.next = curr_node
        cur_cnt += 2
        
        # if this 2 node finish up the recursion
        if cur_cnt == max_cnt: 
            curr_node.next = None
            return None, cur_cnt, max_cnt
        else:
            curr_node.next = next_head
            return next_head, cur_cnt, max_cnt