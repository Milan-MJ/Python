# Program to find the Sum of the digits of a number.
num = int(input("Enter a number: "))
sum_of_digits = 0
while num > 0:
    digit = num % 10  
    sum_of_digits += digit 
    num = num // 10  
print("Sum of the digits:", sum_of_digits)
