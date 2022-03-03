from unicodedata import name
from xml.dom.domreg import well_known_implementations

from Weapon import Weapon


class Robot():
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = Weapon
    def attack(self, dinosaur):
        pass  