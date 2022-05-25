# functions are all about resueability

def print_something():
    print("Something has been printed.")
print_something()

def print_something_else(print_string):
    print(print_string)
print_something_else("Hello world")

def greeting(name):
    print("Hello, my name is " +name)
greeting("Syed")

def addition(int1, int2):
    return int1 + int2
print(addition(2,4))

x = 10
x = (addition(x,4))
print(x)

def addition2(int1=5, int2=5): #default parameters
    return int1 + int2
print(addition2)

def addition3(int1=5, int2=5):
    return int1 + int2
print(addition3(2,4))

def addition4(*multiargs):
    print(type(multiargs))

    for arg in multiargs:
        print(arg)
addition4(1,2,3,4)

# def greeting(name): # no warning that it wont work
   # print("hello, my name is " + name)
# greeting(323)

# def greeting2(name: int): #can tell it what to expect
    # print("hello, my name is " + name)
# greeting2(323)

def division(denom: int, num: int) -> float: # we expect a float as an answer
    return denom/num

def sub(int1: int =5, int2: float = 2) -> float:
    return int1 - int2

a: int = 10
b: float = 7.6

print(sub(10,7.6))