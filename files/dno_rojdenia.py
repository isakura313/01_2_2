name_of_file = "pi_million_digits.txt"
print("Пришло время узнать, есть ли ваша дата рождения  в трансцидентном  числе  PI")

pi_str = ''
with open(name_of_file) as file:
    lines = file.readlines()
    for line in lines:
        pi_str += line.strip()

birth = input("Введите дату вашего рождения?: ")
if birth in pi_str:
    print("Здорово! Вы в числе ПИ! ")
else:
    print("В числе Пи не рождаются. Им становяться!")
