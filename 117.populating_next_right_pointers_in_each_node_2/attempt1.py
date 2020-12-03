"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root: 
            nodes = [root]
            while nodes:
                nodes = self.levelTraversal(nodes)
        
        return root
    
    def levelTraversal(self, nodes):
        next_level = []
        num = len(nodes)
        for i in range(num):
            node = nodes[i]
            if i+1 < num: 
                node.next = nodes[i+1]
            else:
                node.next = None
                
            if node.left: next_level.append(node.left)
            if node.right: next_level.append(node.right)
        return next_level
        