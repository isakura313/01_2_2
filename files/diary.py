name_of_file = input("Введите название своего дневника")
name_of_file += ".txt"

with open(name_of_file, 'a') as diary:
    content = input("Введите контент для вашего дневника: ")
    content += "\n"
    diary.write(content)