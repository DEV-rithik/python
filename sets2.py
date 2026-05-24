try:
    temp = list(map(float, input().split()))
    for value in temp:
        fahren = (9 / 5) * value + 32
        print(f"{value}C = {fahren}F")
except ValueError:
    print("invalid temperature value in list"   )