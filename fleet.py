from robot import Robot


class Fleet:
    def __init__(self):
        self.robots = []
        self.create_fleet()
        

    def create_fleet(self):
        self.robot_one = Robot('C3PO','Dark Sabre', 35)
        self.robot_two = Robot('T-800', 'Noisy Cricket', 25)
        self.robot_three = Robot('Baymax', 'Auto 9', 20)
        
        
        self.robots.append(self.robot_one)
        self.robots.append(self.robot_two)
        self.robots.append(self.robot_three)
