# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#Idea is to perform a level-order traversal (BFS) of the binary tree and 
# capture the last node's value at each level, 
# which represents the right view of the tree.
# Time Complexity: O(N), where N is the number of nodes in the binary tree.
# Space Complexity: O(M), where M is the maximum number of nodes at any level in the tree.
from collections import deque
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []

        queue = deque([root])
        rightside = []

        while queue:
            level_length = len(queue)
            for i in range(level_length):
                node = queue.popleft()
                if i == level_length - 1:
                    rightside.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return rightside
        