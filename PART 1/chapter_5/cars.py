#A SIMPLE EXAMPLE

cars = ['audi', 'bmw', 'subaru', 'toyota'] #create list for cars

for car in cars:
	if car == 'bmw': #looking for BMW
		print(car.upper()) #print in uppercase
	else:
		print(car.title()) #else, print in title

#The loop in the example above first checks if the current value of car is 'bmw'.
#If it is, the value is printed in uppercase. If the car value is anything other 
#than BMW, it will print it in title case.

#CONDITIONAL TESTS

#Conditional test is an expression that can be evaluated as TRUE or FALSE.
#If the conditional test evalutes to TRUE, Python executes the code. 
#If the conditional test evaluates to FALSE, Python ignores the code.

#CHECKING FOR EQUALITY

#The simplest conditional test compares the value of a variable to a specific value.

car = 'bmw' #sets the value of car to 'bmw'
car == 'bmw' #checks whether the value of car is 'bmw' this will return true

#this equality operator (==) returns True if the values on the left and right side of the 
#operator match, and False if they don't match.

car = 'audi' #set the value of car to 'audi'
car == 'bmw' #Is the value of car equal to 'bmw'?
#this test will return False.

#IGNORING CASE WHEN CHECKING FOR EQUALITY

#Testing for equality is case sensitive in Python. 
#For exmaple, two values with different capitalization are not considered equal:

car = 'Audi'
car == 'audi'
#this will return false

#If case matter than this is good. But if it doesn't, we can convert
#the variable to lowercase before doing the comparison:

car = 'Audi'
car.lower() == 'audi'
#this will return True
#this test would return true no matter how the value 'Audi' is formatted. 
#the lower() does not change the orignal value of car. 

car = 'Audi'
car.lower() == 'audi'
#True
car
#'Audi'

