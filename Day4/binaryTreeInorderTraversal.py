# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        #sets result and stack
        result, stack = [], [(root, False)]
        #loops if stack is true
        while stack:
            #sets cur and visited
            cur, visited = stack.pop()
            #checks cur
            if cur:
                #checks visited
                if visited:
                    #adds to result
                    result.append(cur.val)
                else:
                    #appends node
                    stack.append((cur.right, False))
                    stack.append((cur, True))
                    stack.append((cur.left, False))

        return result