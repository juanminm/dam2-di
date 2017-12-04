class Player:
    def __init__(self, name, is_cpu):
        self.name = name
        self.is_cpu = is_cpu


class Human(Player):
    def __init__(self, name):
        Player.__init__(self, name, False)


class CPU(Player):
    def __init__(self):
        Player.__init__(self, "CPU", True)
