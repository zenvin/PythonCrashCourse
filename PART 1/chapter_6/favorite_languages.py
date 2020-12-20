#YOu can use a dictionary to store one kind of information about many objects. 
#For example, say you want to poll a number of people and ask them what their 
#favorite programming language is. A dictionary of storing that result would:

favorite_languages = { #we've broken a larger dictionary into several lines.
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
}

#to use the dictionary above, given the name of a person who took the poll, you
#can easily look up their favorite language:

favorite_languages = { 
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
}

language = favorite_languages['sarah'].title() #the person is the key.
print(f"Sarah's favorite language is {language}.")

#using a loop to print out everything in the dictionary

for name, language in favorite_languages.items():
	print(f"{name.title()}'s favorite language is {language.title()}.")

#the keys() method is useful when you don't need to work with all the values in the
#dictionary. 

for name in favorite_languages.keys():
	print(name.title())

#Looping through the keys is actually the default behavior when looping through a
#dictionary, so this code would have exactly the same output if you wrote:

for name in favorite_languages:
	print(name.title())

#we can access the value associated with any key we care about inside the loop
#by using the current key. Let's print the message to a couple of friends

friends = ['phil', 'sarah'] #make a list of friends we want to print message to.
for name in favorite_languages.keys(): #loop to print names
	print(f"Hi {name.title()}!")

	if name in friends: #check if the friends name is in key
		language = favorite_languages[name].title()
		print(f"\t{name.title()}, I see you love {language}!")

	#we can also use the keys() method to find out if a particular person was polled.
	#the key() method is not only for looping. It actually returns a list of all the
	#keys.
if 'erin' not in favorite_languages.keys():
	print("Erin, please take our poll!")

#looping through dictionary in a different order

favorite_languages = { 
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
}

for name in sorted(favorite_languages.keys()):
	print(f"{name.title()}, thank you for taking the poll.")

#if we're only interested in the values and not the keys, we can use the values() method. 

print("The following languages have been mentioned:")
for languages in favorite_languages.values():
	print(languages.title())

#the values() will pull all values without checking for duplicates(repeats). 
#use the set() function to remove repeats:

print("The following languages have been mentioned:")
for languages in set(favorite_languages.values()):
	print(languages.title())

#you can build a set directly using braces and separating the elements with commas:
languages = {'python', 'ruby', 'python', 'c'} #creating a set
print(languages) #printing the set.

#dictionaries have key-value, sets only have values.

#using a list in dictionaries by adding more than one favorite language (pg 109)

favorite_languages = {
	'jen': ['python', 'ruby'],
	'sarah': ['c'],
	'edward': ['ruby', 'go'],
	'phil': ['python', 'haskell'],
	}

for name, languages in favorite_languages.items():
	print(f"\n{name.title()}'s favorite languages are:")
	for language in languages:
		print(f"\t{language.title()}")
