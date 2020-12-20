#A Dictionary in a Dictionary (pg 110)

users = { #the users dictionary is made of two other dictionary (aeinstein and mcurie)
	'aeinstein':{
	'first': 'albert',
	'last': 'einstein',
	'location': 'princeton',
	},

	'mcurie': {
	'first': 'marie',
	'last': 'curie',
	'location': 'paris',
	},

}

for username, user_info in users.items():
	print(f"\nUsername: {username}") #print the user name
	full_name = f"{user_info['first']} {user_info['last']}" #saving the first and last name into one variable
	location = user_info['location'] #saving location to a variable. 

	print(f"\tFull name: {full_name.title()}")
	print(f"\tLocation: {location.title()}")