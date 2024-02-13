"""
Simple tree.
"""

class SimpleTreeNode:
	
    def __init__(self, val, parent):
        self.NodeValue = val # значение в узле
        self.Parent = parent # родитель или None для корня
        self.Children = [] # список дочерних узлов
	
class SimpleTree:

    def __init__(self, root):
        self.Root = root # корень, может быть None
	
    def AddChild(self, ParentNode, NewChild):
        # код добавления нового дочернего узла существующему ParentNode
        NewChild.Parent = ParentNode
        ParentNode.Children.append(NewChild)
  
    def DeleteNode(self, NodeToDelete):
        # код удаления существующего узла NodeToDelete
        while NodeToDelete.Children != []:
            next_node_to_delete = NodeToDelete.Children[-1]
            self.DeleteNode(next_node_to_delete)
        NodeToDelete.Parent.Children.remove(NodeToDelete)
        del NodeToDelete.Parent

    def GetAllNodes(self):
        # код выдачи всех узлов дерева в определённом порядке
        list_of_nodes = []
        if self.Root == None:
            return list_of_nodes
        return self._GetAllNodes_recursion(self.Root, list_of_nodes)

    def _GetAllNodes_recursion(self, CurrentNode, list_of_nodes):
        list_of_nodes.append(CurrentNode)
        for node in CurrentNode.Children:
            self._GetAllNodes_recursion(node, list_of_nodes)
        return list_of_nodes

    def FindNodesByValue(self, val):
        # код поиска узлов по значению
        list_of_nodes = []
        if self.Root == None:
            return list_of_nodes
        return self._FindNodesByValue_recursion(val, self.Root, list_of_nodes)

    def _FindNodesByValue_recursion(self, val, CurrentNode, list_of_nodes):
        if CurrentNode.NodeValue == val:
            list_of_nodes.append(CurrentNode)
        for node in CurrentNode.Children:
            self._FindNodesByValue_recursion(val, node, list_of_nodes)
        return list_of_nodes
   
    def MoveNode(self, OriginalNode, NewParent):
        # код перемещения узла вместе с его поддеревом -- 
        # в качестве дочернего для узла NewParent
        OriginalNode.Parent.Children.remove(OriginalNode)
        self.AddChild(NewParent, OriginalNode)       
   
    def Count(self):
        # количество всех узлов в дереве
        node_count = 0
        if self.Root == None:
            return node_count
        return self._Count_recursion(self.Root, node_count)

    def _Count_recursion(self, CurrentNode, node_count):
        node_count += 1
        for node in CurrentNode.Children:
            node_count = self._Count_recursion(node, node_count)
        return node_count

    def LeafCount(self):
        # количество листьев в дереве
        leaf_node_count = 0
        if self.Root == None:
            return leaf_node_count
        return self._LeafCount_recursion(self.Root, leaf_node_count)

    def _LeafCount_recursion(self, CurrentNode, leaf_node_count):
        if len(CurrentNode.Children) == 0:
            leaf_node_count += 1
            return leaf_node_count
        for node in CurrentNode.Children:
            leaf_node_count = self._LeafCount_recursion(node, leaf_node_count)
        return leaf_node_count
