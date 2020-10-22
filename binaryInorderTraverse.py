from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def list_to_binarytree(nums):
    if not nums:
        return None
    root = TreeNode(nums[0])
    queue = [root]
    i = 1
    length = len(nums)
    while i < length:
        node = queue.pop(0)
        node.left = TreeNode(nums[i])
        if nums[i] is not None:
            queue.append(node.left)
        i += 1
        if i < length:
            node.right = TreeNode(nums[i])
            if nums[i] is not None:
                queue.append(node.right)
            i += 1
    return root

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            ans.append(root.val)
            inorder(root.right)
        ans = []
        inorder(root)
        return ans


lst = [3,9,20,None,None,15,7]
root = list_to_binarytree(lst)
print(Solution().inorderTraversal(root))

lst = [1,None,2,3]
root = list_to_binarytree(lst)
print(Solution().inorderTraversal(root))