car = 'subaru'
print("Is car == 'subaru'? I  predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

age_0 = 32
age_1 = 12
print("\nIs age_0 >= age_1. I predict True.")
print(age_0 >= age_1)

name_0 = "bob"
print("\nIs name_0 == 'Bob'? I predict False.")
print(name_0 == 'BOB')

print("\nIs name_0.lower() == 'bob'. I predict True.")
print(name_0.lower() == 'bob')

users = ['john', 'nick', 'bob', 'ken']
if 'ryu' in users:
	print("Hadoken!")
else:
	print("Sho-ryu ken!")

if 'ken' and 'bob' in users:
	print("Team KenBob")

if 'john' or 'nick' in users:
	print('Team John and Nick!')

if 'mario' not in users:
	print("It's a so sad.")
