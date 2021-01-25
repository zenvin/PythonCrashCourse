def formattedCityCountry(city, country, population=""):
	if population:
		fullCityCountry = f"{city}, {country}, {population}"
	else:
		fullCityCountry = f"{city}, {country}"
	return fullCityCountry.title()

