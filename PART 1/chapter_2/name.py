name = "ada lovelace"
print(name.title())

# title() is a method. A method is an action that Python can perform on a piece of data (in this case, proper case).
# the . after name, tells Python to make the title() method act on the variable name.

print(name.upper())
print(name.lower())

# Sometimes we will want to use the variable value inside a string. For example, we might want two variables to represent a first name and a last name:
# f-strings is shown below where the f and the the "" is used with the variables placed between it.
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)

#You can also use f-string:
print(f"Hello, {full_name.title()}")

#You can also use f-strings to compose a message and then assign the entire message to a variable:
message = f"Hello, {full_name.title()}"
print(message)

# the use of a variable and then printing the variable makes the print() call much simpler.
# note: f-strings were introduced in Python 3.6.  In 3.5 and earlier editions, one would use format().
# example: full_name = "{} {}".format(first_name, last_name)

#Adding whitespace to strings. Whitespace refers to any nonprinting character, such as spaces, tabs and end-of-line symbols. 
#TAB
print("Python")
print("\tPython")
#NEWLINE
print("Languages:n\nPython\nC\nJavaScript")
#COMBINE TABS and NEW LINE
print("Languages:\n\tPython\n\tC\n\tJavaScript")


#Page 23 Strpipping Whitespace
favorite_language = 'python '
favorite_language.rstrip()

# r.strip() will only remove it temporarily. 
# to remove the whitespace permanently, you would need to associate the stripped value to a variable:
favorite_language = favorite_language.rstrip()

# r.strip() strips from the right l.strip() strips from the left.
# stripping is normally used for cleaning up user input. 

