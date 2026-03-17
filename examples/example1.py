from graphlab.graph import Graph

g = Graph()
g.add_node("A")
g.add_node("B")
g.add_edge("A", "B")

print(g.directed)
print(g.adj)
print(g.neighbors("A"))

print(g.nodes())
print(g.edges())