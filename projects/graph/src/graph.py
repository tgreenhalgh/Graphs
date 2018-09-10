"""
Simple graph implementation compatible with BokehGraph class.
"""
import sys


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex] = set()

    def add_edge(self, vertex1, vertex2):
        if vertex1 not in self.vertices:
            sys.exit("No '{}' vertex!".format(vertex1))
        elif vertex2 not in self.vertices:
            sys.exit("No '{}' vertex!".format(vertex2))
        else:
            self.vertices[vertex1].add(vertex2)
            self.vertices[vertex2].add(vertex1)


graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
print(graph.vertices)