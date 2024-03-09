#Without weights

class Graph:
    def __init__(self):
        self.adjacency_list = {}
    
    def add_node(self, node_value) -> None:
        if node_value not in self.adjacency_list:
            self.adjacency_list[node_value] = []
    
    def add_edge(self, vertex1, vertex2) -> None:
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)
    
    def print_graph(self) -> None:
        for vertex in self.adjacency_list:
            print(f"vertex : {vertex} --> connections: {self.adjacency_list[vertex]}")


if __name__ == "__main__":
    G = Graph()
    G.add_node(1)
    G.add_node(2)
    G.add_node(3)
    
    G.add_edge(1,2)
    G.add_edge(2,3)
    
    G.print_graph()

    