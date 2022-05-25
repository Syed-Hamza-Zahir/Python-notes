# Login system, checking email and password
import datetime
datetime.datetime.now()
# strftime
correct_email = True
while correct_email:
    email = input("Enter your email: ")
    if email.lower() ==("szahir@spartaglobal.com"):
        correct_email = False
    else:
        print("Your email is incorrect")
correct_pass = True

while correct_pass:
    Pass = input("Now enter your pass: ")
    if Pass ==("Docker55%"):
        correct_pass = False
    else:
        print("Your password is incorrect")

print(f"Login successful at {(datetime.datetime.now())}")
