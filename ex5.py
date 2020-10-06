# Exercise 5

name = 'Alex Gardiner'
age = 36
height = 176 # cm
weight = 90 # kg
pounds_per_kg = 2.20462
weight_in_pounds = round(weight * pounds_per_kg,2)
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
height_in_metres = height / 100

print(f"Let's talk about {name}.")
print(f"He's {height} centimetres tall, which is {height_in_metres} metres.")
print(f"He's {weight} kilograms heavy, which is {weight_in_pounds} pounds.")
print("Actually, that's not too heavy!")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

#this line is tricky
total = age  + height + weight
print(f"If I add {age}, {height}, and {weight}, I get {total}.")
