from Animal_class import animal

class reptile(animal):

    def __init__(self):
        super().__init__()
        self.cold_blooded = True
        self.tetrapod = None
        self.heart_chambers = [3, 4]
        self.ambiotic_eggs = None

    def seek_heat(self):
        print("where sun?")

    def hunt(self):
        print("you can run but you cant hide")

    def use_venom(self):
        print("wait for the kill")

    def attract_mate_through_scent(self):
        print("you smell good")




