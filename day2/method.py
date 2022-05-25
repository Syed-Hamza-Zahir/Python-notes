class Method:
    this_can_be_accessed_eaisly = "Hi, here I am eailsy found" #this

    def __init__(self):
        self._this_can_be_accessed_eaisly = "Hi, here I am eailsy found" #or better yet this,
        # the underscore tell the user to not change it, 2 underscore prevents change
        # instance of the above class

    def get_this_can_be_accessed_eaisly(self):
        return self.this_can_be_accessed_eaisly

    def set_this_can_be_accessed_eaisly(self, value_to_be_set):
        self.this_can_be_accessed_eaisly = value_to_be_set

x = Method()

print(x.this_can_be_accessed_eaisly)
x.this_can_be_accessed_eaisly = "I have changed"
print(x.this_can_be_accessed_eaisly)


