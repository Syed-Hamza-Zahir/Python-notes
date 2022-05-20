name = input("Enter your name: ")
height = input("Enter your height in metres: ")
fav_colour = input("Enter your favourite colour: ")
Sec_ani = input("Enter your secret spirit animal: ")

print(f"\nHi {name}, are you sure you're {height}?? {fav_colour} is a great colour! "
      f"So your secret spirit animal begins with {Sec_ani[0]} and ends with {Sec_ani[-1]}.")

guess = input(f"\nHere's a clue... your animal has {len(Sec_ani)} letters. Now guess what your spirit animal is: ")
if guess == Sec_ani:
    print("well done! That is correct, How did you know!")
else:
    print("Wrong!")
