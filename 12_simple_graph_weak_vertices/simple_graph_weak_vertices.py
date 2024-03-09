"""
Simple graph (weak vertices).
"""

from collections import deque
from functools import reduce

class Vertex:

    def __init__(self, val):
        self.Value = val
        self.Hit = False
  
class SimpleGraph:
	
    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None] * size
        
    def AddVertex(self, v):
        # код добавления новой вершины 
        # с значением value 
        # в свободное место массива vertex
        self.vertex[self.vertex.index(None)] = Vertex(v)
	
    # здесь и далее, параметры v -- индекс вершины
    # в списке  vertex
    def RemoveVertex(self, v):
        # код удаления вершины со всеми её рёбрами
        self.vertex[v] = None
        for vertex_id in range(self.max_vertex):
            if self.IsEdge(v, vertex_id):
                self.RemoveEdge(v, vertex_id)
	
    def IsEdge(self, v1, v2):
        # True если есть ребро между вершинами v1 и v2
        return (    self.m_adjacency[v1][v2] == 1
                and self.m_adjacency[v2][v1] == 1
               )
	
    def AddEdge(self, v1, v2):
        # добавление ребра между вершинами v1 и v2
        self.m_adjacency[v1][v2] = 1
        self.m_adjacency[v2][v1] = 1
	
    def RemoveEdge(self, v1, v2):
        # удаление ребра между вершинами v1 и v2
        if self.IsEdge(v1, v2):
            self.m_adjacency[v1][v2] = 0
            self.m_adjacency[v2][v1] = 0

    def DepthFirstSearch(self, VFrom, VTo):
        # узлы задаются позициями в списке vertex
        # возвращается список узлов -- путь из VFrom в VTo
        # или [] если пути нету
        for vertex in self.vertex:
            vertex.Hit = False
        stack = []
        return self.DepthFirstSearch_recursion(VFrom, VTo, VFrom, stack)

    def DepthFirstSearch_recursion(self, VFrom, VTo, current_vertex_id, stack):
        self.vertex[current_vertex_id].Hit = True
        stack.append(self.vertex[current_vertex_id])
        vertex_adjacency_ids = []
        for vertex_id, vertex_adjacency in enumerate(self.m_adjacency[current_vertex_id]):
            if vertex_adjacency == 1:
                vertex_adjacency_ids.append(vertex_id)
        if vertex_adjacency_ids.count(VTo) > 0:
            stack.append(self.vertex[VTo])          
            return stack
        vertex_adjacency_not_visited_ids = []
        for vertex_id in vertex_adjacency_ids:
            if not self.vertex[vertex_id].Hit:
                vertex_adjacency_not_visited_ids.append(vertex_id)
        if vertex_adjacency_not_visited_ids == []:
            stack.pop()
            return stack
        for vertex_id in vertex_adjacency_not_visited_ids:
            self.DepthFirstSearch_recursion(VFrom, VTo, vertex_id, stack)
            if stack[-1] == self.vertex[VTo]:
                break
        if stack == []:
            return []
        if stack[-1] != self.vertex[VTo]:
            stack.pop()
        return stack

    def BreadthFirstSearch(self, VFrom, VTo):
        # узлы задаются позициями в списке vertex
        # возвращается список узлов -- путь из VFrom в VTo
        # или [] если пути нету
        for vertex in self.vertex:
            vertex.Hit = False
        current_vertex_id = VFrom
        self.vertex[current_vertex_id].Hit = True
        queue = deque()
        result_list = []
        return self.BreadthFirstSearch_recursion(VTo, queue, current_vertex_id, result_list)

    def BreadthFirstSearch_recursion(self, VTo, queue, current_vertex_id, result_list):
        result_list.append(self.vertex[current_vertex_id])
        vertex_adjacency_not_visited_ids = []
        for vertex_id, vertex_adjacency in enumerate(self.m_adjacency[current_vertex_id]):
            if vertex_adjacency == 1 and not self.vertex[vertex_id].Hit:
                vertex_adjacency_not_visited_ids.append(vertex_id)
        if vertex_adjacency_not_visited_ids == []:
            result_list.pop()
        for vertex_id in vertex_adjacency_not_visited_ids:
            if vertex_id == VTo:
                result_list.append(self.vertex[VTo])
                return result_list
            self.vertex[vertex_id].Hit = True
            queue.append(vertex_id)
        if len(queue) == 0:
            return []
        new_current_vertex_id = queue.popleft()
        return self.BreadthFirstSearch_recursion(VTo, queue, new_current_vertex_id, result_list)

    @staticmethod
    def convert_binary_number_into_integer(list_of_zeros_and_ones):
        # convert binary number represented by list of zeros and ones into integer
        return reduce(lambda a, b: a + b, 
                      map(lambda x: x[1] * 2 ** x [0], 
                          enumerate(reversed(list_of_zeros_and_ones))
                         ),
                      0
                     )

    def WeakVertices(self):
        # возвращает список узлов вне треугольников
        result_weak_vertices = []
        for vertex_id, vertex in enumerate(self.vertex):
            # сразу считаем текущую вершину "слабой"
            result_weak_vertices.append(vertex)
            # список индексов связных с текущей вершин
            vertex_adjacency_ids = []
            for vertex_adjacency_id, vertex_adjacency in enumerate(self.m_adjacency[vertex_id]):
                if vertex_adjacency == 1:
                    vertex_adjacency_ids.append(vertex_adjacency_id)
            # для использования бинарных операций преобразуем список связности
            # текущей вершины в int, результат будет маской для сравнения
            mask = self.convert_binary_number_into_integer(self.m_adjacency[vertex_id])
            # если больше нуля результат от бинарного "И" маски
            # (списка связности текущей вершины)
            # и списка связности хотя бы одной из связных вершин, 
            # то текущая вершина НЕ слабая и из списка её убираем
            for vertex_adjacency_id in vertex_adjacency_ids:
                # для использования бинарных операций преобразуем 
                # список связности связной вершины в int
                vertex_adjacency_as_int = self.convert_binary_number_into_integer(self.m_adjacency[vertex_adjacency_id])
                if mask & vertex_adjacency_as_int > 0:
                    result_weak_vertices.pop()
                    break
        return result_weak_vertices

