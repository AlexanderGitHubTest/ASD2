"""
Balanced BST (Binary Search Tree) (2)
"""

class BSTNode:
	
    def __init__(self, key, parent):
        self.NodeKey = key # ключ узла
        self.Parent = parent # родитель или None для корня
        self.LeftChild = None # левый потомок
        self.RightChild = None # правый потомок
        self.Level = 0 # уровень узла
        
class BalancedBST:
		
    def __init__(self):
    	self.Root = None # корень дерева

    def GenerateTree(self, a):
	# создаём дерево с нуля из неотсортированного массива a
        if a == []:
            return
        a = a[:]
        a.sort()
        level = 0
        self.Root = self.GenerateTree_recursion(None, level, a)

    def GenerateTree_recursion(self, parent, level, a):
        center_array_id = len(a) // 2
        current_node = BSTNode(a[center_array_id], parent)
        current_node.Level = level
        if center_array_id == 0:
            return current_node
        current_node.LeftChild = self.GenerateTree_recursion(current_node, level + 1, a[0:center_array_id])
        if center_array_id < (len(a) - 1):
            current_node.RightChild = self.GenerateTree_recursion(current_node, level + 1, a[center_array_id + 1:])
        return current_node

    def IsBalanced(self, root_node):
        # сбалансировано ли дерево с корнем root_node
        return self.IsBalanced_recursion(root_node)[0]
    def IsBalanced_recursion(self, current_node):
        left_branch_length = 0
        right_branch_length = 0
        is_left_subtree_balanced = True
        is_right_subtree_balanced = True
        if current_node.LeftChild !=None:
            is_left_subtree_balanced, left_branch_length = self.IsBalanced_recursion(current_node.LeftChild)
        if current_node.RightChild !=None:
            is_right_subtree_balanced, right_branch_length = self.IsBalanced_recursion(current_node.RightChild)
        is_all_subtree_balanced = is_left_subtree_balanced and is_right_subtree_balanced
        is_difference_between_subtrees_does_not_exceed_one = abs(left_branch_length - right_branch_length) <= 1
        max_branches_length = max(left_branch_length, right_branch_length)
        return (is_all_subtree_balanced and is_difference_between_subtrees_does_not_exceed_one, max_branches_length + 1)

