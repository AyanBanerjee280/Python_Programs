# Creating a multiplication table with f string.

num = int(input("Enter the number:\n"))
for i in range (1,201):
    print(f"{num}X{i}={num*i}")
