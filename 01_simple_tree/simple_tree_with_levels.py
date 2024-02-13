"""
Simple tree with levels.
"""

from simple_tree import SimpleTreeNode, SimpleTree

class SimpleTreeNodeWithLevel(SimpleTreeNode):
	
    def __init__(self, val, parent):
        super().__init__(val, parent)
        self.Level = 0 # уровень в дереве (0 - корень)
	
class SimpleTreeWithLevels(SimpleTree):

    def AddChild(self, ParentNode, NewChild):
        super().AddChild(ParentNode, NewChild)
        NewChild.Level = ParentNode.Level + 1         
   
    def MoveNode(self, OriginalNode, NewParent):
        super().MoveNode(OriginalNode, NewParent)
        original_node_new_level = NewParent.Level + 1
        self._SetLevels_recursion(OriginalNode, original_node_new_level)

    def SetLevels(self):
        # простановка узлов в дереве
        if self.Root == None:
            return
        node_level = 0
        return self._SetLevels_recursion(self.Root, node_level)

    def _SetLevels_recursion(self, CurrentNode, node_level):
        CurrentNode.Level = node_level
        node_level += 1
        for node in CurrentNode.Children:
            self._SetLevels_recursion(node, node_level)
