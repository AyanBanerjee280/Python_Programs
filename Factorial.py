#Write a program to find a factorial of a given number

num = int(input("Enter the number to find its factorial: "))
factorial = 1
for i in range(1, num+1):
    factorial = factorial * i
print(f"The factorial of {num} is {factorial}")