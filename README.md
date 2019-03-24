# firstNonRepeatingCharacter
Function that returns first non repeating character in a string.


Parameters:   A string.
Output : A char.


A new ,empty , dictionary is initialised.
Using a for loop iterate through the string , char by char . For every char, the following is done :
 --> if it is not in the dictionary , add it and set the value to 1 .(The key is the char ).
 -->if it is already in the dictionary , increase it's value.
 
Now there is a dictionary with the key value pair being  a char and it's number of ocurences.
Iterate through that dictionary untill a key value pair having value=1 is found, and return the key (meaning , the char)
