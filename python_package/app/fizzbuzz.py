def fizzbuzz(x, y):  # x, y != 0
    counter = 0

    if x == 0 or y == 0:
        print("Cannot have zero")
    else:
        while counter < 100:
            counter = counter + 1
            if counter % x == 0 and counter % y != 0:
                print(f"{counter} fizz")
            elif counter % y == 0 and counter % x != 0:
                print(f"{counter} buzz")
            elif counter % y == 0 and counter % x == 0:
                print(f"{counter} fizzbuzz")
            else:
                print(counter)


fizzbuzz(33, 5)
