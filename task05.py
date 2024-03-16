import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def visualize_tree_traversals(root, traversal_type='dfs'):
    # Create a graph object
    G = nx.Graph()

    # Function to add edges to the graph recursively
    def add_edges(node, pos, level=1):
        if node:
            G.add_node(node.val, pos=pos)
            if node.left:
                left_pos = (pos[0] - 1 / 2 ** level, pos[1] - 1)
                G.add_edge(node.val, node.left.val)
                add_edges(node.left, left_pos, level + 1)
            if node.right:
                right_pos = (pos[0] + 1 / 2 ** level, pos[1] - 1)
                G.add_edge(node.val, node.right.val)
                add_edges(node.right, right_pos, level + 1)

    # Call the function to add edges starting from the root
    add_edges(root, (0, 0))

    # Get the positions of nodes in the graph
    pos = nx.get_node_attributes(G, 'pos')
    colors = {}

    # Perform DFS traversal
    if traversal_type == 'dfs':
        # Dictionary to store depth of nodes
        depth = {}
        # Calculate the depth of each node using DFS
        for node in nx.dfs_preorder_nodes(G, source=root.val):
            depth[node] = nx.shortest_path_length(G, source=root.val, target=node)
        # Find the maximum depth
        max_depth = max(depth.values())
        # Assign colors based on the depth
        for idx, (node, d) in enumerate(depth.items()):
            # Generate color based on depth
            color = "#{:02x}{:02x}{:02x}".format(255, int(200 * (d / max_depth)), int(200 * (d / max_depth)))
            colors[node] = color
            # Display the step number
            plt.text(pos[node][0] + 0.18, pos[node][1] - 0.18, f'step: {idx + 1}', fontsize=10, ha='center', va='center', color='grey')
        traversal_desc = 'Depth First Traversal'

    # Perform BFS traversal
    elif traversal_type == 'bfs':
        # Use a queue for BFS traversal
        queue = deque([root])
        visited = set()
        level = 0
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                visited.add(node)
                # Generate color based on level
                color = "#{:02x}{:02x}{:02x}".format(255, int(255 * (level / len(pos)) * 2), int(255 * ((level + 1) / len(pos)) * 2))
                colors[node.val] = color
                # Display the step number
                plt.text(pos[node.val][0] + 0.18, pos[node.val][1] - 0.18, f'step: {level + 1}', fontsize=10, ha='center', va='center', color='grey')
                for child in [node.left, node.right]:
                    if child and child not in visited:
                        queue.append(child)
            level += 1
        traversal_desc = 'Breadth First Traversal'

    # Draw the graph with node colors
    nx.draw(G, pos, with_labels=True, node_color=list(colors.values()), node_size=800, font_size=10)
    plt.title(traversal_desc)
    plt.show()

# Example of usage:
# First, let's build a binary tree
root = Node(0)
root.left = Node(4)
root.right = Node(2)
root.left.left = Node(5)
root.left.right = Node(7)
root.right.left = Node(6)
root.right.right = Node(10)
root.left.left.left = Node(12)
root.left.left.right = Node(8)

# Now let's visualize the tree traversals
visualize_tree_traversals(root, traversal_type='dfs')  # Depth First Traversal
visualize_tree_traversals(root, traversal_type='bfs')  # Breadth First Traversal
