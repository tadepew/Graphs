from graph import Graph
from util import Queue, Stack


def earliest_ancestor(ancestors, starting_node):
    graph = Graph()

    verts = set()

    # hashtable to store paths to each vert
    paths_to_ancestors = {}

    for parent, child in ancestors:

        if parent not in verts:
            verts.add(parent)

        if child not in verts:
            verts.add(child)

    # ------
    # initialize graph:

   # for each vertex
    for v in verts:
        # add v to graph
        graph.add_vertex(v)
        # list for paths
        paths_to_ancestors[v] = []

    # add edges to graph
    # child vert points to parent
    # v1, v2
    for parent, child in ancestors:
        graph.add_edge(child, parent)

    # ------
    # graph initialized with tuples of parent child pairs

    # queue for verticies
    # we need to use a queue since we are looking at length, although this time it is longest not shortest
    verts_to_visit = Queue()

    # initialize queue with starting vert
    verts_to_visit.enqueue(starting_node)

    while verts_to_visit.size() > 0:

        # dequeue next vert to traverse
        current_vertex = verts_to_visit.dequeue()

        # find all parents to the starting node
        for parent in graph.get_neighbors(current_vertex):

            # update path from child to parent with a shallow copy of path so far
            path_so_far = [*paths_to_ancestors[current_vertex]]

            path_so_far.append(current_vertex)

            # add path to hashtable
            paths_to_ancestors[parent] = path_so_far

            # add parent to queue
            verts_to_visit.enqueue(parent)

        # no more child verts
        # add current vertex to end of path to finish the path
        final_path = [*paths_to_ancestors[current_vertex]]
        # final path so far is paths to farthest ancestor up to current vertex
        final_path.append(current_vertex)
        paths_to_ancestors[current_vertex] = final_path

    # search for the longest path
    longest_path = []

    # iterate through hashtable of paths
    for v in paths_to_ancestors:

        # store current path
        current_path = paths_to_ancestors[v]

        # update longest path if a longer one is found
        if len(current_path) > len(longest_path):
            longest_path = current_path

    # return 1 if length of path is 1, meaning there is no parent
    if len(longest_path) == 1:
        return -1

    # OTHERWISE, return furthest ancestor, aka the last item in the list of paths
    return longest_path[-1]
