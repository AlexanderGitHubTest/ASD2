"""
Heap.
"""

class Heap:

    def __init__(self):
        self.HeapArray = [] # хранит неотрицательные числа-ключи
		
    def MakeHeap(self, a, depth):
	# создаём массив кучи HeapArray из заданного
        # размер массива выбираем на основе глубины depth 
        size_of_array = 2 ** (depth + 1) - 1
        self.HeapArray = [None] * size_of_array
        for key in a:
            self.Add(key)
       
    def GetMax(self):
        # вернуть значение корня и перестроить кучу
        # если куча пуста, вернуть -1
        if len(self.HeapArray) == 0:
            return -1
        value_of_root = self.HeapArray[0]
        if value_of_root == None:
            return -1
        last_filled_node_id = len(self.HeapArray) - 1
        if self.HeapArray[last_filled_node_id] == None:
            last_filled_node_id = self.HeapArray.index(None) - 1
        if last_filled_node_id == 0:
            self.HeapArray[0] = None
            return value_of_root
        self.HeapArray[0] = self.HeapArray[last_filled_node_id]
        self.HeapArray[last_filled_node_id] = None
        self.GetMax_recursion(0)
        return value_of_root

    def _swap_places(self, first_place_id, second_place_id):
        (
         self.HeapArray[first_place_id], self.HeapArray[second_place_id]
        ) = (
             self.HeapArray[second_place_id], self.HeapArray[first_place_id]
            )

    def GetMax_recursion(self, test_node_id):
        left_child_id = 2 * test_node_id + 1
        if left_child_id >= len(self.HeapArray):
            return
        right_child_id = 2 * test_node_id + 2
        if (    self.HeapArray[left_child_id] == None 
            and self.HeapArray[right_child_id] == None
           ):
            return
        if (     self.HeapArray[left_child_id] == None
            and (self.HeapArray[right_child_id] <= self.HeapArray[test_node_id])  
           ):
            return
        if self.HeapArray[left_child_id] == None:
            self._swap_places(test_node_id, right_child_id)
            self.GetMax_recursion(right_child_id)
            return
        if (     self.HeapArray[right_child_id] == None
            and (self.HeapArray[left_child_id] <= self.HeapArray[test_node_id])  
           ):
            return
        if self.HeapArray[right_child_id] == None:
            self._swap_places(test_node_id, left_child_id)
            self.GetMax_recursion(left_child_id)
            return
        if (    (self.HeapArray[right_child_id] >= self.HeapArray[left_child_id])
            and (self.HeapArray[right_child_id] >  self.HeapArray[test_node_id])  
           ):
            self._swap_places(test_node_id, right_child_id)
            self.GetMax_recursion(right_child_id)
            return
        if (    (self.HeapArray[left_child_id] >= self.HeapArray[right_child_id])
            and (self.HeapArray[left_child_id] >  self.HeapArray[test_node_id])  
           ):
            self._swap_places(test_node_id, left_child_id)
            self.GetMax_recursion(left_child_id)
            return

    def Add(self, key):
        # добавляем новый элемент key в кучу и перестраиваем её
        # если куча вся заполнена, вернуть False
        if len(self.HeapArray) == 0:
            return False
        if self.HeapArray[-1] != None:
            return False
        first_available_id = self.HeapArray.index(None)
        self.HeapArray[first_available_id] = key
        self.Add_recursion(first_available_id)
        return True

    def Add_recursion(self, current_id):
        if current_id == 0:
            return
        parent_of_current_id = (current_id - 1) // 2
        if self.HeapArray[parent_of_current_id] > self.HeapArray[current_id]:
            return
        (self.HeapArray[parent_of_current_id], 
         self.HeapArray[current_id]
        ) = (self.HeapArray[current_id],
             self.HeapArray[parent_of_current_id]
            )
        self.Add_recursion(parent_of_current_id)

