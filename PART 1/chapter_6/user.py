#Looping through a dictionary
#python lets you loop through a dictionary. Dictionaries can be used to loop
#through information in a variety of ways; therefore, several ways to loop through
#them. You can loop through all of a dictionary's key value pairs, through its keys,
#or through its value. 

#Looping through all key-value pairs
#let's consider a new dictionary design to store information about a user.

user_0 = {
	'username': 'efermi',
	'first': 'enrico',
	'last': 'fermi',
}

#looping through the dictionary to print all keys and their values:

for key, value in user_0.items(): #create names for the two variables that will hold the key and value.
	print(f"\nKey: {key}")
	print(f"\nValue: {value}")

#can also work with k, v to replace key, value
for k, v in user_0.items(): 
	print(f"\nKey: {k}")
	print(f"\nValue: {v}")

#we also use the items() method, which returns a lsit of key-value pairs.
#The for loop then assignes each of these pairs to the two variables provided.
#In the preceding example, we use the varaibles to print each key followed by the
#associated value. 

