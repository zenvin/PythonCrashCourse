#ordinal numbers indicate their position in a list, such as 1st or 2nd. 
#Most ordinal numbers end in th, except 1, 2 and 3.

numbers = list(range(1, 10)) #store number 1-9 in a list

for number in numbers:
	if number == 1:
		print("1st.")
	elif number == 2:
		print("2nd.")
	elif number == 3:
		print("3rd")
	else:
		print(f"{number}th.")