#write an if-elif-else chain that:

#set the variable age
age = 43
#if a person is < 2, print they a baby
if age < 2:
	stage = 'baby'
elif age < 4:
	stage = 'toddler'
elif age < 13:
	stage = 'kid'
elif age < 20:
	stage = "teenager"
elif age < 65:
	stage = 'adult'
elif age >=65:
	stage = 'elder'
print(f"You are a(n) {stage}. Good luck.")