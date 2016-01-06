from panda import Panda


class PandaSocialNetwork:

    def __init__(self):
        self.social_network = {}

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
                self.social_network[panda1].append(panda2)  # не съм сигорен дали е така
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

    def conection_level(self, panda1, panda2):
        self.level = 0
        deque = deque()
        visit = set()

        deque.append(panda1)
        visit.append(panda1)
        while deque != []:
            for neighb in SOCIAL_NETWORK[panda1]:
                if neighb == panda2:
                    self.level += 1
                    return self.level
                else:
                    if SOCIAL_NETWORK[neighb] not in visit:
                        deque.append(SOCIAL_NETWORK[neighb])
                        if SOCIAL_NETWORK[neighb] != panda2:
                            visit.append(neighb)
                            deque.popleft()

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
def main():
    ivo = Panda("Ivo", "ivo@pandamail.com", "male")
    rado = Panda("Rado", "rado@pandamail.com", "male")
    network = PandaSocialNetwork()
    for panda in [ivo, rado]:
        network.add_panda(panda)

    network.make_friends(ivo, rado)

if __name__ == '__main__':
    main()
