# Exercise 4

cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven
fortnights = 26
fortnightly_salary_after_tax = 2400.00
tax_rate = 0.33
total_pay_after_tax = round(float(fortnights * fortnightly_salary_after_tax),2)
total_pay_before_tax = round(total_pay_after_tax / (1 - tax_rate),2)

print(total_pay_after_tax, " and before...", total_pay_before_tax)
#
print("There are", cars, "cars available")

#
print("There are only", drivers , "drivers available")

print("There will be", cars_not_driven , "cars empty today")

print("We can transport", carpool_capacity , "people today")

print("We have", passengers , "to carpool today.")

print("We need to put about", average_passengers_per_car , "in each car.")


## prints Roosters 97
#print("Roosters", float(100) - float(25) * float(3) % float(4))

# prints "Now I will count the eggs:"
#print("Now I will count the eggs:")

# prints 7.0
#print(float(3) + float(2) + float(1) - float(5) + float(4) % float(2) - float(1) / float(4) + float(6))

# prints "Is it true that 3 + 2 < 5 - 7?"
#print("Is it true that 3 + 2 < 5 - 7?")
# the statement is false, so prints false
#print(3 + 2 < 5 - 7)

# prints "What is 3 + 2?" 5
#print("What is 3 + 2?", 3 + 2)
# prints "What is 5 - 7?" -2
#print("What is 5 - 7?", 5 - 7)

#ok ok
#print("Oh, that's why it's False.")

#ok ok ok
#print("How about some more.")

# prints TRUE
#print("Is it greater?", 5 > -2)
# prints TRUE
#print("Is it greater or equal?", 5 >= -2)
# prints FALSE
#print("Is it less or equal to?", 5 <= -2)
