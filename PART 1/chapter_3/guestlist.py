guests = ['buddha', 'god', 'satan', 'me']

print(f"{guests[0].title()}, please join me for dinner tonight under the stars.")
print(f"{guests[1].title()}, please join me for dinner tonight under the stars.")
print(f"{guests[2].title()}, please join me for dinner tonight under the stars.")
print(f"{guests[3].title()}, please join me for dinner tonight under the stars.")

unavailable = 'me'

print(f"{unavailable} will not make it to the dinner tonight.")
#modifying the list to remove 'me' and add 'Bobby'
guests.remove('me')
guests.append("bobby")

print(f"{guests[0].title()}, please join me for dinner tonight under the stars.")
print(f"{guests[1].title()}, please join me for dinner tonight under the stars.")
print(f"{guests[2].title()}, please join me for dinner tonight under the stars.")
print(f"{guests[3].title()}, please join me for dinner tonight under the stars.")

print(guests)
#inserting someone to the beginning of the list
guests.insert(0,'cash')
print(guests)
#inserting someone to the middle 
guests.insert(2, "love")
print(guests)
#insert someone at the end
guests.insert(-1, "see")
print(guests)

print(f"\nThe list of guests is now {len(guests)} people.")
print(f"\n{guests[0].title()}, please join me for dinner tonight under the stars.")
print(f"\n{guests[1].title()}, please join me for dinner tonight under the stars.")
print(f"\n{guests[2].title()}, please join me for dinner tonight under the stars.")
print(f"\n{guests[3].title()}, please join me for dinner tonight under the stars.")
print(f"\n{guests[4].title()}, please join me for dinner tonight under the stars.")
print(f"\n{guests[5].title()}, please join me for dinner tonight under the stars.")
print(f"\n{guests[6].title()}, please join me for dinner tonight under the stars.")

print(f"\nHi {guests.pop(6).title()}, sorry bro, not enough room at the table.")
print(guests)
print(f"\nHi {guests.pop(5).title()}, sorry bro, not enough room at the table.")
print(guests)
print(f"\nHi {guests.pop(4).title()}, sorry bro, not enough room at the table.")
print(guests)
print(f"\nHi {guests.pop(3).title()}, sorry bro, not enough room at the table.")
print(guests)
print(f"\nHi {guests.pop(2).title()}, sorry bro, not enough room at the table.")
print(guests)

del guests[0]
del guests[0]
print(guests)

