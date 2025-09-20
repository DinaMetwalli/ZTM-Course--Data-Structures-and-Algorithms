# Implementation of Graph Data Structure

'''
    (2)--(0)
    / \
  (1)-(3)
'''

# Edge list representation
graph = [[0, 2], [2, 3], [2, 1], [1, 3]]

# Adjacency list representation
graph = [[2], [2,3], [0,1,3], [1,2]]

graph = {
    0: [2],
    1: [2,3],
    2: [0,1,3],
    3: [1,2]
}

# Adjacency matrix representation
graph = {
    0: [0,0,1,0],
    1: [0,0,1,1],
    2: [1,1,0,1],
    3: [0,1,1,0]
}

class Graph:
    def __init__(self):
        self.number_of_nodes = 0
        self.adjacency_list = {}
    
    def add_vertex(self, node):
        self.adjacency_list[node] = []
        self.number_of_nodes += 1
    
    def add_edge(self, node1, node2):
        # undirected graph
        self.adjacency_list[node1].append(node2)
        self.adjacency_list[node2].append(node1)
    
    def show_connections(self):
        all_nodes = self.adjacency_list.keys()
        for node in all_nodes:
            node_connections = self.adjacency_list[node]
            connections = ""
            for vertex in node_connections:
                connections += f"{vertex} "
            print(f"{node} --> {connections}")

my_graph = Graph()
my_graph.add_vertex(0)
my_graph.add_vertex(1)
my_graph.add_vertex(2)
my_graph.add_vertex(3)
my_graph.add_vertex(4)
my_graph.add_vertex(5)
my_graph.add_vertex(6)
my_graph.add_edge(3, 1)
my_graph.add_edge(3, 4)
my_graph.add_edge(4, 2)
my_graph.add_edge(4, 5)
my_graph.add_edge(1, 2)
my_graph.add_edge(1, 0)
my_graph.add_edge(0, 2)
my_graph.add_edge(6, 5)

'''
(3)---(4)---(5)
 |     |     |
 |     |    (6)
(1)---(2)
  \   /
   (0)
'''
my_graph.show_connections()