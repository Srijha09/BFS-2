
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Idea is to perform a level-order traversal (BFS) of the binary tree while keeping track of each node's parent.
# At each level, we check if the two target nodes are found and ensure they have different
# parents to confirm they are cousins
# Time Complexity: O(N), where N is the number of nodes in the binary tree.
# Space Complexity: O(M), where M is the maximum number of nodes at any level in the tree.
from collections import deque
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: Optional[TreeNode]
        :type x: int
        :type y: int
        :rtype: bool
        """
      
        if not root:
            return False

        queue = deque([(root, None)])  # (node, parent)

        while queue:
            level_size = len(queue)
            x_parent = y_parent = None

            for _ in range(level_size):
                node, parent = queue.popleft()

                if node.val == x:
                    x_parent = parent
                elif node.val == y:
                    y_parent = parent

                if node.left:
                    queue.append((node.left, node))
                if node.right:
                    queue.append((node.right, node))

            # Check if found both nodes at this level
            if x_parent and y_parent:
                return x_parent != y_parent
            if x_parent or y_parent:
                return False

        