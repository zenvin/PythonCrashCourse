#Make a dictionary containing three major rivers and the country each river runs
#through. One key-value pair might be nile: egypt.

rivers = {
"mekong": "indochina",
"danube": "germany",
"yangtze": "china", 
}

#use a loop to print a sentence about each river

for river, country in rivers.items():
	print(f"The {river.title()} runs through {country.title()}.")

#use a loop to print the name of each river:

for river in rivers.keys():
	print(river.title())

#use a loop to print the name of each country:

for country in rivers.values():
	print(country.title())

	