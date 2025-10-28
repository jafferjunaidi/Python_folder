try:
    num1=int(input("Enter first number: "))
    num2=int(input("Enter second number: "))
    result=num1/num2
    print(result)

except ZeroDivisionError:
    print("You can't divide by zero")
    
except Exception as e:
    print(e)
    
finally:
    print("The result is", result)