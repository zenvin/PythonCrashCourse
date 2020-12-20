

favorite_languages = { 
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
}
#make a list of people who should have take the favorite language poll:

taken_poll = ['jen', 'ryeker', 'kevin', 'phil']
#loop through the list. Print a thank you to people that have taken the poll
#and tell those that haven't they need to take it.

for name in favorite_languages.keys():
	if name in taken_poll:
		print(f"Thank you {name.title()} for taking the poll.")
	else:
		print(f"{name.title()}, please consider taking the poll.")