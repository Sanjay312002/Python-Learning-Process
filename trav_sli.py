#Traversal and Slicing

#Traversal
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

#method - 1

for i in range(len(fruits)):
    print(fruits[i])

print("Method - 2")
#method - 2
for j in fruits:
    print(j)


#Slicing
print("Slicing")
str1 = "Hello world"
print(str1[0])
print(str1[0:4]) #slicing from index 0 to 4
print(str1[0:]) #slicing from index 0 to end
print(str1[0:6:2]) #slicing from index 0 to 6 with step 2

# we can also slicing a list
print("Slicing a list")
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
print(fruits[0]) #accessing the first element of the list
print(fruits[0:4]) #slicing from index 0 to 4