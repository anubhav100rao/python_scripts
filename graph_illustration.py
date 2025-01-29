import networkx as nx
import matplotlib.pyplot as plt

# Create a graph
G = nx.Graph()

# Add edges (and nodes implicitly)
G.add_edges_from([[0, 1], [2, 0], [3, 2], [3, 6], [
                 8, 7], [4, 8], [5, 4], [3, 5], [3, 9]])

# Draw the graph
nx.draw(G, with_labels=True, node_color='lightblue',
        edge_color='gray', node_size=2000)
plt.show()


GG = nx.Graph()
GG.add_edges_from([[0, 1], [0, 2], [0, 3]])
nx.draw(GG, with_labels=True, node_color='green',
        edge_color='gray', node_size=2000)
