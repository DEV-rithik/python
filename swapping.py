result = ""
for char in string:
    num = ord(char)
    if 65 <= num <= 90:
        result += chr(num + 32)
    elif 97 <= num <= 122:
        result += chr(num - 32)
    else:
        result += char

num = input("enter a word")
print(result) 