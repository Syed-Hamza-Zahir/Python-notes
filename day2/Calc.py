def add(*multiargs):
    ans = 0
    for arg in multiargs:
        ans = ans + arg
    return ans

def sub(a:float, b:float) -> float:
    ans = a - b
    return ans

def div(multiargs): # nope
    ans = 0
    for arg in multiargs:
        ans = ans / arg
    return ans

def mult(*multiargs):
    ans = 1
    for arg in multiargs:
        ans = ans * arg
    return ans

print(add(3,4,5,6,6,8,54))

print(sub(4.55, -9.0))