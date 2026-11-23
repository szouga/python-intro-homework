try:
    numerator = float(input("Type a numerator: "))

    denominator = float(input("Now give a denominator: "))
    
    if denominator == 0:
        raise ZeroDivisionError
    else:
        quotient = numerator/denominator
        quotient = float(quotient)
        print("Dividend: ", numerator)
        print("Divisor: ", denominator)
        print(f"{numerator} ÷ {denominator} = {quotient}")
except ZeroDivisionError:
    print("Your dividend is fine, however,\nthe divisor cannot be 0 because dividing by zero results in undefined.")
