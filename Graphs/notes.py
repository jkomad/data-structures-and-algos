"""  
1. Graphs: Intro 

Structure:
Vertex(Nodex)
Edge(Connection)

Vertex - Edge - Vertext 

A vertex can connect to (have an edge) with any number of other vertices. 

Edges between vertices can be weighted, which can influence the way traversal occurs between two vertices. 
Edges can also be directional or bidirectional. 

**trees are a form of graph, which means linked lists are also a form of graph (limitations to edges differentiate each data structure from one another)

2. Adjaceny Matrix 

If all edges between vertices in a graph are bidrectional, the adjaceny matrix will be symmetrical. 

The weights for weighted edges can be stored in the adjacency matrix. 

3. Adjaceny list

A dictionary composed of each vertex (key) which each has a list of all the vertices it has edges with (value)

4. Big O 

**Big difference between an adjaceny matrix and an adjaceny list is that in an adjacency matrix, each vertex has to store all of the verices it is not connected to (represented by zeroes)
Space Complexity: 
- Adjaceny Matrix - O(V^2)
- Adjecency List - O(V + E)
"""


class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
            return True
        return False

    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

    def remove_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False

    def remove_vertex(self, vertex):
        if vertex in self.adj_list.keys():
            for v in self.adj_list[vertex]:
                try:
                    self.adj_list[v].remove(vertex)
                except ValueError:
                    pass
            # for k in list(self.adj_list.keys()):
            #     try:
            #         self.adj_list[k].remove(vertex)
            #     except ValueError:
            #         pass
            del self.adj_list[vertex]
            return True
        return False

    def print_graph(self):
        print(self.adj_list)
        return


"""  
Quiz:

1. Adding a Vertex in a Graph with an Adjacency List is O(1)
TRUE - A vertex is represented as a key in an object (dictionary). Key lookup in an object is O(1)

2. Graphs are the go to data structure when you need to represent entities and the relationships between them
TRUE

3. Removing a vertex is O(1)
FALSE
"""

if __name__ == "__main__":
    my_graph = Graph()
    my_graph.add_vertex("A")
    my_graph.add_vertex("B")
    my_graph.add_vertex("C")
    my_graph.add_edge("A", "C")
    my_graph.remove_vertex("A")
    my_graph.print_graph()
