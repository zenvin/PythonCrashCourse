#imagine an alien was just shot down in a game. 

#Create a variable called alien_color and assigned green, yellow and red.
alien_color = ["green" , "yellow" , "red"]

#write an if statement to test whether the alien's coloe is green.
#if it is, print a message that the player earned 5 points.
if 'green' in alien_color:
	print("You just got 5 point!")

#write one version of the this program that passes the if test and another that fails.
#The version that fails has no output.
if 'yellow' in alien_color:
	print('They call me mellow yellow.')

if 'black' in alien_color:
	print("Failed.")

#write and if-else chain.with the color of the alien from above
alien_color = ["green" , "yellow" , "red"]

#if the alien is green, print something
if 'green' in alien_color:
	print("You just earned 5 points for shooting the alien!")
else:
	print("You just earned 10 points!")

#if-elif-else chained with above

if 'green' in alien_color:
	print("You just earned 5 points for shooting the alien!")
if 'yellow' in alien_color:
	print("You just earned 10 points for shooting the alien!")
if  'red' in alien_color:
	print("You just earned 15 points for shooting the alien!")

