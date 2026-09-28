set1 ={1,2,3,4,5,6,7,8,9,10}
print(type(set1))
print(set1)

print("try to add a new element to the set")
#adding a new element to a set. We can add a new element to a set using the add() method. If the element is already present in the set, it will not be added again.
set1.add(12)
print(set1)

print("try to add multiple elements to the set")
#adding multiple elements to a set. We can add multiple elements to a set using the update() method. If the elements are already present in the set, they will not be added again.
set1.update([13,14,15])
print(set1)

print("try to add duplicate element to the set")
#if we try to add a duplicate element to a set, it will not be added again. Sets do not allow duplicate elements.
set1.add(12) #adding a duplicate element to the set
print(set1) #printing the set after adding a duplicate element

#removing an element from a set. We can remove an element from a set using the remove() method. If the element is not present in the set, it will raise an error.
print("try to remove an element from the set")
set1.remove(12) #removing an element from the set
print(set1) #printing the set after removing an element

# #try to remove an element that is not present in the set. It will raise an error.
# print("try to remove an element that is not present in the set")
# set1.remove(77) #removing an element that is not present in the set
# print(set1) #printing the set after removing an element that is not present in the set

#try to remove an element that is not present in the set using discard() method. It will not raise an error.
print("try to remove an element that is not present in the set using discard() method")
set1.discard(77) #removing an element that is not present in the set using discard() method
print(set1) #printing the set after removing an element that is not present in the set

print("try to delete all ele")
set1.clear()
print(set1)

#typecasting
print("convert list to set")

lis = [1,2,5.5,3]
print("list: ",lis)
set2 = set(lis)
print("convert into set: ",set2)
print(type(set2))

#union intersection

#union
set3 = {2,3,4}
set4 = {1,4,5}
print("union")
set3.union(set4)
print("result of union: ",set3)
print("intersection")
print("result of intersection:",set3.intersection(set4))
print("difference")
print("result of difference: ",set3.difference(set4))
