#CHECKING FOR INEQUALITY

#To determine whether two values are not equal, you can combine an exclamation
#point and an equal sign (!=). An '!' represent 'not' in programming lang.

requested_topping = 'mushrooms'

if requested_topping != 'anchoives': #comapres the value of requested_topping to anchoives.
	print("Hold the anchoives!")

#if the two values match, Python returns False and does not run the code following the if statement.

#Most of the conditional expression you write will test for equality, but
#sometimes you'll find it more efficient to test for inequality.

#TESTING MULTIPLE CONDITIONS
#As soon as Python finds on test that passes, it skips the rest of the tests.
#This is beneficial because it's efficient and allows you to test for one specific
#condition.

#In situations where you want to check all the of the conditions, use a series of if
#statements with no elif or else statement.

requested_topping = ['mushrooms' , 'extra cheese']

if 'mushrooms' in requested_topping:
	print('Adding mushrooms.')
if 'pepperoni' in requested_topping: #this test is run even though the first test past because of the if statement.
	print("Adding pepperoni.")
if 'extra cheese' in requested_topping:
	print('Adding extra cheese.')

print(f"\nFinished making your pizza!")

#the bottom will only print mushroom because elif is used. Once a statement is true, the others are skipped.

if 'mushrooms' in requested_topping:
	print('Adding mushrooms.')
elif 'pepperoni' in requested_topping: 
	print("Adding pepperoni.")
elif 'extra cheese' in requested_topping:
	print('Adding extra cheese.')

print(f"\nFinished making your pizza!")

#USING if STATEMENTS WITH lists

requested_toppings = ['mushrooms' , 'green peppers' , 'extra cheese']

for requested_topping in requested_toppings:
	print(f"Adding {requested_topping}.")



#adding an if statement inside the for loop in case we run out of green peppers.

requested_toppings = ['mushrooms' , 'green peppers' , 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping == "green peppers":
		print("Sorry, we are out of green peppers right now")
	else:
		print(f"Adding {requested_topping}.")

print("\nFinished making your pizza")

#checking that a list is not empty

requested_toppings = []

if requested_toppings: #when the name of a list is used in a if statement, Python returns true.
	for requested_topping in requested_toppings:
		print(f"Adding {requested_topping}.")
	print("\nFinished making your pizza")
else: 
	print("Are you sure you want a plain pizza")

#When the name of a list is used in an if statement, Python returns True if the list contains at least one item.
#An empty list evaluates as False.

#Using MULTIPLE LISTS

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

requested_toppings= ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print(f"Adding {requested_topping}.")
	else:
		print(f"Sorry, we don't have {requested_topping}.")
print(f"\nFinished making your pizza!")

