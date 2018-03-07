from statistics import mean

'''

Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
Note:
The range of node's value is in the range of 32-bit signed integer.

References: 1) https://docs.python.org/3/library/functions.html#any
            2) Iterating through tuple will happen just like a normal array.

'''

'''

Other way to do it - 

def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        return list(map(mean, self.levelOrder(root)))

    # copied&pasted from old problem's solution: -> will create [[3], [9,20], [15,7]]
    def levelOrder(self, root):
        levels = []
        level = [root]
        while any(level):
            levels.append([node.val for node in level]) # note that we are appending an list, so map will go through, each list inside a list
            level = [kid for node in level for kid in (node.left, node.right) if kid]
        return levels

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root):
        averages = []
        level = [root]
        while level:
            averages.append(sum(node.val for node in level) / len(level))
            level = [kid for node in level for kid in (node.left, node.right) if kid]
        return averages