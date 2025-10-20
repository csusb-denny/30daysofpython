import math
#Day 2: 30 Days of python programming
first_name = "Denny"
last_name = "Le"

full_name = first_name + " " + last_name
country = "united states"
city = "Hesperia"
age = 21
year = 2025

is_married = False
is_true = True
is_light_on = False
a = b = c = "Hello"
x, y, z = 10, 20, 30

#Check data type of all variables
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(x + y + z))

#len() function - find length of first_name
print(len(first_name))
if len(first_name) == len(last_name):
  print("equal length")
if len(first_name) > len(last_name):
  print("First name > Last name")
else:
  print("Last Name > First Name")
#assigning to variables
num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two

exp = pow(num_one, num_two)

floor_division = (num_one // num_two)

#radius exercise - radius is 30meters
area_of_circle = math.pi * pow(30,2)
print(area_of_circle)
circum_of_circle = 2*math.pi*30
print(circum_of_circle)

#user input radius
radius = float(input("Enter a Radius: "))
print(math.pi * pow(radius,2))