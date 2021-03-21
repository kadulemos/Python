# - Create a distance converter converting Km to miles
# - Take two inputs from user: Their first name and the distance in km
# - Print: Greet user by name and show km, and mile values
# - 1 mile is 1.609 kilometers
# - hint: use correct types for calculating and print
# - Did you capitalize the name

name = input('Say your name: ')
km = input('What is the distance in km? ')
miles = float(km)/1.609
msg = f'Hello {name.title()}! The distance in km is {km} and in miles is {round(miles,1)}'
print(msg)