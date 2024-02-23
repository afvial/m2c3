# Exercise 7: Get the first word from your string using indexes. Use the upper function to transform the letters into uppercase. Create a new string that takes the uppercase word and the rest of the original string.

string_one = 'hello world'

string_two = string_one[:5].upper() + string_one[5:]

# string_three = string_two + string_one[5:]

print(string_two)
print(type(string_two)) 
