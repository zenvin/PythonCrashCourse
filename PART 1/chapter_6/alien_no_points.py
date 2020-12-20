#Using get() to Access Values

#this will return a error as there is no key points.
alien_0 = {'color': 'green', 'speed': 'slow'}
print(alien_0['points'])

#use the get() method to set default value that will be reteued if the requested
#key doesn't exist.

#The get() method requires a key a first argument. As a second, optional argument,
#you can pass the value to be returned if the key doesn't exist:

alien_0 = {'color': 'green', 'speed': 'slow'}

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)

#consider using the get() method instead of the square bracket notation
#if you think the key you're asking for does not exist.

#if the second argument is left blank in the get() method and the key does
#no exist, Python will return a value of None.
#None means no value exists. This is not an error: it's a special value meant to
#indicate the absence of a value.



