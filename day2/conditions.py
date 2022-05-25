age = 15

if age >= 18: # if age > 18 or age = 18 or age != 99 etc
    print("You are the correct age to watch this film.") # must be indented in python
elif age <15 :
    print("You are not the correct age")
else:
    print("you are not the correct age.")

print("This film has started.") # this is outside the condition, it will run regardless

film_rating = "universal"

if film_rating.lower() == "universal":
     print("All age groups can watch this film.")
elif film_rating.lower() == "PG":
    print("General viewing, parental guidence for children.")
elif film_rating.lower() == "12" or "12a":
    print("All age groups can watch this film.")
    # check screen shot