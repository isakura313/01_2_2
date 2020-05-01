name_of_file = input("Введите имя файла для анализа")
name_of_file += '.txt'

amount = 0

with open(name_of_file, 'r') as file:
    lines = file.readlines()
    for line in lines:
        amount += int(line)
    print("Общая сумма у нас состоявляет", amount)
    print("Среднее у нас получается: ", amount/len(lines))
