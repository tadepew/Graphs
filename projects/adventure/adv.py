from room import Room
from player import Player
from world import World
from graph import Graph
from util import Stack

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

    def add_exit(self, current_room, direction):
        # self.rooms[current_room].add(direction)
        self.rooms[current_room][direction] = '?'

    def update_exit(self, current_room, direction, exit_room):
        if exit_room not in self.rooms:
            self.add_room(exit_room)

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

    def get_neighbord(self, room):
        return self.rooms[room]


# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

graph = RoomGraph()

# # initialize graph
# for room in range(0, len(room_graph)):
#     graph.add_room(room)
#     graph.add_exit(room, 'n', 1)

# print(graph.rooms)


rooms_visited = set()

rooms_to_visit = Stack()

rooms_to_visit.push(player.current_room.id)


while rooms_to_visit.size() > 0:
    current_room = rooms_to_visit.pop()

    if current_room not in rooms_visited:
        rooms_visited.add(current_room)
        graph.add_room(current_room)
        current_room_exits = player.current_room.get_exits()

        for room_exit in current_room_exits:
            graph.add_exit(current_room, room_exit)
            print(graph.rooms[current_room])

        player.travel(room_exit)
        next_room = player.current_room.id
        next_room_exits = player.current_room.get_exits()
        graph.add_room(next_room)

        for next_room_exit in next_room_exits:
            graph.add_exit(next_room, next_room_exit)

        rooms_to_visit.push(next_room)

# room_exit is a cardinal direction

# rooms_to_visit.push(next_room)

# traversal_path.append(room_exit)

# player.travel(room_exit)

print(graph.rooms)


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
