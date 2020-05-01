name_of_file = "otzivi.txt"

negative_words = ['плохой', 'отвратительный', 'ужасный', 'неприятный']

new_words = []

with open(name_of_file) as file:
    lines = file.readlines()
    for line in lines:
        if line.strip() in negative_words:
            print("цензура")
        else:
            print(line)
