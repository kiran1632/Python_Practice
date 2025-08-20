#

#in python, conditional statements are used  to execute a block of code depending on whether a condition is true or false. 

#if- statement :-  Used to run a block of code only if a condition is true
'''
x=10
if x >5:
    print("x is grether than 5")

#if-else statement:- Adds on  alternative block if the condition is false

x=3
if x>5:
    print("x is grether than 5")
else:
    print("x is 5 or less")

#if - elif-else ladder :- Used when you have multiple conditions

x=5
if x>5:
    print("x is grether than 5")
elif x==5:
    print("x is equal to 5")
else:
    print("x is less than 5")

#nested if statement:- An if statement  inside another if.

x=10
y=20
if x>5:
    if y>15:
        print("Both condition are true")  #
    else:
        print("only x>5 is true")



#Python program using All Conditional Statements:

name= str(input("What is your name? "))
age=int(input("What is your age? "))
marks=int(input("How mnay marks did you get? (0 to 100): "))
print(f"\nHello, {name}!")

#1. simple if
if age>= 18:
    print("You are eligible to vote.")
#2. if else
if marks>=40:
    print("You have passed exam")
else:
    print("You have failed the exam")

#3. if-elif-else
if marks>=90:
    print("You got an A+ grade.")
elif marks>=75:
    print("You got a B grade.")
elif marks >=60:
    print("You got a C grade.")
else:
    print("You did not gate any grade.")

#Nested if
if age >=18:
    if marks>=60:
        print("You are eligible for collage admission.")
else:
    print("You are too young for collage admission.")

'''


'''

mark=int(input("Enter marks: "))
if mark >=90:
    print("You got A+ grade")
elif mark >=80:  
    print("You got A grade")
elif mark>=70:
    print("You got B+ grade")
else:
    print("Student is failed")
'''
'''
a="kiran kadalage"
b=19
wight=55.60
fruits=["apple","banana","orange"]
subjects=("English","maths","physics","biology")
info={"Class":"BCA 2nd year","Semister":"3rd","Age":19,}
marks=(67,79,85,96)
print(a)
print(b)
print(wight)
print(fruits)
print(subjects)
print(info)
print(marks)
'''

def greet(name):
    print("Hello,", name)
greet("rahul")

def greet():
    print("Hello, कसा आहेस?")
greet()


















































































































