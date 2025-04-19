string = input("Введите текст: ")
i = 0
j = '#'
while i < len(string):
    if string[i] == j:
        break
    print(string[i:i+2])
    i += 1

