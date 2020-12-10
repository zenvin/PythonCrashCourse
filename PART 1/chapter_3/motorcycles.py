# learning how to add elements to a list.

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# changing the first item in the list from honda to ducati
motorcycles[0] = 'ducati'
print(motorcycles)

# APPEND: to add an item to a list. append will add the item to the end of the list without affecting any of the other elements in the list.

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')
print(motorcycles)

# the append() method makes it easier to build lists dynamically. For example, you can start with an empty list and hten add items to the list using a series of appen() calls.

motorcycles = [ ]

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)

# inserting elements into a list by using the insert() method. You can do this by specifying the index of the new element and the value of the new item.
motorcycles = ['honda', 'yamaha', 'suzuki']

motorcycles.insert(0, 'ducati')
print(motorcycles) #output: ['ducati', 'honda', 'yamaha', 'suzuki']

# REMOVING items from the list. use the statement del to remove an item from a list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[0] # use del to remove the first item from the list of motorcycles
print(motorcycles)

#we can remove any item from any position in a list using the del statement. we just need to know the index.

motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[1] # this will remove yamaha as its position is [1]

print(motorcycles)

# IMPORTANT: the value that was removed from the using the del statement can no longer be accessed.

# the pop() method
# the pop() method removes the last item in a list, but it lets you work with that item after removing it. 
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycles = motorcycles.pop()
print(motorcycles) # will print the list without suzuki
print(popped_motorcycles) # will print suzuki

# you can use the pop() to print the last item that was owned

motorcycles = ['honda', 'yamaha', 'suzuki']

last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")

# Remove an item from any posiiton in a list by including the index of the item you want to remove in parentheses, not brackets.

motorcycles = ['honda', 'yamaha', 'suzuki']

first_owned = motorcycles.pop(0)
print(f"The first motorcyle I owned was a {first_owned.title()}.")

# IMPORTANT: remember that each time you use pop(), the item you work with is no longer in the list. 

# REMOVE AN ITEM BY VALUE
# if we don't know the position of the value we want to remove, but we do know the value, we can use the remove() method.

# say we want to remove 'ducati' from the list

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

# the remove() value can also be used/work with. Let's remove 'ducati' and print a reason for removing it from the list.

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive} is too expensive for me.")

# the remove() will only remove the first occurence of the value you specify. If the value occurs more than once, you will need to use a loop to remove all occurences.



