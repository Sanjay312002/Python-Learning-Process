#conditional statment

if( 5 == 4):
    print("5 is equal to 5") #Indentation(the space before the print) inside the if block is important in python.


print("Hi")

a = 7
b = int(input("Enter a number for b: "))

if( a == b):
    print("a is equal to b")
elif( a > b):
    print("a is greater than b")
else:
    print("a is not equal to b")



#nested if else
age =int(input("Enter your age: "))
eat_pizza = False
exercise = False

if(age < 30):
    if(eat_pizza):
        print('unfit')
    else:
        print('fit')
else:
    if(exercise):
        print('fit')
    else:
        print('unfit')
    





#Ternary operator


print("You are eligible for vote") if age > 18 else print("Child")