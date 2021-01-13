



def opciones(desicion):
    if desicion == 1:
        #inciar sesion
        print('Inicio de sesion')
        login = input('Ingresa tu usuario: ')
        pasword = input('Ingresa tu contrasenia: ')


    elif desicion == 2:
        #registrarse
        print('Bienvenido a el registro.')
        name = input('Ingresa tu nombre completo')
        databasekey = []
        databasekey.append(name)
        print(databasekey)
        paswordnew = input('Ingresa tu contrasenia nueva: ')
        paswordnew2 = input('Ingresa tu contrasenia de nuevo: ')
        databasekey(name)


    else:
        print('Introduce una opcion correcta')


def inicio():
    print('BIENVENIDO A LOGITEC')
    print('1.Iniciar sesion.  \n 2.Logearse')
    desicion = int(input('Antes de comenzar, digite que es lo que quiere realizar: '))
    opciones(desicion)

if __name__ == '__main__':
    inicio()
