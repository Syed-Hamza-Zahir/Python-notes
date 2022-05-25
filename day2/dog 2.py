class dog:  # everythin in here is self contained


    def __init__(self, name, colour): # how you initialise variables in a class
        self.name = name
        self.colour = colour
        self.animal = "canine" # cannot chnage this as its not a parameter
        self.bark()


    def bark(self):  # a function becomes a method when in a class, self means referring to dog class
            return "woof"

fido = dog("fido", "brown")

# before we did  fido.name = name, fido.colour = colour

print(fido.name)
print(fido.colour)
print(fido.animal)
print(fido.bark())