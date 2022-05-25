# lambdas are self-contained, can't assign variables to it, for anonymous function.
# take many parameters, returns one expression

def add(num1, num2):
    return num1 + num2

addition = lambda num1,numb2: num1 + numb2

print(add(4,7))
print(addition(4,7))

savings = [342.34, 456.87, 500.00, 43.56]
bonus = list(map(lambda x: x * 1.1, savings))
print(bonus)
