temp = input("Enter a temperature in Fahrenheit: ")

fahrenheit = float(temp)
celsius = float((fahrenheit - 32) * 5 / 9)

print(f"{fahrenheit:.1f}°F is {celsius:.1f}°C.")
