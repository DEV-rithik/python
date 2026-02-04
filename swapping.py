text = "Code Quest 2026!"
result = ""

for char in text:
    num = ord(char)
    if 65 <= num <= 90:
        result += chr(num + 32)
    elif 97 <= num <= 122:
        result += chr(num - 32)
    else:
        result += char

print(result)