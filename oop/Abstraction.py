class Customer:
    def __init__(self):  # constructor
        self._firstname = ""
        self._lastname = ""

    def fullname(self):
        print(f" Full name: {self._firstname} {self._lastname}")

    @property
    def lastname(self):
        return self._lastname
