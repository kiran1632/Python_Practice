#
#Ex.,simple function

def greet():
    print("Hello! welcome")
greet()

#Ex.,Function with argument

def welcome(name):
    print("Hello",name)
welcome("kiran")

#Ex.,Funtion with return value

def base(num):
    return num*num*num
ans=base(5)
print("Answer: ",ans)


def data(min):
    return min+min
total=data(8)
print("Addition: ",total)

#Function with multiple arguments

def num(a,b,c):
    return a+b-c
print("total :",num(10,20,10))


def all(a,b,c):
    return a+b*c
print("Total : ",all(12,14,2))

#Function with  *args

def min(*numbers):
    a=0
    for b in numbers:
        a+=b
    return a
print("Total: ",min(1,2,3,4,5))

#fuction with kwargs (key-value-argument)

def user_info(**info):
    for key, value in info.items():
        print(key,":",value)
user_info(name="kiran",age=25,city="Pune")



def information(**data):
    for key, value in data.items():
        print(key,":",value)
information(Name="kiran",Age=19,Class="BCA-2")


#Example:


def calculate_percentage(marks_obtained,total_marks):
    percentage=(marks_obtained/total_marks)*100
    return percentage
student_name="Kiran kadalage"
obtained=450
total=500
result=calculate_percentage(obtained,total)
print("Student: ",student_name)
print("Marks: ",obtained,"/",total)
print("Percentage: ",result,'%')

















































































































