#input from user

name = input();
print("Before type conversion:", name)
print(type(name)) #whatever input we give it will be considered as string by default. So the type of name will be string. 
#so what we should do is we should convert the input into integer or float if we want to perform any mathematical operation on it.
num = int(input("Enter a number: ")) #the input will be converted into integer using int() function.
#the type conversion is done using int() function. It will convert the input into integer,float(for that we use float instead of int).
print("After type conversion:", num)
print(type(num))
print(num + 10) #now we can perform mathematical operation on it.