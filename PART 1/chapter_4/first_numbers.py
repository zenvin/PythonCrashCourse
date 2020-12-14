#using the range() function. the range() function makes it easy to generate a series of number
for value in range(1, 5):
	print(value)

# although the code looks like it would print 1-5, it doesn't it only print 1-4.
# this is due to the off-by-one behavior often seen in programming. python start counting at the first value and ends at the second value.

#to print 1 - 5 we would need to do:
print("\n")
for value in range(1, 6):
	print(value)

#using the range() to make a list of numbers
#you can convert results of the range() directly into a list using the list(). 
#you would wrap the list() around the range(). 
numbers = list(range(1, 6))
print(numbers) # will print [1, 2, 3, 4, 5]

#you can also use the range() function to tell Python to skip numbers in a given value. 
#if you pass a third argument to range(), Python will use that value as a step size when generating numbers
even_numbers = list(range(2, 11, 2)) #the additon of 2 as a third a parameters, means it will count by 2
print(even_numbers) #this will print [2, 4, 6, 8, 10]

#creating a list of the first 10 square numbers:
squares = [] #we start with an empty list
for value in range(1, 11):  #this tells python to loop through 1-10
	square = value ** 2		#we create a square value for each value being looped
	squares.append(square)	#each squared value is appended to the list squares

print(squares) #prints the list squares with the squared numbers.

#to write the code more concisely, we can omit the temporary square and append  each new value directly to the list
squares = []
for value in range(1, 11):
	squares.append(value ** 2)

print(squares)

#either way is acceptable. sometimes using the temporary variable makes your code easier to read.

#simple statistics with a list of numbers
#you can easily find the minimum, maximum and sum of a list of numbers
digits = list(range(0, 10))
min(digits) #finds the minimum number in digits
max(digits) #finds the maximum number in digits
sum(digits) #finds the sum of all the number in digits

#list comprehension
#a list comprehension combines the for loop and the create of new elements into one line and automatically appends each new element.

squares = [value ** 2 for value in range(1, 11)] #example of list comprehension. normally not revealed to beginners.
print(squares)

#to use list comprehension:
	#1) Start with a descriptive name for the list
	#2)then open a set of square brackets and define the expression for the values you want to 
	#store in the list. in this example it's value**2
	#3) then write a for loop to generate the numbers you want to feed into the expression 
	# in this example, it's the for value in range(1, 11). Notice that no colon is used at the end of the for loop.
#it will take practice to write our own list comprehensions. if you're writing 3-4 lines of code
#and it feels repetitive, maybe consider writing a list comprehension


