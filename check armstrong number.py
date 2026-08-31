number = input("Enter the number: ")

length = len(number)
sum = 0

for i in range(0, length):
    digit = int(number[i])
    sum = sum + digit ** length

if sum == int(number):
    print("Armstrong number")
else:
    print("Not an Armstrong number")