class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = int(attack_power)
        self.health = 100

    def attacks(self, robot):
        self.robot = robot

