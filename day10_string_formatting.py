# Write a Python program that:
# 1. Takes the student's name as input.
# 2. Takes the student's age as input.
# 3. Takes marks in Python, SQL, and HTML as input.
# 4. Converts the student's name into title case.
# 5. Calculates total marks out of 300.
# 6. Calculates the average marks.
# 7. Calculates the percentage.
# 8. Displays everything in a neatly formatted result card using f-strings.

Name = input("Enter your Name: ")
age = int(input("Enter your age: "))

sql_marks = int(input("Enter your SQL marks (0-100): "))
while sql_marks < 0 or sql_marks > 100:
    print("Invalid marks! Try again.")
    sql_marks = int(input("Enter your SQL marks (0-100): "))
    
HTML_marks=int(input("Enter your HTML_marks"))
while HTML_marks < 0 or HTML_marks > 100:
    print("Invalid marks! Try again.")
    HTML_marks= int(input("Enter your HTML marks (0-100): "))
    
python_marks=int(input("Enter your python_marks"))
while python_marks < 0 or python_marks > 100:
    print("Invalid marks! Try again.")
    python_marks = int(input("Enter your python marks (0-100): "))
    
Name = Name.title()
print(Name)
score = sql_marks + python_marks + HTML_marks
avrg_mark = score / 3
percentage = score / 300 * 100

print("\n========== STUDENT RESULT CARD ==========")

print(f"Student Name: {Name}")
print(f"Age: {age}")

print(f"SQL: {sql_marks}")
print(f"HTML: {HTML_marks}")
print(f"Python: {python_marks}")

print(f"Total Marks: {score} / 300")
print(f"Average Marks: {avrg_mark:.2f}")
print(f"Percentage: {percentage:.2f}%")

print("=========================================")