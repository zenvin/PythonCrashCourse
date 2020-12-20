#learning how to use dictionaries

#consider a game featuring aliens that can have different colors and poitn values. 
#this simple dictionary stores information about a particular alien:

alien_0 = {'color': 'green', 'points': 5} #creates a dictionary called alien_0

print(alien_0['color']) #this will print 'green'
print(alien_0['points']) #this will print '5'

#a DICTIONARY in Python is a collection of key-value pairs. 
#each key is connected to a value, and you can use a key to access the value
#associated with that key. 

#a key's value can be a number, a string, a list or even another dictionary. 
#In fact, you can use any object that you can create in Python as a value in a dict.

#in python, a dictionary is wrapped in braces, {}, with a series of key-value pairs.

#a key-value pair is set of values assosciated with each other. When you provide
#a key, Python returns the value assosciated with that key. 
#Every key is connected to its value by a colon, and individual key-value pairs are
#separated by commas. 

#the simplest dictionary has exactly one key-value pair:
alien_0 = {'color': 'green'}  #'color is the key' and 'green is the value'

#To get the value associated with a key, give the name of the dictionary and then
#place the key inside a set of square brackets:

alien_0 = {'color': 'green'}
print(alien_0['color']) #will return 'green'

#We can have an unlimited number of key-value pairs in the dictionary. 
#If a player shoots down this alien, you can look up how many points they should
#using code like this:

alien_0 = {'color': 'green', 'points': 5}

new_points = alien_0['points']
print(f"You just earn {new_points} points!")

#Adding new key-value pairs
#To add a new key-value pair, you would give the name of the dictionary followed by
#the new key in square brackets.

#add coordinates to the alien_0 dictionary as new key-values:

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0 #adding the x_position key and value
alien_0['y_position'] = 25 #adding the y_posisiton key and value
print(alien_0)

#STARTING WITH AN EMPTY DICTIONARY
#Start by defining an empty dictionary with an empty set of braces and then add
#each key-value pair on its own line:

alien_0 = {}

alien_0['color'] = "green"
alien_0['points'] = 5

print(alien_0)

#Typically, you'll use empty dictionaries when storing user-supplied data in a dictionary
#or when you write code that generates a large number of key-value pairs automatically.

#MODIFYING VALUES IN A DICTIONARY
#To modify a value in a dictionary, give the name of the dictionary with the key in 
#square brackets and then the new value you want associated with that key. 

#Changing color from green to yellow
alien_0 = {'color': 'green'}
print(f"The aliens is {alien_0['color']}.")

alien_0['color'] = 'yellow' #this line modifies the key color to make it yellow.
print(f"The aliens is now {alien_0['color']}.")

#Tracking the position of an alien that can move at different speed.
#We'll store a value representing the alien's speed and then use it to determine
#how far to the right the alien should move:

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")

#Move the alien to the right.
#Determine how far to move the alien based on its current speed.

if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	x_increment = 3

#The new position is the old poisiton plus the increment. 
alien_0['x_position']= alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}") #will print 2 as the new position.

#REMOVING Key-Values Pairs
#When you no longer need a piece of information that's stored in a dictionary,
#use del statement to completely remove a key-value pair.
#del need the name of the dictionary and the key that you want to remove.

#let's remove the key 'points' from alien_0

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points'] #using del to delete the points key from alien_0 dictionary
print(alien_0)

#BEWARE: deleted key-value pair is removed PERMANENTLY.

#NESTING
#How can you manage a fleet of aliens? One way is to make a list of aliens 
#and use it in a dictionary.

alien_0 = {'color': 'green', 'points': 5}   #first we create 3 dictionaries.
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2] #then we store the dictionaries in a list called aliens.

for alien in aliens: #loop through to print them out.
	print(alien)

#using range to make 30 aliens (all the same attributes though)

aliens = [] #Start with an empty list

#make 30 green aliens
for alien_number in range(30):
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)

#show the first five aliens
for alien in aliens[:5]:
	print(alien)
print("...")

#show how many aliens have been created
print(f"Total number of aliens {len(aliens)}.")	 

aliens = [] 
for alien_number in range(30):
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)

for alien in aliens[:3]: #to change the colors of the first 3 three aliens:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10
	elif alien['color'] == 'yellow': #to make any yellow alien red.
		alien['color'] = "red"
		alien['speed'] = 'fast'
		alien['points'] = 15
 
for alien in aliens[:5]:
	print(alien)
print("...")

#Putting a list inside a dictionary

#Store information about a pizza being ordered:
pizza = {
	'crust': 'thick',
	'toppings': ['mushrooms', 'extra cheese']
}

#summarize the order:
print(f"You ordered a {pizza['crust']}-crust pizza "
	"with the following toppings:")

for topping in pizza['toppings']:
	print(f"\t{topping}")	

#you can nest a list inside a dictionary any time you want more than one value to
#be associated with a single key in a dictionary.
