name_of_file = "pi_million_digits.txt"
print("Программа по получению числа пи")
accur = input("Введите до какого числа вам требуется точность")

pi_str = ''
with open(name_of_file) as file:
    lines = file.readlines()
    for line in lines:
        pi_str += line.strip()

print(pi_str[:int(accur)])

