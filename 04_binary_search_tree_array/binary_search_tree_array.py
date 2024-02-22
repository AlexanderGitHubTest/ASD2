"""
Binary search tree (2).
"""

class aBST:

    def __init__(self, depth):
        if depth <= 0:    
            tree_size = 0
            self._depth = 0
        if depth > 0:    
            tree_size = 2 ** depth - 1
            self._depth = depth
        self.Tree = [None] * tree_size # массив ключей
	
    def FindKeyIndex(self, key):
        # ищем в массиве индекс ключа
        if self._depth == 0:
            return None
        current_id = 0
        current_depth = 1
        return self.FindKeyIndex_recursion(key, current_id, current_depth)

    def FindKeyIndex_recursion(self, key, current_id, current_depth):
        if self.Tree[current_id] == key:
            return current_id
        if self.Tree[current_id] == None:
            return -current_id
        if current_depth == self._depth:
            return None
        if key < self.Tree[current_id]:
            return self.FindKeyIndex_recursion(key, 2*current_id + 1, current_depth + 1)
        if key > self.Tree[current_id]:
            return self.FindKeyIndex_recursion(key, 2*current_id + 2, current_depth + 1)
	
    def AddKey(self, key):
        # добавляем ключ в массив
        # метод возвращает индекс добавленного/существующего ключа или -1 если не удалось
        find_key_result = self.FindKeyIndex(key)
        if find_key_result == None:
            return -1
        if (find_key_result > 0
            or (find_key_result == 0
                and self.Tree[0] == key
               )
           ):
            return find_key_result
        self.Tree[-find_key_result] = key
        return -find_key_result

