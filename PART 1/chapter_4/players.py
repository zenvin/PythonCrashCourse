#working with part of a list

#use slice to work with a specific group of items.
	#to make a slice, you specify the index of the first and last elements you want to work with.
	#as with the range(), python stops one item before the second idex you specify.
	#to output the first three elements in a list, you would request indices 0 through 3.

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])  #this will print a slice of the list, which is just the first 3 players

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:4]) #will print the second, third, and fourth items

print(players[:4]) #will slice automatically from the beginning of the list

print(players[2:]) #will start at the third item(3) and splice to the end of the list

#remember that negative number is used to access the end of the list. 
print(players[-3:]) #will slice the last three players on the list

#a third value can be entered as well. It will tell python how many items to skip when splicing.

#LOOPING THROUGH A SLICE
#you can user a slice in a for loop if you want to loop through a subset of the elements in a list.

#looping throught the first 3 players of the list.
players = ['charles', 'martina', 'michael', 'florence', 'eli']

print("Here are the first three players on my team:")
for player in players[:3]:
	print(player.title())

#COPYING A LIST
#to copy a list, you can make a slice that inclues the entire original list by omitting the first index and the second index ([:]).
#this tells python to make a slice that starts at the first item and ends with the last item, producing a copy of the entire list.

