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
        pass

    def are_friends(self, panda1, panda2):
        pass

    def friends_of(self, panda):
        pass