lista = list()

def person():
    print('-'*30)
    print(f'{"  NEW REGISTER"}'.center(30))
    print('-'*30)

    lista.append(str(input('Name: ')).capitalize())
    while True:
        try:
            lista.append(int(input('Age: ')))
            break
        except:
            print('Enter a valid age.')


def registro():
    print('-'*30)
    print(f'{"PEOPLE REGISTERED"}'.center(30))
    print('-'*30)

    cont = 0
    for x in lista:
        if cont % 2 == 0:
            print(f'{lista[cont]}', end='')
        else:
            print(f'\t{lista[cont]} Years')
        cont += 1


def menu(num):
    while True:
        print('-'*30)
        print(f'{"  MENU PRINCIPAL"}'.center(30))
        print('-'*30)
    
        print('1 - See registered people\n'
              '2 - Register new person\n'
              '3 - Left to system')
        print('-'*30)
        try:
            ask = int(input(num))
            if 0 < ask <= 3:
                if ask == 1:
                    registro()
                if ask == 2:
                    person()
                if ask == 3:
                    return ask
            else:
                print('Try again, please.')
        except:
            print("Doesn't have any option like this.")