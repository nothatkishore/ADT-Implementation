class Node:
    def __init__(self, value):
        self.value = value
        self.edges = []


class Edge:
    def __init__(self, node, weight):
        self.node = node
        self.weight = weight


class Graph:
    def __init__(self):
        self.nodes = []

    def add_node(self, value):
        node = Node(value)
        self.nodes.append(node)
        return node

    def add_edge(self, source, destination, weight):
        source_node = None
        destination_node = None

        for node in self.nodes:
            if node.value == source:
                source_node = node
            if node.value == destination:
                destination_node = node

        if source_node is None:
            source_node = self.add_node(source)
        if destination_node is None:
            destination_node = self.add_node(destination)

        source_node.edges.append(Edge(destination_node, weight))


# Example usage:
graph = Graph()
graph.add_edge('A', 'B', 3)
graph.add_edge('A', 'C', 2)
graph.add_edge('B', 'C', 1)

print("Graph Nodes:")
for node in graph.nodes:
    print("Node:", node.value)
    print("Edges:")
    for edge in node.edges:
        print(f"-> {edge.node.value} (Weight: {edge.weight})")
