from sistemaPacote.lib.archive import *
from sistemaPacote.lib.interface import *
from time import sleep

arq = 'people.txt'

if archExist(arq):
    print()
else:
    createarch(arq)

while True:
    resp = menu(['See registered people', 'Register new person', 'Left the system'])
    if resp == 1:
        #See list about content of ppeople registered
        sleep(0.2)
        readarch(arq)
    elif resp == 2:
        #Register a new person
        sleep(0.2)
        header('NEW REGISTER')
        name = str(input('Name: '))
        age = readint('Age: ')
        register(arq, name, age)
    elif resp == 3:
        #Left the system
        sleep(0.2)
        print('Outing the system... See long!')
        break
    else:
        #Typed the wrong option
        print('Enter a valid option!')
    sleep(1)
