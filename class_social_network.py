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
        if not self.has_panda(panda1):  #
            self.add_panda(panda1)
        elif not self.has_panda(panda2):
            self.add_panda(panda2)
        else:
            if self.are_friends(panda1, panda2):
                return "Pandas are alredy friends"
            else:
                SOCIAL_NETWORK[panda1].append(panda2)  # не съм сигорен дали е така
                SOCIAL_NETWORK[panda2].append(panda1)

    def are_friends(self, panda1, panda2):
        if panda1 in SOCIAL_NETWORK[panda2]:
            return True
        else:
            return False

    def friends_of(self, panda):
        pass

    def save(self, filename):
        pass

    def load(self, filename):
        pass
