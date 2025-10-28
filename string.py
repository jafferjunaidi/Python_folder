# name=input("Enter your name: ")
# print(name)

# c = len(name) # Count the number of characters in the string
# print(c)
# print("The number of characters in your name is:", c) 

# Print the characters in reverse order
# for i in range(c - 1, -1, -1):  
#   print(name[i]) 

# stdname = "John Doe"
# for a in stdname:
#  print(a)  # Print each character line by line  

# string format
# bio="Hi, my name is {} and I'm student of Aptech-{}".format("Jaffer","MSG")
# bio="Hi, my name is {0} and I'm student of Aptech-{1}".format("Jaffer","MSG") #index=0 is Jaffer, index=1 is MSG 
# bio="Hi, my name is {name} and I'm student of Aptech-{branch}".format(name="Jaffer", branch="MSG") 
# print(bio)

# name = "Abid"
# age = 23              # {} placeholders
# details = f"{name} is {age} years old" # Using f-string(formatted string literal) combine variables into a string in a readable way
# print(details) 

#string methods
# stdname2 = input("Enter your name: ")
# print(stdname2.title()) # Convert the first character of each word to uppercase
# print(stdname2.upper()) # Convert all characters to uppercase
# print(stdname2.lower()) # Convert all characters to lowercase
# print(stdname2.capitalize()) # Convert the first character to uppercase and the rest to lowercase

stdname3="Jaffer5188" 
# print(stdname3.find("i",2)) # searching for character "i" starting from index 2 and rest of the string if found it will print the index, if not found it will return -1
# print(stdname3.find("r",3)) #  r is found at index 5, it will print 5

# print(stdname3.index("u")) # searching for character "u" in the string stdname3, if not found it will raise an error
# print(stdname3.index("a")) # a is found at index 1, it will print 1

# print(stdname3.isalpha()) # Checks whether all the characters in the string stored in variable are alphabetic (A–Z or a–z).
                          # If all characters are letters (no digits, symbols, spaces, punctuation), it returns True otherwise returns False
                          
# print(stdname3.isnumeric()) # Checks whether all the characters in the string stored in variable are numeric (0–9).
                            # If all characters are digits, it returns True otherwise returns False
                            # If there is anything non-numeric (like letters, spaces, symbols), it returns False.

# print(stdname3.isalnum()) # Checks whether all the characters in the string stored in variable are alphanumeric (A–Z, a–z, 0–9).
                          # If all characters are letters or digits, it returns True otherwise returns False
                          # If there is anything non-alphanumeric (like spaces, symbols, punctuation), it returns False.
