import os
import math, datetime, sys



wd = os.getcwd()

type(wd) # builtins
len(wd)

def return_user_id():
    print(os.getpid())

def return_user_name():
    print(os.uname())

def os_info():
    print(os.cpu_count())

print(datetime.date.today())

print(sys.path)

print(math.remainder(1,5))

print(os_info())

