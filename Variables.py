# Python knows the types, unlike with other languages, you need to state it
a = 1  # int
b = 2  # int
c = 3.5  # float
# d = float(d)
a = 5
hi = "Hello world!"

origin = "www.google.com"

print(hi)
print(origin)
print("origin")
print(type(hi))
print(type(a))
print(type(c))

# input activity

Name = input("\nEnter your name: ")
DoB = input("Enter your date of birth: ")
Age = int(input("Enter your age: "))
gender = bool(input("You are a male, True or False: "))
hobby = input("What is your hobby?")
print(f"You name is {Name}, you were born on {DoB}, so you are {Age} years old. You've said that it is {gender} that "
      f"you are a male. You claim you enjoy {hobby}.")

