import random
num1=random.randrange(1,100)
num2=int(input("Enter a number between 1 and 100: "))
if num1==num2:
    print("You guessed right!",num2,num1)
elif num2>num1:
    print("You guessed higher!",num2,num1)
else:
    print("you guessed lower!",num2,num1)
    