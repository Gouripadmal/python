#num = int(input("Enter the number:"))
number = int(input("Enter the octal number:"))

binary = ""
octal = ""
# while num > 0:
#     remainder = num % 2
#     binary = str(remainder) + binary
#     num = num // 2

#print(binary)
while num > 0:
    remainderrr = number % 8
    octal = str(remainderrr) + octal
    number = number // 8
print(octal)