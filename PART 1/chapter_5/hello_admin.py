#make a list of five or more usernames. loop through the list and print a
#greeting to each user.
usernames = ['admin', 'ken', 'ryu', 'bison', 'chun-li', 'sagat']

for user in usernames:
	if 'admin' in user:
		print(f"Hello {user.title()}, would you like to see a status report?")
	else: 
		print(f"Hello {user.title()}, thank you for logging in today.")

#add an if test to the above program to check if the list is empty
usernames = []

if usernames:	
	for user in usernames:
		if 'admin' in user:
			print(f"Hello {user.title()}, would you like to see a status report?")
		else: 
			print(f"Hello {user.title()}, thank you for logging in today.")
else:
	print("We need to find some users!")

#create a program that simulates how websites ensures that everyone has a unique username.

current_users = ['admin', 'ken', 'ryu', 'bison', 'chun-li', 'sagat']
new_users = ['ben','bob', 'karen', 'Ken', 'Sagat', 'freddy']

lower_new_users = []

for user in new_users: #to make the new user list lower-cased
	lower_new_users.append(user.lower())

print(lower_new_users)

for user in lower_new_users:
	if user in current_users:
		print(f"{user} has been used. Please choose another name.")
	else:
		print(f"{user} is availble for use.")


