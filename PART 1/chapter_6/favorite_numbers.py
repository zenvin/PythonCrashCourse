#use a dictionary to store people's favorite numbers.
#think of five names, and use them as keys in your dictionary.
#think of a favorite number for each person and store each as
#a value. 

favorite_number ={
	'bob': 23,
	'clark': 12,
	"suzy": 69,
	'winston': 88,
	'orson': 123456,
}
print(favorite_number) #will print the list

#print each person's name their favorite number

print(f"Bob's favorite number is {favorite_number['bob']}.")
print(f"Clark's favorite number is {favorite_number['clark']}.")
print(f"Suzy's favorite number is {favorite_number['suzy']}.")
print(f"Winston's favorite number is {favorite_number['winston']}.")
print(f"Orson's favorite number is {favorite_number['orson']}.")

#6-10 from pg 112
#modify so each person has more than one favorite number.

favorite_number ={
	'bob': [23, 7],
	'clark': [836, 97],
	"suzy": [1, 3],
	'winston': [963, 3],
	'orson': [0, 0],
}

#print each person's name along with their numbers:

for name, number in favorite_number.items():
	print(f"{name.title()}'s favorite number are {str(number)}.")