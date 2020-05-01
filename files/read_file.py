# file = open('auth1.txt')
# content = file.read()
# print(content)

with open('auth.txt') as file:
    content = file.read()
    print(content.strip())