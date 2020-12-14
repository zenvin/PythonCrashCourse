# make a list of five places you'd like to see.
locations = ["angkor wat", "the great wall of china", "the forbidden city", "tibet", "shaolin"]

print("\nThis is the oringinal list:")
print(locations)

print("\nThis is the list sorted alphabetically:")
print(sorted(locations))

print("\nI've used sorted() so the list hasn't changed:")
print(locations)

print("\nPrinting the list in reverse order:")
locations.reverse()
print(locations)

print("\nAnd now it's back to the original order:")
locations.reverse()
print(locations)

print("\nAnd now, to permanently change the order of the list alphabeitcally with the sort():")
locations.sort()
print(locations)

print("\nAnd now, to permanently change the order of the list reverse-alphabeitcally with the sort():")
locations.sort(reverse=True)
print(locations)