#check whether a number is a prime number or not

num = int(input("Enter the number: "))
for i in range (2, num):
    prime = True
    if (num%i ==0):
        prime = False
        break
if prime:
    print("This number is a prime number.")
else:
    print("This number is not a prime number.")