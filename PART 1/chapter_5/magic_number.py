#NUMERICAL COMPARISIONS

#Testing numberical values is pretty straight forward:

age = 18
age == 18
#True

#or we can also test to see if two numbers are not equal:

answer = 17

if answer != 42: #True, hence Python will print msg below.
	print("That is not the correct answer. Please try again!")

#numberical comparisons can also use <, > <=, >=

age = 19
age < 21
#True

age <= 21
#True

age > 21
#False

age >= 21
#False

#CHECKING MULTIPLE CONDITIONS AT THE SAME TIME

#Using 'and' to check multiple conditions
age_0 = 22
age_1 = 18
age_0 >= 21 and age_1 >= 21
#False

age_0 = 22
age_1 = 21
age_0 >= 21 and age_1 >= 21
#True

#to improve readability, use parentheses around the individual tests:
(age_0 >= 21) and (age_1 >= 21)

#Using 'or' to check multiple conditions
#They keyword or allows you to check multiple conditions as well, but it passes
#when either or both of the individual tests pass.
#An 'or' expression fails only when both individual tests fail.

age_0 = 22
age_1 = 18
age_0 >= 21 or age_1 >= 21 #one test pass --> True
#True
age_0 = 18
age_1 = 18
age_0 >= 21 or age_1 >= 21 #both test fail --> False
#False

#CHECKING WHETHER A VALUE IS IN A LIST

#Use the keyword "in" to find out whether a particular value is already in a list.

requested_toppings = ['mushrooms', 'onions', 'pineapple']
'mushrooms' in requested_toppings
#True
'pepperoni' in requested_toppings
#False

#super easy way to check and see if a list of essential values are in a list


