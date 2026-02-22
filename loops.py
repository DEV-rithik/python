# question 1
a = int(input("enter a number: "))
factorial = 1
for i in range(1,a+1):
    factorial *= i

print(factorial)

# question 2
a= int(input("enter your first number:"))
b = int(input("enter your last number: "))
temp  = 0
for i in range(a,b+1):
    if(i % 2 == 0):
        print(i)
        temp += 1
print("total even numbers = " , temp)