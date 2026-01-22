print("Enter a decimal number")
n = int(input())

print("Choose conversion")
print("1. Binary")
print("2. Octal")
print("3. Hexadecimal")
choice = int(input())

if choice == 1:
    temp = n
    result = ""
    if temp == 0:
        result = "0"
    while temp > 0:
        result = str(temp % 2) + result
        temp = temp // 2
    print("Binary:", result)

elif choice == 2:
    temp = n
    result = ""
    if temp == 0:
        result = "0"
    while temp > 0:
        result = str(temp % 8) + result
        temp = temp // 8
    print("Octal:", result)

elif choice == 3:
    temp = n
    result = ""
    x = "0123456789ABCDEF"
    if temp == 0:
        result = "0"
    while temp > 0:
        result = x[temp % 16] + result
        temp = temp // 16
    print("Hexadecimal:", result)

else:
    print("Invalid choice.")
