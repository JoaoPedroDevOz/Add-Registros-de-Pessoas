def readint(num):
    while True:
        try:
            verify = int(input(num))
        except (ValueError, TypeError):
            print("\033[1;31mThis is not a whole number!\033[m")
            continue
        except (KeyboardInterrupt):
            print("\033[1;31mThe number was not entered!\033[m")
            return 0
        else:
            return verify

def linha(tam=42):
    return '-' * tam

def header(title):
    print(linha())
    print(title.center(42))
    print(linha())

#menu

def menu(lista):
    header('PRINCIPAL MENU')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c+=1
    print(linha())

    #option
    opc = readint('Your Option: ')
    return opc