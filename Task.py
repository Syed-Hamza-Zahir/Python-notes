
def age(name, year, month, day):
    print(f"Hello {name}, nice to meet you!")
    if month <= 5 and day <= 19:
        print ("I can see that you were born in " + str(A))
    elif month >= 5 and day >= 19:
        print ("I can see that you were born in " + str(B))
    elif month <= 5 and day >= 19:
        print ("I can see that you were born in " + str(A))
    elif month >= 5 and day <= 19:
        print("I can see that you were born in " + str(A))
    else:
        print("This function sucks")

name = input("What is your name?:")
year = int(input("How old are you (in years as a number)?: "))
month = int(input("what month were you born in (number): "))
day = int(input("On Which day of this month were you born?: "))
A = (2022 -int(year))
B = (2021 -int(year))

print(age(name, year, month, day))
