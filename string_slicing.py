
name="Johnsmith" 
print(name[-1]) # Accessing the last character of a string using negative indexing  

# start:stop:step  
# start: The index to begin the slice (inclusive)
# stop: The index to end the slice (exclusive)
# step: How many characters to skip (default is 1)


# slicing examples
print(name[0:5]) # Slice from index 0 to 4
print(name[7:]) # Slice from index 7 to end
print(name[:5]) # Slice from beginning to index 4
print(name[::2]) # Slice the whole string with steps of 2 print every second character
print(name[1:])  # print from index 1 to the end
print(name[:-1]) # exclude the last character
print(name[:-3]) # Exclude the last three characters
print(name[::-1]) # Reverse the string
print(name[0:5:3]) 
#  What it means:
#  start = 0 → Start from index 0 ('P')
#  stop = 5 → Go up to index 5 (but not including it, so 's' is the last considered)
#  step = 3 → Take every 3rd character from that range

# Index:  0   1   2   3   4
# Char : 'J' 'o' 'h' 'n' 's'