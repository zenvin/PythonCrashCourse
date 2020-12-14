#PEP Python Enchancement Proposal is the style guide.

#one identation is four spaces
#check editor to ensure that they are converting tabs to spaces.

#Line Length
#Many Python programmer recommend that each line should be less than 80 characters.
#Comments should be limit to 72 characters per line
#Some prefer 90 character as the limit. Not set in stone.

#Blank lines
#to group parts of your program visually, use blank lines.
#one blank line between different section is good enough. Don't overdo it.

#review

#make a list of numbers from 1 - 10

numbers = list(range(1, 21))
print(numbers)

#list comprhension 1-5 squared
squared = [number**2 for number in range(1 , 6)]
print(squared)

#slice, print last 2 items in squared:
print(squared[-2:])
#print last 3 items
print(squared[-3:])

#loop to append to numbers
for value in range(5 , 10):
	numbers.append(value)
print(numbers)