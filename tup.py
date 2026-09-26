#tuples are immutable
tup = (10,20,30,40,50)
print(tup)

print(tup[0]) #accessing the first element of the tuple
print(min(tup)) #min() function is used to find the minimum value in the tuple.
print(max(tup)) #max() function is used to find the maximum value in the tuple
print(len(tup)) #len() function is used to find the length of the tuple.
#we cannot modify the elements of a tuple, but we can access the elements of a tuple using indexing and slicing. We can also concatenate and replicate tuples, but we cannot change the elements of a tuple.
tup[0] = 100 #this will raise an error because tuples are immutable
print(tup)

#we cannot als sorting the elements of a tuple because tuples are immutable. We can convert the tuple to a list, sort the list, and then convert the list back to a tuple if we want to sort the elements of a tuple.
