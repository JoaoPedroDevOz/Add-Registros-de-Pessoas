from Exercices.Exmodulos.ex115pacote.lib.interface import *

def archExist(name):
    try:
        op = open(name, 'rt')
        op.close()
    except FileNotFoundError:
        return False
    else:
        return True

def createarch(name):
    try:
        op = open(name, 'wt+')
        op.close()
    except:
        print('There was an error creating file!')
    else:
        print(f'Archive {name} was created successfully')

def readarch(name):
    try:
        op = open(name, 'rt')
    except:
        print('ERROR to read the file!')
    else:
        header('REGISTERED PEOPLE')
        for linha in op:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} years')
    finally:
        op.close()

def register(arq, name='unknown', age=0):
    try:
        op = open(arq, 'at')
    except:
        print('There was an error opening the file!')
    else:
        try:
            op.write(f'{name}; {age}\n')
        except:
            print('There was an error to write the data!')
        else:
            print(f'Add a new register {name}')
            op.close()
