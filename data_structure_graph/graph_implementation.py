class Graph:
    def __init__(self):
        self.number_of_nodes = 0
        self.adjacency_list = {}
    
    def __str__(self):
        return str(self.__dict__)

    def add_vertex(self, node):
        self.number_of_nodes += 1
        self.adjacency_list[node] = []

    def add_edge(self, node1, node2):
        self.adjacency_list[node1].append(node2)
        self.adjacency_list[node2].append(node1)
    
    def show_connection(self):
        for vertex, neighbors in self.adjacency_list.items():
            print(vertex, end='-->')
            print(' '.join(neighbors))
        
graph = Graph()
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_vertex('4')
graph.add_vertex('5')
graph.add_vertex('6')
graph.add_edge('3', '1')
graph.add_edge('3', '4')
graph.add_edge('4', '2') 
graph.add_edge('4', '5') 
graph.add_edge('1', '2') 
graph.add_edge('1', '0') 
graph.add_edge('0', '2') 
graph.add_edge('6', '5')
print(graph)
graph.show_connection()