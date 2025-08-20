#For loop: use for loop when you want to repeat  an use for each item in a sequence (like., list,string, or range)
''''
#synatax:

#for variable in sequence:
    #code to repeat



#eg.1] loop using range()

for i  in range (5):
    print(i)

#eg.2] loop through a list

fruits=["apple","banana","cherry"]
for fruit in fruits:
    print(fruit)

#while loop: Use while loop when you want to repeat code as long as condition is true . you don't need to know exatctly how many times it will repeat
#synatx:

while condition :
    #code to repeat

#eg.1

count=1
while count<=10:
    print(count)
    count+=1
'''
#eg. 2] break and continue
'''
for i in range (10):
    if i==4:
        break
    print(i)
'''
#eg.
'''
for i in range (10):
    if i==2:
        continue
    print(i)
'''

#Python program using for and while loops

#for loop: Print the first 5 even numbers
'''
print("Using for loop: first five even numbers: ")
for i in  range(2,11,2):
    print(i)
'''
#while loop: Print the 5 odd numbers
'''
print("\nUsing for loop: first five odd numbers: ")
i=1
cout=0
while cout <5:
    print(i)
    i+=2 
    cout+=1
'''
'''
i=1
cout=0
while cout <5:
    print(i)
    i+=2
    cout+=1
'''
'''
age=19
name="kiran"
fruits=["banan","mango","apple"]
number=(12,15,16,18,19)
info={f"\nname ": "kiran","\nage":19,"\ngame":"kho-kho"}
print(age)
print(name)
print(fruits)
print(number)
print(info)


if(age>18):
    print("eligible to vote")
elif(age== 19):
    print("your age is 19")
else:
    print("Not eligibal to vote")
'''
'''
fruits=["apple","banana","mango"]
for fruit in fruits:
    print(fruit)
'''
'''
num=int(input("Enter a number: "))
for  i in range(1,11):
    print(i*num)
'''
'''
a=5
b=5
while b<11:
    print(b*a)
    b+=1
'''

num=2

for i in range(5,11):
    print(i*num)
    


























































































































































































































































































































































