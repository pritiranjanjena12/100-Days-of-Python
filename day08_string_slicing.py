# Write a Python program that takes a username as input and performs these operations:
# 1. Print the complete username.
# 2. Print its first character.
# 3. Print its last character.
# 4. Print the first three characters.
# 5. Print the username in reverse order.
# 6. Print the total number of characters.

#taking username as input 
username = input ("Enter your username: ")

# 1. Print the complete username.
print (username)

# 2. Print the first character.
print (username[0])

# 3.print the last character.
print (username[-1])

# 4. print the first three characters.
print (username[0:3])

# 5. print the username in reverse order.
print (username[::-1])

# 6. print the total number of characters.
print (len(username))