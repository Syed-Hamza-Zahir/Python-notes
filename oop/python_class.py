from snake_class import snake

class python(snake):

    def __init__(self):
        super().__init__()
        self.large = True
        self.two_lungs = True
        self.venom = False

    def digest_large_prey(self):
        print("I'm full")

    def constrict(self):
        print("squeeze")

    def climb(self):
        print("spiderman")

    def shed_skin(self):
        print("new year, new me")

peter = python()
peter.shed_skin()