# Write a function greet(name, greeting="Hello") that prints a greeting. Call it three different ways

def greet(name, greeting="Hello"):
    if greeting is None or greeting.strip() == "":
        greeting = "Hello"
    
    print(f"{greeting}, {name}!")

greet("Elphaba")
greet("Elphaba", "Sweet Oz")
greet("Elphaba")

