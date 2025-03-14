class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def traverse(temp):
            if temp.val == val:
                return temp
            left, right = None, None
            if temp.left:
                left = traverse(temp.left)
            if temp.right:
                right = traverse(temp.right)
            return left or right

        if root:
            return traverse(root)
        return None
