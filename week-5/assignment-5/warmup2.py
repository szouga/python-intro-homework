# Use a while loop that repeatedly asks the user to enter a positive integer.
# If the user enters anything that isn't a positive integer, 
# print a message and ask again. Once valid input is received, print it and stop. 
# The example session below shows the format — your inputs and message wording might differ:
# Enter a positive integer: -3
# That's not a positive integer. Try again.
# Enter a positive integer: hello
# That's not a positive integer. Try again.
# Enter a positive integer: 7
# Got it: 7
# Hint: You'll need try/except to handle non-numeric input — or you can check str.isdigit().

counter = 0

while True:
    try:
        user_number = int(input("Enter a positive number: "))
        if user_number <= 0:
            print("Error numeric value not positive. Try again.")
            user_number = int(input("Enter a positive number: "))
        else:
            print(f"A positive number!: {user_number}")
            break
    except ValueError as ve:
        print(f"{ve}: ValueError, Please type only positive numbers:")
        print("   ☑️     ✖")
        print("   ⬇️    ⬇️")
        print("   ➕   ➖")
        
    counter += 1