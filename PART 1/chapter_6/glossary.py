#A Python dictionary can be used to model an actual dictionary.
#However, to avoid confusion, let's call it a glossary.

#think of five programming words you've learned about.
#use the words as the keys in you glossary, and store their meanings as value

glossary = {
	'print()': 'This command outputs a string, number, variable or other items.',
	'del': 'This deletes things. From a list, a key etc.',
	'#': 'This is used to leave comment as Python will not run it.',
	'if': 'A way to run conditional tests.',
	'for': 'A way to start a loop.',
	'sort()': 'Sorts the list or items alphabetically.',
	'items()': 'Goes through the items in the dictionary.',
	'values()': 'Only pulls the values of the dictionary and not the keys.',
	'keys()': 'Only pulls the keys of the dictionary.',
}

#print each word and their meaning as neatly formatted output/:

print(f"The meaning of Print is: {glossary['print()']}.")
print(f"\nThe meaning of del is: {glossary['del']}.")
print(f"\nThe meaning of # is: {glossary['#']}.")
print(f"\nThe meaning of if is: {glossary['if']}.")
print(f"\nThe meaning of for is: {glossary['for']}.")

#6-4 Glossary:
for term, definition in glossary.items():
	print(f"\nThe definition of {term} is {definition}.")