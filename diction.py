#Dictionary in python

from webbrowser import get


dict = {1:"sanjay"}
dict1 = {"name":"sanjay", "age":25, "city":"pune"}
dicts = {1:'one',2:'two',3:'three'}
print(dict)
print(dicts)
#this will raise an error because we cannot access the elements of a dictionary using indexing. We can access the elements of a dictionary using keys.
# print(dict1[0]) 
print(dict1["name"]) #accessing the value of the key "name"
print(dicts[1]) #accessing the value of the key 1

#get - method is used to access the value of a key in a dictionary. If the key is not present in the dictionary, it will return None instead of raising an error.
print(dict1.get("name")) #accessing the value of the key "name" using get() method
print(dict1.get("salary")) #accessing the value of the key "salary" using get() method
#if the value of the key is not present in the dictionary, it will return None instead of raising an error. We can also provide a default value to be returned if the key is not present in the dictionary.

#values() - method is used to access the values of a dictionary. It will return a view object that displays a list of all the values in the dictionary.
print(dict1.values()) #accessing the values of the dictionary using values() method
#keys() - method is used to access the keys of a dictionary. It will return a view object that displays a list of all the keys in the dictionary.
print(dict1.keys()) #accessing the keys of the dictionary using keys() method

#items() - method is used to access the items of a dictionary. It will return a view object that displays a list of all the items in the dictionary.
print(dict1.items()) #accessing the items of the dictionary using items() method    

#inserting a new key-value pair in a dictionary. We can insert a new key-value pair in a dictionary using the assignment operator. If the key is already present in the dictionary, it will update the value of the key.
dict1["salary"] = 50000 #inserting a new key-value pair in the
print(dict1) #printing the dictionary after inserting a new key-value pair
nums = {1:'one',2:'two',3:'three'}
nums[4] ='four' #inserting a new key-value pair in the dictionary
print(nums) #printing the dictionary after inserting a new key-value pair

#deleting a key-value pair from a dictionary. We can delete a key-value pair from a dictionary using the del keyword. If the key is not present in the dictionary, it will raise an error.
print("Before deletion:", nums) #printing the dictionary before deleting a key-value pair
nums.pop(4) #deleting a key-value pair from the dictionary using pop() method
print("After deletion:", nums) #printing the dictionary after deleting a key-value pair


# Quiz
map = {5: {'P': {5:"P"}, 6:"Q"}, 7: "R", 'Q': "S","S" : 'T'}
print("Answer of the quiz:",map[map[map[5][6]]]) #accessing the value of the key 5 in the dictionary
#Explain - The code accesses the value of the key 5 in the dictionary, then uses that value as a key to access another value in the dictionary, and so on.