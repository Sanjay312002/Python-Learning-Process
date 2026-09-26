#list

heigh_list = [170,167,182,193,155]
print(heigh_list)
#accessing list elements
print(heigh_list[3])
#negative indexing
print(heigh_list[-3])

#changing list elements
heigh_list[4]=177
print(heigh_list)

lis1=[1,2,3,4]
lis2 =[5,6,7,8]
#concatenation of two lists
lis3 = lis1 + lis2
print(lis3)

#replication of list
lis4 = 3 * lis2 # 3times the lis2 values will be printed
print(lis4)

#append
lis=[1,2,3,4,5,6,7,8,9]
lis.append(10) #append() method is used to add an element at the end of the list.
print(lis)
#len() function is used to find the length of the list.
print(len(lis))

 #extend() method is used to add the elements of one list to the end of another list.
lis1.extend(lis2) # same as concatenation of two lists
print(lis1) #concatenate the 2nd list and stored in the 1st list


#return the index of the ele(returns the index of the first occurrence of the specified element in the list. If the element is not found, it raises a ValueError.)
#index() method is used to find the index of the first occurrence of the specified element in the list. If the element is not found, it raises a ValueError.
print("index of 3 in list: ",lis.index(3)) 

#count a ele 
print("count a ele in list: ",lis.count(3))

print(min(lis)) #min() function is used to find the minimum value in the list.
print(max(lis)) #max() function is used to find the maximum value in the list

list2 = [7,48,4,1,0,3,9,5,2,6]
#sort() method is used to sort the elements of the list in ascending order. It modifies the original list.
print("before sorting:",list2)
list2.sort()
print("After sorting:",list2)

#decending order
list2.sort(reverse=True)
print("After descending sorting:",list2)

 #clear() method is used to remove all the elements from the list.
#lis1.clear()
#print("clear list:", lis1)

#Mutable: Lists are mutable, which means that their elements can be changed after the list has been created. This allows for dynamic modification of the list's contents, such as adding, removing, or updating elements.
mut = [0,1,2,3,4,5]
print("original List(Before Mutable): ",mut) #output: [0, 1, 2, 3, 4, 5]
mut[0] = 1000
print("Mutable List: ",mut) #output: [1000, 1, 2, 3, 4, 5]

pop_list = [1,2,3,4,5,6,7,8,9]
#pop() method is used to remove and return the last element from the list. If an
#    index is specified, it removes and returns the element at that index. If the list is empty, it raises an IndexError.
print("Before pop(): ",pop_list)
print("After pop(): ",pop_list.pop()) #removes the last element from the list and returns it.   
print("Pop particular ele:",pop_list.pop(3)) #removes the element at index 3 and returns it.

#nested List: A nested list is a list that contains other lists as its elements. It allows for the creation of multi-dimensional data structures, where each inner list can represent a row or a collection of related items. Nested lists can be accessed and manipulated using indexing and slicing, just like regular lists.
nested_list = [[1,2,3],[4,5,6],[7,8,9]]
print("Nested List: ",nested_list)
print("Access first sublist: ",nested_list[0])
print("Access second sublist: ",nested_list[1])
print("Access second element of first sublist: ",nested_list[0][1]) #accessing the 2nd element of the first sublist
print("Access third element of second sublist: ",nested_list[1][2]) #accessing the 3rd element of the 2nd sublist
#negative indexing in nested list
print("Access last sublist: ",nested_list[-1]) #accessing the last sub  list
print("Access last element of last sublist: ",nested_list[-1][-1]) #accessing the last element of the last sublist