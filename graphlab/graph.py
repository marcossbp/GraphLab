class Graph:

    def __init__(self, directed=False):
        self.directed = directed
        self.adj = {}
    
    def add_node(self, node):
        if node not in self.adj:
            self.adj[node] = {} # Add a node with no adjacent nodes
    
    def add_edge(self, node1, node2, weight = 1):
        # you can add two nodes to the graph by adding an edge between them
        self.add_node(node1) 
        self.add_node(node2)

        self.adj[node1][node2] = weight

        if not self.directed:
            self.adj[node2][node1] = weight
    
    def neighbors(self, node):
        return self.adj.get(node, {})

    def nodes(self):
        return list(self.adj.keys())
    
    def edges(self):
        return self.adj.items() # Implement class