'''
functions.py

1. functions are defined using `def name():`
2. code inside the function needs to be indented
3. functions are called by `name()`

'''

def say_hi(name, age):
    print("Hello " + name + ", you are " + age)

def say_hi_int(name, age):
    print("Hello " + name + ", you are " + str(age))

say_hi("Paul", "65") # pass parameters as strings
say_hi("Anne-Marie", "59")

print("\n")
say_hi_int("Paul", 65) # pass parameters as string, int
say_hi_int("Anne-Marie", 59)
