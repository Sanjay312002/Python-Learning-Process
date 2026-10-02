# reading the file

# file = open('info.txt','r')
#file = open('../files/text2.txt','r') # relative path

# print(file.read(10)) #file.read(10) read the first 10 characters of the file
#print(file.read())  #file.read() # read the entire file

#print(file.readline())  #file.readline() read the firstline of the file (if i use this method again it read the next line of the file)

# print(file.readlines()) #file.readlines() read the entire file and return a list of lines in the file
# file.close()

#write the file

#file = open('info.txt','w') # it remove existing content in file and write new content in the file
# write the entire file 
file = open('info.txt','a') # it append(add) the content in the file without removing existing content in the file
#file.write("Java is a programming language") 

lst = ['Mentalist', 'is', 'detective series']
file.writelines(lst) # it write the list of lines in the file
file.close()


# this is the best way to read the file because it automatically close the file after reading the file
with open('info.txt','r') as file:
    print(file.read())