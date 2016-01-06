from panda import Panda
from collections import deque

SOCIAL_NETWORK = {}


class PandaSocialNetwork:

    def __init__(self):
        pass

    def add_panda(self, panda):
        if self.has_panda(panda):
            return "This Panda already there"
        else:
            SOCIAL_NETWORK[panda] = []

    def has_panda(self, panda):
        if panda in SOCIAL_NETWORK:  # Проверка дали е в SN
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
                SOCIAL_NETWORK[panda1].append(panda2)  # не съм сигурен дали е така
                SOCIAL_NETWORK[panda2].append(panda1)

    def are_friends(self, panda1, panda2):
        if panda1 in SOCIAL_NETWORK[panda2]:
            return True
        else:
            return False

    def friends_of(self, panda):
        if panda in SOCIAL_NETWORK:
            return SOCIAL_NETWORK[panda]
        else:
            return False

    def connection_level(self, panda1, panda2):
        self.level = 0
        deque2 = deque()
        visit = set()

        deque2.append(panda1)
        visit.append(panda1)
        while deque2 != []:
            for neighb in SOCIAL_NETWORK[panda1]:
                if neighb == panda2:
                    self.level += 1
                    return self.level
                else:
                    for nei in SOCIAL_NETWORK[neighb]:
                        if nei not in visit:
                            deque2.append(nei)
                            if nei != panda2:
                                visit.append(neighb)
                                deque2.popleft()
                                self.level += 1

    def are_connected(self, panda1, panda2):
        if self.level > 0:
            return True
        return False

    def how_many_gender_in_network(level, panda, gender):
        pass

    def save(self, filename):
        pass

    def load(self, filename):
        pass
