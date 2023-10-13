
age = int(input("ENter your age: "))
print(f"Your age is: {age}")

if age>=18 and age<=60:
    print("You can get driving license")

elif age<18:
    print("Too Young")

elif age>60:
    print("too old")


Mans = [15, 18, 21, 6, 65, 79, 46, 56,13]
print("Minimum eligible age is 18")

for i in Mans:
    if i>18 and i<65:
        print(f"Eligible and your age is {i}")

    else:
        print(f"Not eligible and your age is {i}") 

print("End")


