# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

def greet():
    print("Bom dia amor!")
    print("Tudo bem?")
    print("Dormiu bem?")
    print("\n")

greet()

def greet_with_name(name):
    print(f"Bom dia {name}!")
    print("Tudo bem?")
    print("Dormiu bem?")
    print("\n")

greet_with_name("bb")

def greet_with_name_and_location(name, location):
    print(f"Bom dia {name}!")
    print("Tudo bem?")
    print("Dormiu bem?")
    print(f"Como está o clima em {location}?")
    print("\n")

greet_with_name_and_location("bb", "Martinopole")

greet_with_name_and_location(location = "Martinopole", name = "bb")