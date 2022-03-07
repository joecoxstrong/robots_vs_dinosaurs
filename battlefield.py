from fleet import Fleet
from herd import Herd
import random

class Battlefield: 
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()
        self.chosen_dino_index = 0
        self.chosen_robot_index = 0

    def run_games(self):
        # self.robot_list = self.fleet.robots
        # self.dino_list = self.herd.dinosaurs

        self.display_welcome()

        self.battle()
        self.dispaly_winner()

    def display_welcome(self):
        print(f"Let's get ready to rumble!!!")


    def battle(self): #randomly choose who get's to attack
        while len(self.fleet.robots) > 0 and len(self.herd.dinosaurs) > 0:
            self.show_dino_opponent_options()
            self.show_robo_opponent_options()
            dice_roll = random.randint(1,10)
            if dice_roll % 2 == 0:
                self.robo_turn(self.chosen_robot_index)
            else:
                self.dino_turn(self.chosen_dino_index)
                

    def dino_turn(self,dinosaur_index):
       
        self.herd.dinosaurs[self.chosen_dino_index].dinosaur_attack(self.fleet.robots[self.chosen_robot_index])
        if self.fleet.robots[self.chosen_robot_index].health <= 0:
            print(f'{self.fleet.robots[self.chosen_robot_index].name} has been eliminated!')
            self.fleet.robots.pop(self.chosen_robot_index)

    def robo_turn(self,robot_index):
    
        self.fleet.robots[self.chosen_robot_index].robot_attack(self.herd.dinosaurs[self.chosen_dino_index])
        if self.herd.dinosaurs[self.chosen_dino_index].health <= 0:
            print(f'{self.herd.dinosaurs[self.chosen_dino_index].name} has been eliminated!')
            self.herd.dinosaurs.pop(self.chosen_dino_index)


    def show_dino_opponent_options(self):
        print('Dinosaur options: ')
        index = 0
        for dinosaur in self.herd.dinosaurs:
            print(f'Press {index} for {dinosaur.name} with {dinosaur.health}.')
            index += 1
        self.chosen_dino_index = int(input('Choose a Dinosaur: '))
    
    def show_robo_opponent_options(self):
        print('Robot options: ')
        index = 0
        for robot in self.fleet.robots:
            print(f'Press {index} for {robot.name} with {robot.health}.')
            index += 1
        self.chosen_robot_index = int(input('Choose a Robot: '))


    def dispaly_winner(self):
        if len(self.fleet.robots) == 0:
            print('DINOSAURS WIN!!!')
        elif len(self.herd.dinosaurs) == 0:
            print('ROBOTS WIN!!!')




