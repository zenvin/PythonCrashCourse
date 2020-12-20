#use a dictionary to store information about a person you know. First, last, age, city

battosai = {
	'first_name': 'Kenshin', 
	'last_name': 'Himura', 
	'age': 33, 
	'city': 'Kyoto'
}

print(battosai) # will print all keys and their respective value.

print(battosai['first_name'])
print(f"This is showing that we can print the first name of battosai: {battosai['first_name'].title()}")
print(f"This is showing that we can print the last name of battosai: {battosai['last_name'].title()}")
print(f"Battosai is {battosai['age']} years old and lives in {battosai['city']}.")


#from page 112
#make 2 dictionaries representing differnt people

wolf = {
	'first_name': 'Hajime',
	'last_name': 'Saitoh',
	'age': 38,
	'city': 'osaka',
}

shorty = {
	'first_name': 'boy',
	'last_name': 'okita',
	'age': 20,
	'city': 'tokyo',
}

#store all 3 dictionaries in a list called people

people = [battosai, wolf, shorty]

#loop through each person and print everything you know about them

for person in people:
	print(person)

#6-9 from 112
favorite_places = {
	'bob': 'dojo',
	'lucy': 'police station',
	'john': 'yakitori',
}

for name, place in favorite_places.items():
	print(f"{name.title()} likes to be at the {place.title()}.")

