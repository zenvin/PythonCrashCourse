#use a for loop to count from number 1 to 20

for number in range(1, 21):
	print(number)

#count to a million
#make a list of number from one to one million and then use a for loop to print the numbers
# numbers = (list(range(1, 1000001)))
# for value in numbers:
# 	print(value)

#summing a million. make a list of numbers from 1 to 1 million
	#then use min() and max() to make sure your list is start at 1 and ends at 1,000,000
		#then use sum()

numbers_million = (list(range(1, 1000001)))
print(min(numbers_million))
print(max(numbers_million))
print(sum(numbers_million))

#odd numbers
#using a third argument in the range() function to make a list of odd numbers from 1 to 20.
numbers = (list(range(1, 21, 2)))
for value in numbers:
	print(value)

#Threes.
#make a list of multiples of 3 from 3 to 30. use a for loop to print the numbers in your
number_threes = list(range(3, 31, 3))
for value in number_threes:
	print(value)

#Cubes
#make a slist fo the first 10 cubes and use a loop to print out the value of each
cubed = list(range(1, 11))
for value in cubed:
	print(value**3)

#use list comprehension to generate a list of the first 10 cubes

cubed = [value**3 for value in range(1, 11)]
print(cubed)