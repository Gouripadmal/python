number1=int(input("Enter the first number:"));
number2=int(input("Enter the second number:"));
number3=int(input("Enter the third number:"));
if (number1>number2) and (number1>number3):
    print(number1," is greatest")
elif(number2>number1) and (number2>number3):
    print(number2," is greatest")
else:
    print(number3," is greatest")