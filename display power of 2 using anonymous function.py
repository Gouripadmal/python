number = int(input("Enter the number:"))

power= list(map(lambda x:2**x,range(number+1)))
print(power)    