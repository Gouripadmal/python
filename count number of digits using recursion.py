def digit_sum(n):
 number_of_digits=0;
    if n == 0:
        return 0
    return n % 10 + digit_sum(n // 10)
number_of_digits = number_of_digits + 1
print(digit_sum(1234))
print(number_of_digits)