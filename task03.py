import heapq
import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_list = {v: {} for v in vertices}
        self.graph = nx.Graph()

    def add_edge(self, u, v, weight):
        self.adjacency_list[u][v] = weight
        self.adjacency_list[v][u] = weight
        self.graph.add_edge(u, v, weight=weight)

    def dijkstra(self, source):
        distances = {v: float('inf') for v in self.vertices}
        distances[source] = 0

        heap = [(0, source)]

        while heap:
            current_distance, current_vertex = heapq.heappop(heap)

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.adjacency_list[current_vertex].items():
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(heap, (distance, neighbor))

        return distances

    def visualize_graph(self, source_vertex, shortest_distances):
        pos = nx.spring_layout(self.graph)
        nx.draw(self.graph, pos, with_labels=True, node_color='skyblue', node_size=800, edge_color='k', font_size=10)
        labels = nx.get_edge_attributes(self.graph, 'weight')
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=labels)
        plt.title('Shortest distances from vertex ' + source_vertex)
        plt.xlabel('From vertex')
        plt.ylabel('To vertex')
        plt.text(0.5, 0.95, 'From vertex ' + source_vertex + ' to other vertices:', horizontalalignment='center', transform=plt.gca().transAxes)
        
        for vertex, distance in shortest_distances.items():
            plt.text(pos[vertex][0], pos[vertex][1] + 0.1, f"from {source_vertex} to {vertex}: {distance}", horizontalalignment='center', fontsize=8, color='red')
        
        plt.show()

# Example of use
vertices = ['A', 'B', 'C', 'D', 'E']
graph = Graph(vertices)
graph.add_edge('A', 'B', 4)
graph.add_edge('A', 'C', 2)
graph.add_edge('B', 'C', 5)
graph.add_edge('B', 'D', 10)
graph.add_edge('C', 'D', 3)
graph.add_edge('C', 'E', 6)
graph.add_edge('D', 'E', 8)

source_vertex = 'D'
shortest_distances = graph.dijkstra(source_vertex)
print("Shortest distances from vertex", source_vertex + ":")
for vertex, distance in shortest_distances.items():
    print("From vertex", source_vertex, "to vertex", vertex + ":", distance)

graph.visualize_graph(source_vertex, shortest_distances)
