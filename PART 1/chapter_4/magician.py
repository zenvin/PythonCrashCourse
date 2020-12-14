# for loop. used to do the same action with every item in a list.

# using for loop print list of magician's names.
magicians = ["alice", "david", "carolina"]  #defining the list
for magician in magicians: #defining the loop. this line tells python to pull a name fromthe list magicians and associate it with the variable magician.
	print(magician.title()) #print the name that's been assigned to magician. python will repeat the above lines once for each name in the list. 
	#for every magician in the list of magicians, print the magician's name.	
# we can choose any name for the temporary variable that will be associated with each value in the list.
# but use meaningful names that represent a single item from the list. 

magicians = ["alice", "david", "carolina"]
for magician in magicians:
	print(f"{magician.title()}, that was a great trick!\n") # this line is considered inside the loop and is idented.

#let's add a second line to the loop

magicians = ["alice", "david", "carolina"]
for magician in magicians:
	print(f"{magician.title()}, that was a great trick!")
	print(f"I can't wait to see your next trick, {magician.title()}.\n")

#lines after the loop that is not indented will be executed once:
print("Thank you, everyone. That was a great magic show!")

#don't forget to indent. The loop below will work even if we don't indent the second print
#and being so, we would not know that it didn't run the way we intended for it to run.

magicians = ["alice", "david", "carolina"] #the error showed here is a LOGCIAL ERROR.
for magician in magicians:
	print(f"{magician.title()}, that was a great trick!")
print(f"I can't wait to see your next trick, {magician.title()}.\n") #not idented. this error will not pop up as there is one command after the loop.

#syntax error is when our python syntax is wrong.

#unnecessary identation
#python will inform us about indentation that are unexpected.

#another logical loop: the last print line will be part of the loop.
magicians = ["alice", "david", "carolina"] #the error showed here is a LOGCIAL ERROR.
for magician in magicians:
	print(f"{magician.title()}, that was a great trick!")
	print(f"I can't wait to see your next trick, {magician.title()}.\n") #not idented. this error will not pop up as there is one command after the loop.
	print("Thank you, everyone. That was a great magic show!")

#forgetting the colon after the for loop is a syntax error. Python will remind use.