#You can put just about any action in the indented block following the test.
#If the conditional test evaluates to True, Python will execute the code following
#the if statement. If the test evaluates False, Python will ignore the code.

age = 19
if age >= 18: #Python will check to see if this statement is true.
	print('You are old enough to vote.') #will be executed.
	print('Have you registed to vote?') #will also be executed as the statement from line 6 is true.


#if-else Statements
#use if-else when you want to take one action when a conditional test passes and a
#different action in all other cases.
#if-else is similar to the if statement, but it allows you to define an action or set of
#actions that are executed when the conditional test fails. 

age = 17
if age >= 18:
	print("You are old enough to vote.")
	print("Have you registered to vote yet?")
else:
	print('Sorry, you are too young to vote.')
	print('Please register to vote as soon as you turn 18!')





