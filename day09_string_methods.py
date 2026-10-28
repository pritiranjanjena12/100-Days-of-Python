# Write a Python program that:
# 1. Asks the user to enter their full name, allowing accidental spaces at the beginning and end.
# 2. Removes the extra spaces from the name.
# 3. Displays the name in title case.
# 4. Displays the name in uppercase and lowercase.
# 5. Asks the user to enter their favorite programming language.
# 6. Removes extra spaces from that input and displays it in lowercase.
# 7. Replaces the word "python" with "Python" in the cleaned language text.
# 8. Displays the number of characters in the cleaned full name using len().

#Asking user to input their Full Name.
# 2.removes the extra spaces from the name.
Name = input("Enter your name: ")
Name = Name.strip()

# 3.display the name in title case.
print(Name.title())

# 4.display the name in uppercase and lowercase 
print(Name.lower())
print(Name.upper())

# 5.Ask the to enter their favorite proggramming language
fvrt_programing=input("enter your fvrt programing language: ")

# 6.removes the extra spaces from that input and display it in lowercase.
cleaned_language = fvrt_programing.strip().lower()
print(cleaned_language)

# 7. Replaces the word "python" with "Python" in the cleaned language text.
print(cleaned_language.replace('python', 'Python'))

# 8. Displays the number of characters in the cleaned full name using len().
print(len(Name))