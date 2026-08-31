number = int(input("Enter the number:"))
for i in range(2,numbert):
    if(number%i)==0:
        print("")
        break
else:
        print("The numbers divisible by another number")
        print(i)