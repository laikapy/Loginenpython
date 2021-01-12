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
        paswordnew = input('Ingresa tu contrasenia nueva: ')
        paswordnew2 = input('Ingresa tu contrasenia de nuevo: ')


    else:
        print('Introduce una opcion correcta')

#       Este es un cambio, solo para probar el gitsoft

##Agregando esto nada mas xD


este es un nuevo cambio, para probar el rm --cached

def inicio():
    print('BIENVENIDO A LOGITEC')
    print('1. Logearse \n 2.Iniciar sesion.')
    desicion = int(input('Antes de comenzar, digite que es lo que quiere realizar: '))
    opciones(desicion)

if __name__ == '__main__':
    inicio()
