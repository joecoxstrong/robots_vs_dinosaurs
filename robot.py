from weapon import Weapon

class Robot:
    def __init__(self, name, weapon_name, attack_power):
        self.name = name
        self.health = 100
        self.weapon = Weapon(weapon_name, attack_power)
    
    def robot_attack(self, dinosaur):
        dinosaur.health -= self.weapon.attack_power 

