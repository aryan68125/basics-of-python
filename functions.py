#a simple functions that does not take any input 
print("Function that does not accept any input as a variable\n")
def greet():
    print("Hello")
    print("How are you")
    print("I am a python program that uses a function to greet you")
    print("I am at your service MASTER")
    print("\n")
#calling the create function greet()
greet()

#function that accepts a name as a variable
print("Function that does accept any input as a variable name (name of a person)\n")
name = input("Enter your name\n")
def greet_with_name(name):
    print(f"Hello {name}")
    print("How are you")
    print("I am a python program that uses a function to greet you")
    print("I am at your service MASTER")
    print("\n")
#calling a function that accept a name as a variable name as an input
greet_with_name(name)

#functions with more than one input using positional arguments
print("Function that does accept any input as a variable name (name of a person) and location (your city)\n")
name2 = input("Enter your name\n")
location = input("Enter your city\n")
def greet_with(name,location):
    print(f"Your name is {name}")
    print(f"Your city is {location}")
    print("\n")
#calling function which accepts two parameters
greet_with(name2,location)

#functions with more than one input using keyword arguments
print("Function that does accept any input as a variable name (name of a person) and location (your city)\n")
name3 = input("Enter your name\n")
location2 = input("Enter your city\n")
def greet_with(name,location):
    print(f"Your name is {name}")
    print(f"Your city is {location}")
    print("\n")
#calling function which accepts two parameters
greet_with(location=location2,name = name3)