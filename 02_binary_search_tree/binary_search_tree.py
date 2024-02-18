"""
Binary search tree.
"""

class BSTNode:
	
    def __init__(self, key, val, parent):
        self.NodeKey = key # ключ узла
        self.NodeValue = val # значение в узле
        self.Parent = parent # родитель или None для корня
        self.LeftChild = None # левый потомок
        self.RightChild = None # правый потомок

class BSTFind: # промежуточный результат поиска

    def __init__(self):
        self.Node = None # None если 
        # в дереве вообще нету узлов

        self.NodeHasKey = False # True если узел найден
        self.ToLeft = False # True, если родительскому узлу надо 
        # добавить новый узел левым потомком

class BST:

    def __init__(self, node):
        self.Root = node # корень дерева, или None

    def FindNodeByKey(self, key):
        # ищем в дереве узел и сопутствующую информацию по ключу
        current_node = self.Root
        if current_node == None:
            return BSTFind()
        return self.FindNodeByKey_recursion(key, current_node)

    def FindNodeByKey_recursion(self, key, current_node):
        if key == current_node.NodeKey:
            search_result = BSTFind()
            search_result.Node = current_node
            search_result.NodeHasKey = True
            return search_result
        if (    key < current_node.NodeKey
            and current_node.LeftChild == None
           ):
            search_result = BSTFind()
            search_result.Node = current_node
            search_result.ToLeft = True
            return search_result
        if (    key < current_node.NodeKey
            and current_node.LeftChild != None
           ):
            current_node = current_node.LeftChild
            return self.FindNodeByKey_recursion(key, current_node)
        if current_node.RightChild == None:
            search_result = BSTFind()
            search_result.Node = current_node
            return search_result
        current_node = current_node.RightChild
        return self.FindNodeByKey_recursion(key, current_node)
        
    def AddKeyValue(self, key, val):
        # добавляем ключ-значение в дерево
        key_search_result = self.FindNodeByKey(key)
        if key_search_result.Node == None:
            self.Root = BSTNode(key, val, None)
            return True
        if key_search_result.NodeHasKey:
            return False
        if key_search_result.ToLeft:
            key_search_result.Node.LeftChild = BSTNode(key, val, None)
            key_search_result.Node.LeftChild.Parent = key_search_result.Node
            return True
        key_search_result.Node.RightChild = BSTNode(key, val, None)
        key_search_result.Node.RightChild.Parent = key_search_result.Node
        return True          
  
    def FinMinMax(self, FromNode, FindMax):
        # ищем максимальный/минимальный ключ в поддереве
        # возвращается объект типа BSTNode
        if FindMax and FromNode.RightChild == None:
            return FromNode
        if FindMax and FromNode.RightChild != None:
            return self.FinMinMax(FromNode.RightChild, FindMax)
        if FromNode.LeftChild == None:
            return FromNode
        return self.FinMinMax(FromNode.LeftChild, FindMax)        
	
    def DeleteNodeByKey(self, key):
        # удаляем узел по ключу
        key_search_result = self.FindNodeByKey(key)
        if (       key_search_result.Node == None 
            or not key_search_result.NodeHasKey
           ):
            return False
        if key_search_result.Node.Parent == None:
            key_search_result_parent_type = None
        if (    key_search_result.Node.Parent != None
            and key_search_result.Node.Parent.LeftChild == key_search_result.Node
           ):
            key_search_result_parent_type = "left_child"
        if (    key_search_result.Node.Parent != None
            and key_search_result.Node.Parent.RightChild == key_search_result.Node
           ):
            key_search_result_parent_type = "right_child"
        # key search result is leaf
        if (    key_search_result.Node.LeftChild == None
            and key_search_result.Node.RightChild == None
            and key_search_result_parent_type == None
           ):
            self.Root = None
            del key_search_result.Node.Parent
            del key_search_result.Node
            return True
        if (    key_search_result.Node.LeftChild == None
            and key_search_result.Node.RightChild == None
            and key_search_result_parent_type == "left_child"
           ):
            key_search_result.Node.Parent.LeftChild = None
            del key_search_result.Node.Parent
            del key_search_result.Node
            return True
        if (    key_search_result.Node.LeftChild == None
            and key_search_result.Node.RightChild == None
           ):
            key_search_result.Node.Parent.RightChild = None
            del key_search_result.Node.Parent
            del key_search_result.Node
            return True
        # key search result has only left branch
        if (    key_search_result.Node.LeftChild != None
            and key_search_result.Node.RightChild == None
            and key_search_result_parent_type == None
           ):
            key_search_result.Node.LeftChild.Parent = None
            self.Root = key_search_result.Node.LeftChild
            del key_search_result.Node
            return True
        if (    key_search_result.Node.LeftChild != None
            and key_search_result.Node.RightChild == None
            and key_search_result_parent_type == "left_child"
           ):
            key_search_result.Node.Parent.LeftChild = key_search_result.Node.LeftChild
            key_search_result.Node.LeftChild.Parent = key_search_result.Node.Parent
            del key_search_result.Node.LeftChild
            del key_search_result.Node.Parent
            del key_search_result.Node
            return True
        if (    key_search_result.Node.LeftChild != None
            and key_search_result.Node.RightChild == None
           ):
            key_search_result.Node.Parent.RightChild = key_search_result.Node.LeftChild
            key_search_result.Node.LeftChild.Parent = key_search_result.Node.Parent
            del key_search_result.Node.LeftChild
            del key_search_result.Node.Parent
            del key_search_result.Node
            return True
        # key search result has only right branch
        if (    key_search_result.Node.LeftChild == None
            and key_search_result.Node.RightChild != None
            and key_search_result_parent_type == None
           ):
            key_search_result.Node.RightChild.Parent = None
            self.Root = key_search_result.Node.RightChild
            del key_search_result.Node.Parent
            del key_search_result.Node
            return True
        if (    key_search_result.Node.LeftChild == None
            and key_search_result.Node.RightChild != None
            and key_search_result_parent_type == "left_child"
           ):
            key_search_result.Node.Parent.LeftChild = key_search_result.Node.RightChild
            key_search_result.Node.RightChild.Parent = key_search_result.Node.Parent
            del key_search_result.Node.RightChild
            del key_search_result.Node.Parent
            del key_search_result.Node
            return True
        if (    key_search_result.Node.LeftChild == None
            and key_search_result.Node.RightChild != None
           ):
            key_search_result.Node.Parent.RightChild = key_search_result.Node.RightChild
            key_search_result.Node.RightChild.Parent = key_search_result.Node.Parent
            del key_search_result.Node.RightChild
            del key_search_result.Node
            return True
        # key search result has left and right branches
        if (    key_search_result.Node.RightChild.LeftChild == None
            and key_search_result_parent_type == None
           ):
            key_search_result.Node.RightChild.Parent = None
            key_search_result.Node.LeftChild.Parent = key_search_result.Node.RightChild
            key_search_result.Node.RightChild.LeftChild = key_search_result.Node.LeftChild
            self.Root = key_search_result.Node.RightChild
            del key_search_result.Node
            return True
        if (    key_search_result.Node.RightChild.LeftChild == None
            and key_search_result_parent_type == "left_child"
           ):
            key_search_result.Node.Parent.LeftChild = key_search_result.Node.RightChild
            key_search_result.Node.RightChild.Parent = key_search_result.Node.Parent
            key_search_result.Node.LeftChild.Parent = key_search_result.Node.RightChild
            key_search_result.Node.RightChild.LeftChild = key_search_result.Node.LeftChild
            del key_search_result.Node
            return True
        if key_search_result.Node.RightChild.LeftChild == None:
            key_search_result.Node.Parent.RightChild = key_search_result.Node.RightChild
            key_search_result.Node.RightChild.Parent = key_search_result.Node.Parent
            key_search_result.Node.LeftChild.Parent = key_search_result.Node.RightChild
            key_search_result.Node.RightChild.LeftChild = key_search_result.Node.LeftChild
            del key_search_result.Node
            return True      
        return self.DeleteNodeByKey_recursion(key_search_result.Node.RightChild.LeftChild, 
                                         key_search_result.Node,
                                         key_search_result_parent_type
                                        )

    def DeleteNodeByKey_recursion(self, current_node, result_node, key_search_result_parent_type):
        if (    current_node.LeftChild == None
            and current_node.RightChild == None
            and key_search_result_parent_type == None
           ):
            current_node.Parent.LeftChild = None
            current_node.Parent = None
            current_node.LeftChild = result_node.LeftChild
            current_node.RightChild = result_node.RightChild
            result_node.LeftChild.Parent = current_node
            result_node.RightChild.Parent = current_node
            del result_node
            self.Root = current_node
            return True      
        if (    current_node.LeftChild == None
            and current_node.RightChild == None
            and key_search_result_parent_type == "left_child"
           ):
            current_node.Parent.LeftChild = None
            current_node.Parent = result_node.Parent
            current_node.LeftChild = result_node.LeftChild
            current_node.RightChild = result_node.RightChild
            result_node.Parent.LeftChild = current_node
            result_node.LeftChild.Parent = current_node
            result_node.RightChild.Parent = current_node
            del result_node
            return True      
        if (    current_node.LeftChild == None
            and current_node.RightChild == None
           ):
            current_node.Parent.LeftChild = None
            current_node.Parent = result_node.Parent
            current_node.LeftChild = result_node.LeftChild
            current_node.RightChild = result_node.RightChild
            result_node.Parent.RightChild = current_node
            result_node.LeftChild.Parent = current_node
            result_node.RightChild.Parent = current_node
            del result_node
            return True      
        if (    current_node.LeftChild == None
            and current_node.RightChild != None
            and key_search_result_parent_type == None
           ):
            current_node.Parent.LeftChild = current_node.RightChild
            current_node.RightChild.Parent = current_node.Parent
            current_node.Parent = None
            current_node.LeftChild = result_node.LeftChild
            current_node.RightChild = result_node.RightChild
            result_node.LeftChild.Parent = current_node
            result_node.RightChild.Parent = current_node
            del result_node
            self.Root = current_node
            return True      
        if (    current_node.LeftChild == None
            and current_node.RightChild != None
            and key_search_result_parent_type == "left_child"
           ):
            current_node.Parent.LeftChild = current_node.RightChild
            current_node.RightChild.Parent = current_node.Parent
            current_node.Parent = result_node.Parent
            current_node.LeftChild = result_node.LeftChild
            current_node.RightChild = result_node.RightChild
            result_node.Parent.LeftChild = current_node
            result_node.LeftChild.Parent = current_node
            result_node.RightChild.Parent = current_node
            del result_node
            return True      
        if (    current_node.LeftChild == None
            and current_node.RightChild != None
           ):
            current_node.Parent.LeftChild = current_node.RightChild
            current_node.RightChild.Parent = current_node.Parent
            current_node.Parent = result_node.Parent
            current_node.LeftChild = result_node.LeftChild
            current_node.RightChild = result_node.RightChild
            result_node.Parent.RightChild = current_node
            result_node.LeftChild.Parent = current_node
            result_node.RightChild.Parent = current_node
            del result_node
            return True      
        return self.DeleteNodeByKey_recursion(current_node.LeftChild, 
                                         result_node,
                                         key_search_result_parent_type
                                        )

    def Count(self):
        # количество узлов в дереве
        nodes_count = 0
        if self.Root == None:
            return nodes_count
        current_node = self.Root
        return self.Count_recursion(current_node, nodes_count)

    def Count_recursion(self, current_node, nodes_count):
        nodes_count += 1
        if (    current_node.LeftChild == None
            and current_node.RightChild == None
           ):
            return nodes_count
        if current_node.LeftChild != None:
            nodes_count = self.Count_recursion(current_node.LeftChild, nodes_count)
        if current_node.RightChild != None:
            nodes_count = self.Count_recursion(current_node.RightChild, nodes_count)
        return nodes_count

