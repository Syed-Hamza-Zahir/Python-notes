from Reptile_class import reptile

class snake(reptile):
    def __init__(self):
        super().__init__()
        self.forked_tongue = True
        self.clood_blooded = True
        self.venom = None
        self.limbs = False

    def use_tongue_to_smell(self):
        print("smell through tongue")

