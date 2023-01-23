fileName = 'tel.txt'

def writeFile(file_name):
    with open(file_name, 'a') as data:
        data.writelines("Hello world111" + '\n')


def readFile(file_name):
    result = []
    with open(file_name, 'r+') as data:
        for line in data:
            result.append(line.split())
    return result


def findUsers(userList):
    name = 'Ivan,'
    for user in userList:
        if user[1] == name:
            print(user[3])


# writeFile(fileName)
print(type(readFile(fileName)))
print(readFile(fileName))
findUsers(readFile(fileName))
