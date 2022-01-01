# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        def postOrder(node, subtreeCnt, res):
            if node == None: return "#"
            
            serial = str(node.val) + "," + postOrder(node.left, subtreeCnt, res) + "," + postOrder(node.right, subtreeCnt, res) 
            subtreeCnt[serial] = subtreeCnt.get(serial, 0) + 1
            if subtreeCnt[serial] == 2:
                res.append(node)
            return serial
        
        res = list()
        subtreeCnt = dict()
        postOrder(root, subtreeCnt, res)
        return res
