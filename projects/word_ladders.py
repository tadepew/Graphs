import string


class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


word_set = set()

with open('words.txt', 'r') as f:
    for line in f:
        line = line.strip()  # no newline
        word_set.add(line.lower())

letters = list(string.ascii_lowercase)


def get_neighbors(word):
    neighbors = []

    word_letters = list(word)

    # for each letter in the word
    for i in range(len(word_letters)):
        # replace with all english letters

        for letter in letters:
            # Copy the word letters
            t = list(word_letters)

            t[i] = letter

            w = "".join(t)

            # see if we form a word
            if w != word and w in word_set:
                neighbors.append(w)

    return neighbors


def find_word_ladders(begin_word, end_word):
    visited = set()

    q = Queue()

    q.enqueue([begin_word])
    # initalize queue with a list just with the beginning word

    while q.size() > 0:
        path = q.dequeue()

        cur_word = path[-1]  # get last node out of the path

        if cur_word not in visited:
            visited.add(cur_word)

            if cur_word == end_word:
                return path

            for neighbor in get_neighbors(cur_word):
                path_copy = [*path]  # copy the list so far
                path_copy.append(neighbor)
                q.enqueue(path_copy)

    return None
