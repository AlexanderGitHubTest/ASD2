"""
Simple graph.
"""

class Vertex:

    def __init__(self, val):
        self.Value = val
  
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
        if (   self.m_adjacency[v1][v2] == 0
            or self.m_adjacency[v2][v1] == 0
           ):
            return False
        return True
	
    def AddEdge(self, v1, v2):
        # добавление ребра между вершинами v1 и v2
        self.m_adjacency[v1][v2] = 1
        self.m_adjacency[v2][v1] = 1
	
    def RemoveEdge(self, v1, v2):
        # удаление ребра между вершинами v1 и v2
        if self.IsEdge(v1, v2):
            self.m_adjacency[v1][v2] = 0
            self.m_adjacency[v2][v1] = 0

