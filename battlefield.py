from fleet import Fleet
from herd import Herd
import random

class Battlefield: 
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()


    def run_games(self):
        self.robot_list = self.fleet.robots
        self.dino_list = self.herd.dinosaurs

        self.display_welcome()

        self.battle()

    def display_welcome(self):
        print(f"Let's get ready to rumble!!!")


    def battle(self): #randomly choose who get's to attack
        while len(self.fleet.robots) > 0 and len(self.herd.dinosaurs) > 0:
            dice_roll = random.randint(1,10)
            if dice_roll % 2 == 0:
                self.robo_turn()
            else:
                self.dino_turn()
                

    def dino_turn(self):
        self.show_dino_opponent_options()
        select_dino = int(input('Select a Dinosaur to attack with. '))
        self.show_robo_opponent_options
        select_robot = int(input('Select a Robot to attack. '))
        self.herd.dinosaurs[select_dino].attack(self.fleet.robots[select_robot])

        if self.fleet.robots[select_robot].health <= 0:
            print(f'{self.fleet.robots[select_robot]} has been eliminated!')
            self.fleet.robots[select_robot].remove(self.fleet.robots)

    def robo_turn(self):
        self.show_robo_opponent_options()
        select_robot = int(input('Select a Robot to Attack with. '))
        self.show_dino_opponent_options()
        select_dino = int(input('Select a Robot to attack. '))
        self.fleet.robots[select_robot].attack(self.herd.dinosaurs[select_dino])

        if self.herd.dinosaurs[select_dino].health <= 0:
            print(f'{self.herd.dinosaurs[select_dino]} has been eliminated!')
            self.herd.dinosaurs[select_dino].remove(self.herd.dinosaurs)


    def show_dino_opponent_options(self):
        print('Select a Dinosaur.')
        index = 0
        for dinosaur in self.herd.dinosaurs:
            print(f'Press {index} for {dinosaur.name} with {dinosaur.health}.')

    def show_robo_opponent_options(self):
        print('Select a Robot.')
        index = 0
        for robot in self.fleet.robots:
            print(f'Press {index} for {robot.name} with {robot.health}.')


    def dispaly_winner(self):
        if len(self.fleet.robots) == 0:
            print('Dinosaurs win!')
        elif len(self.herd.dinosaurs) == 0:
            print('Robots win!')
                



