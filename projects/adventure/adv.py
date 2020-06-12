from room import Room
from player import Player
from world import World
from util import Stack, Queue

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "projects/adventure/maps/test_line.txt"
map_file = "projects/adventure/maps/test_cross.txt"
# map_file = "projects/adventure/maps/test_loop.txt"
# map_file = "projects/adventure/maps/test_loop_fork.txt"
# map_file = "projects/adventure/maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)


class RoomGraph:
    def __init__(self):
        # self.last_id = 0
        self.rooms = {}
        # self.exits = {'n': '?', 's': '?', 'e': '?', 'w': '?'}

    # def add_exit(self, current_room, direction):
    #     # self.rooms[current_room].add(direction)
    #     self.rooms[current_room][direction] = '?'

    def add_exit(self, current_room, direction, exit_room):
        # exit room likely hasn't been added yet, so add
        if exit_room not in self.rooms:
            self.add_room(exit_room)

        # this sets both the current room and exit room ID as the value to the respective direction
        if direction == 'n':
            self.rooms[current_room]['n'] = exit_room
            self.rooms[exit_room]['s'] = current_room

        if direction == 's':
            self.rooms[current_room]['s'] = exit_room
            self.rooms[exit_room]['n'] = current_room

        if direction == 'e':
            self.rooms[current_room]['e'] = exit_room
            self.rooms[exit_room]['w'] = current_room

        if direction == 'w':
            self.rooms[current_room]['w'] = exit_room
            self.rooms[exit_room]['e'] = current_room

    def add_room(self, room):
        if room not in self.rooms:
            self.rooms[room] = {}

    def get_neighbors(self, room):
        return self.rooms[room]

    def dfs(self, starting_room, final_room):

        rooms_to_visit = Queue()

        exits = dict()
        exits[starting_room] = []

        rooms_visited = set()

        rooms_to_visit.enqueue(starting_room)

        while rooms_to_visit.size() > 0:

            current_room = rooms_to_visit.dequeue()

            # find neighbors until we find destiantion to find PATH between
            if current_room not in rooms_visited:

                rooms_visited.add(current_room)

                neighbors = self.get_neighbors(current_room)

                for direction in neighbors:

                    neighbor = neighbors[direction]

                    if neighbor == final_room:
                        final_path = [*exits[current_room]]

                        final_path.append(current_room)
                        # print("current_room", current_room)
                        final_path.append(neighbor)
                        # print("neighbor", neighbor)
                        # print("FP1", final_path)
                        # print("FP2", final_path[1:-1])

                        # don't return starting room or destination room because we only need the path between
                        return final_path[1:-1]

                    # add neighbors to queue
                    rooms_to_visit.enqueue(neighbor)

                    # keep track of exits/path so far for each neighbor
                    copy_of_exit = [*exits[current_room]]
                    copy_of_exit.append(current_room)

                    # exits taken to get to neighbor stored in dict
                    exits[neighbor] = copy_of_exit

        print("Not found!!!!")
        return


# Fill this out with directions to walk
# traversal_path = ['n', 'n']


# print("room", player.current_room.id)


def maze_traversal(player):

    traversal_path = []

    # store visited rooms
    graph = RoomGraph()

    # create dict of rooms visited
    rooms_visited = dict()

    # stack for rooms to visit
    rooms_to_visit = Stack()

    # push current room onto stack
    rooms_to_visit.push(player.current_room)

    previous_room = None

    while rooms_to_visit.size() > 0:

        # pop off current room
        current_room = rooms_to_visit.pop()

        if current_room.id not in rooms_visited:

            # make sure you can move to room
            if previous_room is not None:

                can_move = False
                # exit_to_use = None

                # loop through exits from previous room to get to new room
                for room_exit in previous_room.get_exits():

                    connecting_room = previous_room.get_room_in_direction(
                        room_exit)

                    if connecting_room.id == current_room.id:
                        can_move = True
                        # exit_to_use = room_exit

                # can't get there that way, find shortest path that does get there using DFS
                if not can_move:

                    # DFS of path
                    room_path = graph.dfs(previous_room.id, current_room.id)

                    traversal_path = traversal_path + room_path

            rooms_visited[current_room.id] = current_room

            graph.add_room(current_room.id)

            traversal_path.append(current_room.id)

            for room_exit in current_room.get_exits():

                connecting_room = current_room.get_room_in_direction(room_exit)

                # graph.add_exit(current_room.id, room_exit)
                # MAYBE NEED TO COMBINE ADD EXIT AND UPDATE EXIT
                graph.add_exit(current_room.id, room_exit,
                               connecting_room.id)

                rooms_to_visit.push(connecting_room)

            previous_room = current_room
    print(graph.rooms)
    # need to turn rooms into directions
    traversal_directions = []

    for i in range(0, len(traversal_path) - 1):

        previous_room = traversal_path[i]
        current_room = traversal_path[i + 1]

        neighbors = graph.get_neighbors(previous_room)

        for direction in neighbors:
            if neighbors[direction] == current_room:
                traversal_directions.append(direction)

    print("traversal path", traversal_path)
    print("traversal directions", traversal_directions)
    print("done")

    return (traversal_path, traversal_directions)
    # rooms_visited.add(current_room)
    # graph.add_room(current_room)
    # current_room_exits = player.current_room.get_exits()

    # for room_exit in current_room_exits:
    #     graph.add_exit(current_room, room_exit)
    #     print(graph.rooms[current_room])

    # player.travel(room_exit)
    # next_room = player.current_room.id
    # next_room_exits = player.current_room.get_exits()
    # graph.add_room(next_room)

    # for next_room_exit in next_room_exits:
    #     graph.add_exit(next_room, next_room_exit)

    # rooms_to_visit.push(next_room)

# room_exit is a cardinal direction

# rooms_to_visit.push(next_room)


# traversal_path.append(room_exit)
# player.travel(room_exit)

traversal_path, traversal_directions = maze_traversal(player)

traversal_path = traversal_directions

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
