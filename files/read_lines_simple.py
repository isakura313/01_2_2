name_of_file = input("Введите имя файла: ")
name_of_file += ".txt"

count = 0
with open(name_of_file) as file:
    for line in file:
        if line == '\n':
            break
        print(count, line.strip())
        count += 1
