#Assignments - Python Fundamentals
#A. Python is an indent based programming language
#The following program throws an indentation error. Correct it and make sure it prints properly.

teams = ['Data', 'AI', 'DevOps']
for t in teams:
    print('Hello', t, 'Team from Inceptez Technologies')
print('Keep Learning and Exploring!')

######################################################################################################
#B. Commented line in Python
#Use Case 1:
#Add single-line and multi-line comments to describe what the below code does for Inceptez Technologies training tracker.

students = 100 # Variable students is assigned with 100 value
trainers = 2 # Variable trainers is assigned with 2 value
''' We add students and trainers value and assign it to total
After caluculating the total we are printing the total value'''
total = students + trainers
print(total)

#Use Case 2:
#Convert the below block into a “dead code” using comments, then re-activate it later to print

''' dead code
print("Welcome to Inceptez Python Learning")
'''

######################################################################################################
#C. Playing with Quotes
#Use Case 1:
#Create three string variables that correctly store and print:
#This is Inceptez's "Python" class for Data Engineers & AI Engineers → Use single, double, and triple quotes appropriately.

str1 = "Data Engineer"
str2 = 'AI Engineer'
str3 = "DevOps Engineer"
print("""This is Inceptez's "Python" class for""",str1, ",", str2, "&", str3)

#Use Case 2: Multiline string

multiline_str = """Welcome to Inceptez Technologies!
Python Training: Basics
Enjoy your learning journey."""
print(multiline_str)

######################################################################################################
#D. Let's learn all about VARIABLES
#Use Case 1:
'''Declare variables to store the following details:
- Student Name
- Course Name (e.g., “Python Fundamentals”)
- Training Institute Name (Inceptez Technologies)
Then print a formatted message:
Name: Arun is learning the course Python Fundamentals at the institute Inceptez Technologies '''

student_name = "Arun"
course_name = "Python Fundamentals"
training_institute_name = "Inceptez Technologies"
print("Name:", student_name,"is learning the course",course_name,"at the institute",training_institute_name)

#Use Case 2:
#Demonstrate dynamic inference, dynamic typing using with fee by applying .18 gst  and prove strongly typing character also by operating it with Eighteen percent gst

fee = 45000 #int Dynamic inference
print("fee type",fee, type(fee))
gst_rate = 0.18 #float Dynamic inference
print("gst_rate type",gst_rate,type(gst_rate))

gst_amount = fee*gst_rate
print("gst_amount type",gst_amount,type(gst_amount))
total = fee + gst_amount
print("total type",total,type(total))

fee = 1000.50 # Dynamic Typing
print("fee type",fee, type(fee))
gst_rate = "eighteen percentage" #string Dynamic typing
print("gst_rate type",gst_rate,type(gst_rate))
# print(fee*gst_rate) # strongly typed

######################################################################################################
#E. Variables Naming Conventions
#Use Case 1:
#Identify which variable names below are invalid for Inceptez’s student database:
'''
2student = 'Ravi' #invalid started with number
_student_id = 1001 #valid
studentName = 'Priya' #valid
class name = 'Python' #invalid keywords can't be used
inceptez_batch = 'Morning' #valid

#Use Case 2:
#Declare 3 variables following naming styles for Inceptez projects:

DataEngineeringBatch = "WE49" #PascalCase
dataEngineeringBatch = "WE45"#camelCase
data_engineering_batch = 100 #snake_case
'''
######################################################################################################

#F. Type identification & Casting
#Use Case 1:
#Write a program that asks for an employee’s age.
#1. Checks its type is of string (think about using isinstance() function)
#2. Converts it to int (continue writing your program from here..)
#3. Prints the years pending for retirement, for eg. 60 is the retirement age.
#Example:
#Enter your age: 40
#You will retire in 20 years at Inceptez Technologies.
'''
age: str =str(input("Enter your age:"))#Converting the type after getting input from user
print(type(age))
#Check whether the given input is of type str or not?
print(isinstance(age,str))
years_to_retire = 60 - int(age)
print("age of the person to retire ",years_to_retire)
'''


#Use Case 2 (Debug):
#Fix the type error in the following code for salary calculation:

salary = '50000'
bonus = 10000
print('Total Salary in Inceptez:', int(salary) + bonus)

######################################################################################################

#G. Data types and casting
#Use Case 1 — Employee Salary Breakdown Using Numeric & String Types
#Employee Salary Breakdown
#a. Write a program that asks the user for:
#employee_name (string)
#base_salary (float)
#hra_percent (integer)
#bonus_amount (float)
'''
employee_name:str = input("Enter your employee name:")
base_salary:float = float(input("Enter your base salary:"))
hra_percent:int = int(input("Enter your hra percentage:"))
bonus_amount:float = float(input("Enter your bonus amount:"))

HRA = base_salary * (20 / 100)
Total_Salary = base_salary + HRA + bonus_amount
print("Employee:",employee_name)
print("Base Salary",base_salary)
print("HRA @ 20%",HRA)
print("Total Salary Payable",Total_Salary)

#Use Case 2: Student Result Classification
#a. Write a program that takes marks as input (initially as a string).
#B. Check if the value can be converted to float.
#C. Then classify (try using if condition with the help of AI, however we will learn about if condition soon):
#Marks >= 90 --> Outstanding
#Marks >= 75 --> Excellent
#Marks >= 50 --> Pass
#Marks < 50 --> Fail
#D. If the input is not numeric, print:
#Invalid marks entered — Please provide numeric input.

mark = str(input("Enter your mark:"))
print(type(mark))
mark = float(mark)
print(type(mark))

if mark>=90:
    print("Result: Outstanding")
elif mark>=75:
    print("Result: Excellent")
elif mark>=50:
    print("Result: Pass")
else:
    print("Result: Fail")

#D. If the input is not numeric, print:
#Invalid marks entered — Please provide numeric input.

check_mark_input = input("Enter your mark:")
if not isinstance(check_mark_input,int):
    print("Enter mark in integer format")
'''

#Use Case 3: Bug Fixing — Datatype Mismatch
#The below code is intended to calculate total price, but it has datatype errors. Fix it.
#Incorrect code:
item_name = input("Enter product name: ")
price = float(input("Enter price per item: "))
quantity = int(input("Enter quantity: "))
total_cost = price * quantity
print("You purchased " + str(quantity) + " units of " + item_name)
print("Total payable: " + str(total_cost) +" INR")
######################################################################################################
