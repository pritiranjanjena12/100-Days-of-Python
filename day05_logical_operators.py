
# Day 5: Python Logical Operators
# Topics: and, or, not

print("=== Exam Eligibility Checker ===")

# Take input from the user
marks = float(input("Enter your marks: "))
attendance = float(input("Enter your attendance percentage: "))

# Check individual requirements
marks_requirement = marks >= 40
attendance_requirement = attendance >= 75

# Use logical operators
eligible = marks_requirement and attendance_requirement
extra_eligible = marks_requirement or attendance_requirement
not_eligible = not eligible

# Display results
print("\n=== Results ===")
print("Marks requirement:", marks_requirement)
print("Attendance requirement:", attendance_requirement)
print("Eligible for exam:", eligible)
print("At least one requirement met:", extra_eligible)
print("Not eligible for exam:", not_eligible)