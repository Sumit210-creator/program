
def greet_user():
    name = input("Hello, what is your name? ")
    print(f"Hello, {name}. Good to meet you!")

greet_user()


def celsius_to_fahrenheit():
    celsius = float(input("Enter a temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}C is equivalent to {fahrenheit}F.")

celsius_to_fahrenheit()


def group_students():
    students = int(input("How many students? "))
    group_size = int(input("Required group size? "))
    
    groups = students // group_size  
    leftovers = students % group_size  
    
    if leftovers == 1:
        print(f"There will be {groups} groups with 1 student left over.")
    else:
        print(f"There will be {groups} groups with {leftovers} students left over.")

group_students()


def distribute_sweets():
    sweets = int(input("How many sweets? "))
    pupils = int(input("How many pupils? "))
    
    sweets_per_pupil = sweets // pupils  
    leftovers = sweets % pupils  
    
    print(f"Each pupil gets {sweets_per_pupil} sweets.")
    print(f"There will be {leftovers} sweets left over.")

distribute_sweets()

