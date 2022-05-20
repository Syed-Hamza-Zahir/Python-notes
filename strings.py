single_quotes = 'This works.'
double_quotes = "This also works."

print(single_quotes)
print(double_quotes)

# bad_string = 'Wow, I don't like this.'
better_string = 'Wow, I don\'t like this.'
better_string2 = "wow, I don't like this."

Hw = "Hello! World"
print(Hw[7:])
print(Hw[-5:])
print(Hw[:5])
print(Hw[0:5])

print(len(Hw))

print("Ctrl + / = comment_out_multiple_lines")

White_space = "         lot's of white space at the end and start                   "
print(len(White_space))
print(len(White_space.strip()))

example_text = "here's is some text with lot's of text"
print(example_text.count("text"))
print(example_text.count("e"))
print(example_text.lower())
print(example_text.upper())
print(example_text.capitalize())
print(example_text.replace("with", "without"))

email = "sZAHIr@starTAGloBal.com"
print(email.lower())

int_string = "6"
print(int(int_string))
print(type(int(int_string)))

a = "2"
b = "4"
print(int(a) +int(b))

# f strings
name = "Lassie"
years = 7
height_cm = 60.2
print(f"{name} is {years} years old and {height_cm}cm tall.")

# string evaluation with f strings
name = "Snoopy"
years = 3
print(f"{name.upper()} IS {years * 7} YEARS OLD IN DOG YEARS")

pi = 3.12159265359
print(f"Pi to 3 decimal places {pi: .3f}")
print(f"Pi to 5 decimal places {pi: .5f}")

score = 16
max_score = 26
print(f"You scored {score/max_score}")
print(f"You scored {score/max_score:%}")
print(f"You scored {score/max_score:.2%}")
print(f"You scored {score/max_score:.0%}")