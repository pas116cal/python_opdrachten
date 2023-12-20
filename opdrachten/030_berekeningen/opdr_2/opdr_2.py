# Opdracht 2 berekeningen
# Naam student:
# Groep:

# Hier komt je code...

def celsius_naar_fahrenheit(celsius):
    return round((celsius * 9/5) + 32, 1)

def fahrenheit_naar_celsius(fahrenheit):
    return round((fahrenheit - 32) * 5/9, 1)

celsius1 = -12
fahrenheit1 = celsius_naar_fahrenheit(celsius1)
tekst1 = f"{celsius1} graden Celsius is gelijk aan {fahrenheit1} graden Fahrenheit"

fahrenheit2 = 102
celsius2 = fahrenheit_naar_celsius(fahrenheit2)
tekst2 = f"{fahrenheit2} graden Fahrenheit is gelijk aan {celsius2} graden Celsius"

print(tekst1)
print(tekst2)

celsius3 = 62.2
fahrenheit3 = celsius_naar_fahrenheit(celsius3)
tekst3 = f"{celsius3} graden Celsius is gelijk aan {fahrenheit3} graden Fahrenheit"

fahrenheit4 = 96
celsius4 = fahrenheit_naar_celsius(fahrenheit4)
tekst4 = f"{fahrenheit4} graden Fahrenheit is gelijk aan {celsius4} graden Celsius"

print(tekst3)
print(tekst4)
