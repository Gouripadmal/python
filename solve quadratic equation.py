
import math 
a = int(input("Enter the value of a:"));
b = int(input("Enter the value of b:"));
c = int(input("Enter the value of c:"));
solution = (-b+math.sqrt((b**2)-(4*a*c)))/(2*a);
solution1 = (-b-math.sqrt((b**2)-(4*a*c)))/(2*a);
print(solution);
print(solution1);
