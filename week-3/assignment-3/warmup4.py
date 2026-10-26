number = int(input("Enter a number: "))

#parity = determine whether a number or 
# data value is even or odd

#check sign
if number < 0:
    negative = "negative"
    print(f"{number} is {negative}.")
elif number == 0:
    print(f"{number} is zero.")
else:
    positive = "positive"
    print(f"{number} is {positive}.")
#^automatically evaluate positive numbers only

#check parity
if number == 0:
    print("0 is even.")
elif number % 2 == 0:
    print(f"{number} is even.")
elif number % 2 == 1:
    print(f"{number} is odd.")
else:
    print("Error")
    


