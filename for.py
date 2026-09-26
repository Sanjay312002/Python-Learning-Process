for i in range(50):
    print("Hi Hello")


# in python we can use for loop to iterate over a sequence of numbers, strings, lists, tuples, dictionaries, sets etc. The range() function is used to generate a sequence of numbers.
#in python the range() function is used to generate a sequence of numbers. It takes three arguments: start, stop, and step. The start argument is the starting number of the sequence, the stop argument is the ending number of the sequence, and the step argument is the difference between each number in the sequence. The range() function returns a range object, which can be converted to a list or tuple using the list() or tuple() functions.
#in the range funtion it iterate before the stop value and it will not include the stop value in the output. The step value is optional and defaults to 1 if not provided. If the step value is negative, the sequence will be generated in reverse order.
print("from 0 to 20")
for j in range(20):
    print(j)


print("from 1 to 10") 
for i in range(1,10):
    print(i)

print("from 15 to 1")
for k in range(15,0,-1):
    print(k)

print("from 0 to 20 with step 2")
for m in range(0,20,2):
    print(m)

#quiz1
for l in range(5,11,2):
    print(l,end=" ") #end=" " is used to print the output in the same line with a space between them. By default, the print() function adds a newline character at the end of the output, which causes each print statement to be printed on a new line. By specifying end=" ", we are telling the print() function to use a space instead of a newline character at the end of the output. This allows us to print multiple values on the same line with a space between them.

    