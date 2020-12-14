#TUPLES
#tuples are list that cannot be changed.
#values that cannot be changed are immutable
#an immutable list is a tuple.

#a tuple looks just like a list except you use parentheses instead of square brackets.
#you can access the tuple the same way you access a list.

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

#trying to change a tuple value
# dimensions[0] = 250 
# get this error:
	#Traceback (most recent call last):
#   File ".\dimensions.py", line 14, in <module>
#     dimensions[0] = 250
# TypeError: 'tuple' object does not support item assignment

#tuples are technically defeined by the presence of a comma; the parentheses make them look neater and more readable. 
#if you want to define a tuple with one element, you need to include a trialing comma:
my_t = (3 , )
#it doesn't make sense to build a tuple with one element, but this can happend when tuples are generated automatically.

#looping all values in a tuple
#you can loop values in a tuple the same way you did with a for loop
dimensions = (200, 50)
for dimension in dimensions:
	print(dimension)

#we can't modify a tuple, but we can assign a new value to a variable that represent a tuple. 
#we can change our dimensions by:
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
	print(dimension)

dimensions = (400 , 100)
print("\nModified dimensions:")
for dimension in dimensions:
	print(dimension)
	