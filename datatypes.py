# Python Datatypes

# Integer
i=-24
print(i,type(i))

# String
name="Jaffer"
print(name,type(name))

employee='Hamza'
print(employee,type(employee))

# Float 
f=27.6
print(f,type(f))

# Complex
c=16+4j
print(c,type(c))

std_name= ''' 
Aman is a good student.
He loves programming and enjoys learning new things. 
'''
print(std_name)

# List
values=[1, 2, 2, 3, 4, "Noman",True]  #List can contain different data types
print(values[5])   # Accessing and updating list values
values[5]="Fahad"  #update value at index 5
print(values[5])   # Accessing updated value
values.append(7) # Adding a new value to the list in the end
#values.insert(1,34)  # Inserting a new value at index 1
#values.remove(2)  # Removing the first occurrence of 2 from the list
values.pop(5)  # Removing the value at index 5
print(values,type(values))  # Printing the list and its datatype

# Set (Set is an unordered collection of unique elements)
myset={24,26,28,30,32,"Abid",True}  # Set can contain different data types
myset.add(34)  # Adding a new value to the set
myset.remove(26)  # Removing the value 26 from the set
print(myset,type(myset))  # Printing the set and its datatype

# Tuple (Tuple is immutable, meaning it cannot be modified after creation)
fruit=("Mango",)
# fruit=["Mango"] # List can be modified
fruit[0]="Orange"
print(fruit,type(fruit))

# mapping dictionary (Dictionary is a collection of key-value pairs)
# A dictionary is a mutable, unordered collection of items.
# It is defined by a pair of curly braces containing key-value pairs.

std_data={"name":"Jaffer", "age":24, "lab":"PR2-2022-10B", "teacher":"Miss Aqsa"}
print(std_data["name"])  # Accessing value by key
print(std_data.keys()) # printing all keys from the dictionary
print(std_data.values())  # printing all values from the dictionary
print(std_data.items())  # printing all key-value pairs from the dictionary
print(std_data,type(std_data))  # Printing the dictionary and its datatype