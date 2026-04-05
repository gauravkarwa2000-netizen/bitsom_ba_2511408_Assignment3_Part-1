                                        #TASK-1: Data Parsing and Profile Cleaning
print('\n Task-1: Data parsing and profile cleaning')
print("TASK-1: Data Parsing and Profile Cleaning")

#Raw Data
raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]
#Calling special_name variable to use to store the name of roll number 103 inside the for loop 
special_name= None

#Looping thorough each student
for students in raw_students:
    # Step1: Cleaning and formating the names in student_name
    student_name= students["name"].strip().title()

    # Step2: Converting roll number to integer
    roll= int(students["roll"])

    # Step3: Converting marks string into list of integers
    marks_list= students["marks_str"].split(",")
    marks=[]
    for m in marks_list:               # for loop to store coverted strings into lists in integer format
        marks.append(int(m.strip()))

   # Step 4: Validating the student names
    is_valid = True
    for char in student_name.split():
        if not char.isalpha():
            is_valid = False

    # Step 5: Print validation result
    if is_valid:
        print("✓ Valid name")
    else:
        print("X Invalid name")

    # Step 6: Print formatted profile
    print("=" * 50)
    print(f"Student : {student_name}")
    print(f"Roll No : {roll}")
    print(f"Marks   : {marks}")
    print("=" * 50)


# Step 7: Storing Special student name for roll 103
    if roll == 103:
        special_name= student_name

#Step8: Printing special name in upper caps and lower caps
if special_name:
    print(special_name.upper())
    print(special_name.lower())


                                        #Task-2: Marks analysis using loops and conditions
print("Task-2: Marks analysis using loops and conditions")

student_name = "Ayesha Sharma"
subjects     = ["Math", "Physics", "CS", "English", "Chemistry"]
marks        = [88, 72, 95, 60, 78]

subject_marks= zip(subjects, marks)

print(f"\nstudent_name: {student_name}")
print("="*50)

#Part-1: Printing subject + grades
#Using for with nested if and else loops to compare the overall grades of the student
for s,m in subject_marks:    
    if 90<= m <=100:
        grade ="A+"
    elif 80<= m <=89:
        grade ="A"
    elif 70<= m <=79:
        grade ="B"
    elif 60<= m <=69:
        grade ="C"
    else:
        grade ="F"
    # Printing marks with grades while keeping space of 40 char
    print(f"{s:40} : {m} ({grade})")

#Part-2: Basic Calculations

    #Total Marks
    total_marks= sum(marks)
    #Average marks upto 2 decimal places
    avg_marks= round(total_marks/len(marks),2)

    #Highest Marks
    max_marks = max(marks)
    max_index = marks.index(max_marks)
    highest_subject = subjects[max_index]

    #Lowest Marks
    low_marks= min(marks)
    low_index = marks.index(low_marks)
    lowest_subject = subjects[low_index]

print("\n\n-------------------- Analysis --------------------")
print(f"Total Marks   : {total_marks}")
print(f"Average Marks : {avg_marks}")
print(f"Highest       : {highest_subject} ({max_marks})")
print(f"Lowest        : {lowest_subject} ({low_marks})")

#Part-3: Adding new subjects

new_count = 0

while True:
    sub = input("\nEnter subject name (or type 'done' to stop): ")

    if sub.lower() == "done":
        break

    mark_input = input("Enter marks between 0–100: ")

    # Validating if the inputed marks is positive digits or not within 0 to 100.
    if not mark_input.isdigit():
        print(" Invalid input (Marks should be in digits)")
        continue

    mark = int(mark_input)

    if mark < 0 or mark > 100:
        print(" Marks must be between 0 and 100")
        continue

    # Adding valid subjects and marks data
    subjects.append(sub)
    marks.append(mark)
    new_count += 1

# New calculations after the new subject and marks are added
updated_avg = round(sum(marks) / len(marks), 2)

print("\n----------- Updated Summary -----------")
print(f"New subjects added : {new_count}")
print(f"Updated average    : {updated_avg}")


                                        #Task-3: Class Performance Summary
print("Task-3: Class Performance Summary ")

#Raw Data
class_data = [
    ("Ayesha Sharma",  [88, 72, 95, 60, 78]),
    ("Rohit Verma",    [55, 68, 49, 72, 61]),
    ("Priya Nair",     [91, 85, 88, 94, 79]),
    ("Karan Mehta",    [40, 55, 38, 62, 50]),
    ("Sneha Pillai",   [75, 80, 70, 68, 85]),
]

# creating all the variables that will be required outside the loop to compare and print required data
print("Name              | Average | Status")
print("-"*36)

pass_count = 0
fail_count = 0

topper_name = ""
topper_avg = 0
total_avg_sum = 0

# Looping through statements
for name, marks in class_data:

    avg = round(sum(marks)/ len(marks), 2)

    # Code if student is pass or fail
    if avg >= 60:
        status = "Pass"
        pass_count += 1
    else :
        status = "Fail"
        fail_count += 1
    
    #Code to find topper in class data
    if avg > topper_avg:
        topper_avg = avg
        topper_name = name
    
    # Overall class average sum of students
    total_avg_sum += avg

    # Printing the formatted row for all the outputs
    print(f"{name:17} | {avg:7} | {status}")

#Code to print all the required outputs outside the loop
class_avg = round(total_avg_sum / len(class_data), 2)

print("\n--------- Summary ----------")
print(f"Passed : {pass_count}")
print(f"Failed : {fail_count}")
print(f"Topper : {topper_name} ({topper_avg})")
print(f"Class Average : {class_avg}")


                                        # Task-4: String Maipulation Utility
print("Task-4: String Maipulation Utility")

essay = "  python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.  "

# Step 1: Striping whitespaces form essay
clean_essay = essay.strip()
print("1. Clean Essay:")
print(clean_essay)

# Step 2: Title Casing the clean_essay
title_case = clean_essay.title()
print("\n2. Title Case:")
print(title_case)

# Step 3: Counting "python" from the title_case
count_python = clean_essay.count("python")
print("\n3. Count of 'python':", count_python)

# Step 4: Replacing python with Python 🐍 
replaced = clean_essay.replace("python", "Python 🐍")
print("\n4. Replaced Essay:")
print(replaced)

# Step 5: Spliting the essay into sentences
sentences = clean_essay.split(". ")
print("\n5. Sentences List:")
print(sentences)

# Step 6: structuring the sentences into numbered sentences
print("\n6. Numbered Sentences:")

for i, sentence in enumerate(sentences, start=1):

    # Ensure sentence ends with "."
    if not sentence.endswith("."):
        sentence += "."

    print(f"{i}. {sentence}")

