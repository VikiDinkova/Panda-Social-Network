from panda import Panda
from collections import deque
import json
import ast


class PandaSocialNetwork:

    def __init__(self):
        self.social_network = self.load("social_network.json")

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
                self.social_network[panda1].append(panda2)
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
        if self.connection_level(panda1, panda2) > 0:
            return True
        return False

    def level_d(self):
        level_dict = {}
        for panda in self.social_network:
            level_dict[panda] = {}
            for panda_fr in self.social_network:
                level_dict[panda][self.connection_level(panda, panda_fr)].append(panda_fr)
        return level_dict

    def how_many_gender_in_network(self, level, panda, gender):
        level_dict = self.level_d()
        counter = 0
        for friends in level_dict[panda][level]:
            if friends.gender() == gender:
                counter += 1
        return counter

    # TODO fix save method
    def save(self, filename="social_network.json"):
        net = {}
        x = []
        for key in self.social_network:
            for element in self.social_network[key]:
                x.append(element.__dict__)
            net[str(key.__dict__)] = x
            x = []
        with open(filename, "w") as f:
            json.dump(net, f, indent=4)

    def load(self, filename="social_network.json"):
        with open(filename, 'r') as f:
            data = json.load(f)

        return self._from_dict_to_object(data)

    def _from_dict_to_object(self, data):
        net = []
        new_social_network = {}
        for key in data:
            for element in data[key]:
                x = Panda(
                    element["_name"],
                    element["_email"],
                    element["_gender"])

                net.append(x)
            key = ast.literal_eval(key)  # преобразува стринг на дикт
            new_social_network[Panda(
                    key["_name"],
                    key["_email"],
                    key["_gender"])] = net
            net = []
        return new_social_network


def main():
    network = PandaSocialNetwork()
    print([str(x)for x in network.social_network])
if __name__ == '__main__':
    main()
