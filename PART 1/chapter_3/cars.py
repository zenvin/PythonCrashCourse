#organizing a list

#using the sort() to sort a list by alphabetical order.
cars = ['bmw', 'audi', "toyota", 'subaru']
cars.sort() # this will permanently change the order of the cars list
print(f"\n {cars}")

#to sort in reverse alphabetical order, pas the argument reverse=True to the sort() method.
cars.sort(reverse=True) #again, this will permanently change the list. Notice too that it's True, not true.
print(f"\n {cars}")

#sorted() will sort the list but will not permanently change it.
cars = ['bmw', 'audi', "toyota", 'subaru']

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

#NOTE: Sorting a listis a bit more complicated when all the values are not in lowercase. 
#There are several ways to interpret capital letters when determing a sort order, and specifying
#the exact order can be more complex than we want to deal with at this time. 
#However, most approaches to sorting will build directly on what you learned in this section.

# the reverse() method: will print the list in reverse order. Not reverse alphabetically, just reverse order of what it already is.

cars = ['bmw', 'audi', "toyota", 'subaru']
print("\nThis is the orinal list:")
print(cars)

print("\nThis is the list with the cars.reverse() method:")
cars.reverse() #will permanently change the list's order. To bring it back, reverse() it again.
print(cars)

#the len() function will find the length of the list.

print(f"The length of the cars list is {len(cars)}.\n")
len(cars)

