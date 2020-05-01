name_of_file = input("Введите имя файла: ")
name_of_file += ".txt"

count = 0
with open(name_of_file) as file:
    lines = file.readlines()
    for line in lines:
        print(line)
    print(lines)
    print(type(lines))
    print(len(lines))
    print(lines)
