number = int(input("Enter the number:"))
start = int(input("Enter the starting number:"))
end = int(input("Enter the ending number:"))
for num in range(start,end+1):
    if(number%num)==0:
        print("Enter the number:")
else:
    print(number)

        