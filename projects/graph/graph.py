"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # initialize a queue (fifo)
        # BFT processes closest vertices first and then moves outwards away from start
        # THEREFORE, you want to query (queue) oldest element based on the order they were inserted since it is first-in-first-out
        verts_to_visit = Queue()

        # enqueue first vert
        verts_to_visit.enqueue(starting_vertex)

        # this will store visited verts
        # no duplicates in set, keeping track of visited nodes
        verts_visited = set()

        while verts_to_visit.size() > 0:
            # dequeue vert off of queue
            current_vertex = verts_to_visit.dequeue()

            # if vert not already visited
            if current_vertex not in verts_visited:
                # visit/print vert
                print(current_vertex)

                # add vert to visited
                verts_visited.add(current_vertex)

                # enqueue all neighbors to visit
                for neighbor in self.get_neighbors(current_vertex):
                    verts_to_visit.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # a DFS explores as far as possible along each branch first and then bracktracks. For this, a stack works better since it is LIFO(last-in-first-out)
        # create a lifo stack
        verts_to_visit = Stack()

        # initialize with starting node/vert
        verts_to_visit.push(starting_vertex)

        # create a set of visited verts
        verts_visited = set()

        while verts_to_visit.size() > 0:
            # pop node off top of the stack
            current_vertex = verts_to_visit.pop()

            # if node isn't visited
            if current_vertex not in verts_visited:
                # visit/print node
                print(current_vertex)

                # mark as visited
                verts_visited.add(current_vertex)

                # push all neighbors on the stack
                for neighbor in self.get_neighbors(current_vertex):
                    verts_to_visit.push(neighbor)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """

        def dft_helper(starting_vertex):

            if starting_vertex not in verts_visited:
                print(starting_vertex)

                verts_visited.add(starting_vertex)

                for neighbor in self.get_neighbors(starting_vertex):
                    dft_helper(neighbor)

        verts_visited = set()

        dft_helper(starting_vertex)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        verts_to_visit = Queue()
        # initalize with starting vertex
        verts_to_visit.enqueue(starting_vertex)

        # hashtable for paths to verticies
        paths_to_verts = {}
        paths_to_verts[starting_vertex] = []

        verts_visited = set()

        while verts_to_visit.size() > 0:

            current_vertex = verts_to_visit.dequeue()

            if current_vertex not in verts_visited:
                verts_visited.add(current_vertex)

                for neighbor in self.get_neighbors(current_vertex):
                    if neighbor == destination_vertex:
                        final_path = paths_to_verts[current_vertex][:]
                        final_path.append(current_vertex)
                        final_path.append(neighbor)
                        return final_path
                    verts_to_visit.enqueue(neighbor)

                    copy_path = paths_to_verts[current_vertex][:]
                    copy_path.append(current_vertex)

                    paths_to_verts[neighbor] = copy_path

        print("Vertex not found")
        return

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
