class Herd:
    def __init__(self):
        self.dinosaurs = []
        self.create_herd()

    def create_herd(self):
        self.dino_one = Dinosaur('Carnotaurus', 25)
        self.dino_two = Dinosaur('Stegosaurus', 20)
        self.dino_three = Dinosaur('T-Rex', 40)

        self.dinosaurs.append(self.dino_one)
        self.dinosaurs.append(self.dino_two)
        self.dinosaurs.append(self.dino_three)

      