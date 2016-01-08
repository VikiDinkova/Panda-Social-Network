from panda import Panda
from collections import deque
import json


class PandaSocialNetwork:

    def __init__(self):
        self.social_network = self.load("social_network.json") # за да работим с предишния network

    def add_panda(self, panda):
        if self.has_panda(panda):
            return "This Panda already there"
        else:
            self.social_network[panda] = []

    def has_panda(self, panda):
        if panda in self.social_network:  # Проверка дали е в SN
            return True
        else:
            return False

    def make_friends(self, panda1, panda2):
        if not self.has_panda(panda1):  #
            self.add_panda(panda1)
        elif not self.has_panda(panda2):
            self.add_panda(panda2)
        else:
            if self.are_friends(panda1, panda2):
                return "Pandas are alredy friends"
            else:
                self.social_network[panda1].append(panda2)  # не съм сигурен дали е така
                self.social_network[panda2].append(panda1)

    def are_friends(self, panda1, panda2):
        if panda1 in self.social_network[panda2]:
            return True
        else:
            return False

    def friends_of(self, panda):
        if panda in self.social_network:
            return self.social_network[panda]
        else:
            return False

    def connection_level(self, panda1, panda2):
        visited = set()
        queue = deque()
        visited.add(panda1)
        queue.append((0, panda1))

        while len(queue) != 0:
            node_with_lvl = queue.popleft()
            node = node_with_lvl[1]
            level = node_with_lvl[0]
            if node == panda2:
                return level
            for neighbour in self.social_network[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append((level + 1, neighbour))

        return -1

    def are_connected(self, panda1, panda2):
        if self.level > 0:
            return True
        return False

    def how_many_gender_in_network(level, panda, gender):
        pass

    def save(self, filename):
        with open(filename, "w") as f:
            json.dump(str(self.social_network), f)

    def load(self, filename):
        with open(filename, 'r') as f:
            data = json.load(f)
        return data



def main():
    network = PandaSocialNetwork()

if __name__ == '__main__':
    main()
