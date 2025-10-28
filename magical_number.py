# Task: The Magical Number
# Write a program that asks the user to enter a number. Based on the number, use conditional statements to decide and print the correct message:
# If the number is divisible by both 3 and 5, print "FizzBuzz".
# If the number is only divisible by 3, print "Fizz".
# If the number is only divisible by 5, print "Buzz".
# If the number is even and less than 50, print "Even & Small".
# If the number is odd and greater than 100, print "Odd & Large".
# Otherwise, print "Nothing Special".

# Ask the user to enter a number
number = int(input("Enter a number: "))

# Check conditions in order of priority
if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")
elif number % 2 == 0 and number < 50:
    print("Even & Small")
elif number % 2 != 0 and number > 100:
    print("Odd & Large")
else:
    print("Nothing Special")