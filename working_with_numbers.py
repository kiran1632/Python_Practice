a="Ak12as67hj"
for char in a:
    if char.isdigit() == True:
        a = a.replace(char,"")
    else:
        pass

print(a)