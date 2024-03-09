#With weights

class Graph:
    def __init__(self) -> None:
        self.list = {}
    
    def add_node(self, data) -> None:
        if data not in self.list:
            self.list[data] = []
    
    def add_edge(self, vertex1, vertex2, weight) -> None:
        if vertex1 in self.list and vertex2 in self.list:
            self.list[vertex1].append([vertex2, weight])
            self.list[vertex2].append([vertex1, weight])
    
    def print_graph(self) -> None:
        for vertex in self.list:
            print(f"vertex:{vertex} ---> connections:{self.list[vertex]}")
    

if __name__ == "__main__":
    G = Graph()
    G.add_node(1)
    G.add_node(2)
    G.add_node(3)
    
    G.add_edge(1, 2, 4)
    G.add_edge(1, 3, 5)
    
    G.print_graph()
    