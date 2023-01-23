fileName = 'tel.txt'

def writeFile(file_name):
    with open(file_name, 'a') as data:
        data.writelines("Hello world111" + '\n')

def readFile(file_name):
    result = []
    with open(file_name, 'r+') as data:
        for line in data:
            result.append(line.split(','))
    return result

def findName(userList):
    name = input('Введите имя, начиная с пробела: ')
    for user in userList:
        if user[1] == name:
            print(user[3])
    else:
        print('Запрашиваемое имя не найдено. Попробуйте ещё раз.')

findName(readFile(fileName))

def newPer(file_name):
    with open(file_name, 'a') as data:
        create = input('Введите ФИО и номер телефона через запятую: ')
        data.writelines(create)

def findTel(userList):
    tel = input('Введите номер телефона, начиная с пробела и "+": ')
    for user in userList:
        if user[3] == tel:
            print(user[0], user[1], user[2])
    else:
        print('Запрашиваемый номер не найден. Создать новый контакт?')
        create = input('Введите "да" или "нет": ')
        if create == 'да':
            print(newPer(fileName))

findTel(readFile(fileName))
