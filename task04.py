import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="salmon"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color

def visualize_heap(root):
    G = nx.Graph()

    def add_edges(node, pos, level=1):
        if node:
            G.add_node(node.val, pos=pos, color=node.color)
            if node.left:
                left_pos = (pos[0] - 1 / 2 ** level, pos[1] - 1)
                G.add_edge(node.val, node.left.val)
                add_edges(node.left, left_pos, level + 1)
            if node.right:
                right_pos = (pos[0] + 1 / 2 ** level, pos[1] - 1)
                G.add_edge(node.val, node.right.val)
                add_edges(node.right, right_pos, level + 1)

    add_edges(root, (0, 0))

    pos = nx.get_node_attributes(G, 'pos')
    colors = nx.get_node_attributes(G, 'color').values()
    nx.draw(G, pos, with_labels=True, node_color=colors, node_size=800, font_size=10)
    plt.show()

# Example of use:
# First, let's build a binary heap
root = Node(0)
root.left = Node(4)
root.right = Node(2)
root.left.left = Node(5)
root.left.right = Node(7)
root.right.left = Node(6)
root.right.right = Node(10)
root.left.left.left = Node(12)
root.left.left.right = Node(8)

# Now let's visualise the pile
visualize_heap(root)
