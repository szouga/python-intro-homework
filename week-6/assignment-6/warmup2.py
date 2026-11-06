# Write two functions:

# celsius_to_fahrenheit(c) — converts Celsius to Fahrenheit using (c * 9/5) + 32
# fahrenheit_to_celsius(f) — converts Fahrenheit to Celsius using (f - 32) * 5/9
# Call each with a few test values and print the results. Use f-strings and round to one decimal place.

#round up or down first, then apply one decimal place so number after decimal is always 0
def celsius_to_fahrenheit(c):
    """converts Celsius to Fahrenheit"""
    fahrenheit = (c * 9/5) + 32
    
    fahrenheit = f"{fahrenheit:.1f}°F"
    return fahrenheit

def fahrenheit_to_celsius(f):
    """converts Fahrenheit to Celsius"""
    
    celsius = (f - 32) * 5/9
    
    celsius = f"{celsius:.1f}°C"
    return celsius
    
houston_location = "Houston, TX"
houstonf = fahrenheit_to_celsius(62)
houstonc = celsius_to_fahrenheit(17)
#62 degrees F = 17 degrees C

atlanta_location = "Atlanta, GA"
atlantaf = fahrenheit_to_celsius(68)
atlantac = celsius_to_fahrenheit(21)
#68 degrees F = 21 degrees C

colorado_location = "Keystone, CO"
coloradoc = celsius_to_fahrenheit(-7)
coloradof = fahrenheit_to_celsius(20)
#-7 degrees C = 20 degrees F

arizona_location = "Summerhaven, AZ"
arizonac = celsius_to_fahrenheit(7)
arizonaf = fahrenheit_to_celsius(45)
#7 degrees C = 45 degrees F
layout_width = 100
# ^used for design
print("As of November 5 2026, the current temperature in these four cities are:".center(layout_width))
print(f"{houston_location}   ~  {houstonc} | {houstonf}".center(layout_width))
print(f"{atlanta_location}   ~  {atlantac} | {atlantaf}".center(layout_width))
print(f"{colorado_location}  ~  {coloradoc} | {coloradof}".center(layout_width))
print(f"{arizona_location}   ~  {arizonac} | {arizonaf}".center(95))