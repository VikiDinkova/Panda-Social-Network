from panda import Panda

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
        if self.are_friends(panda1, panda2):
            return True
        else:
            SOCIAL_NETWORK[panda1].append(panda2)  # несъм сигорен дали е така
            SOCIAL_NETWORK[panda2].append(panda1)

    def are_friends(self, panda1, panda2):
        if panda1 in SOCIAL_NETWORK[panda2]:
            return True
        else:
            return False

    def friends_of(self, panda):
        pass
