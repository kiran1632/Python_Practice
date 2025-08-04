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

print("Using for loop: first five even numbers: ")
for i in  range(2,11,2):
    print(i)

#while loop: Print the 5 odd numbers

print("\nUsing for loop: first five odd numbers: ")
i=1
cout=0
while cout <5:
    print(i)
    i+=2 
    cout+=1




































































































































