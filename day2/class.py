class dog:  # everythin in here is self contained

    animal_kind = "canine"  # class variable which returns an attribute of a string

    def bark(self):  # a function becomes a method when in a class, self means referring to dog class
        print(self.animal_kind)
        return "woof"

# dog.animal_kind = "animal"# this will affect the other instances

fido = dog()
fido.animal_kind = "CAT" # this is fine
lassie = dog()
rex = dog()
daisy = dog()

print(type(fido))
print(type(lassie))
print(fido.animal_kind)
print(lassie.animal_kind)
print(fido.bark())
print(lassie.bark())