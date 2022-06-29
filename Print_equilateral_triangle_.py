#write a program to find the sum of first n natural number using while loop

num = int(input("Enter the number:\n"))
if num<0:
    print("Please enter a positive number")
else:
    sum = 0
while num>0:
    sum += num
    num -= 1
print("The result is:", sum)