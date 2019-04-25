import string
import random

#hay que usar string.string.ascii_letters, string.digits y string.punctiation

def randomPasswordGenerator():
    #se crea la longitud que tendrá la contraseña, debe ir de 4 a 16 caracteres
    length = random.randint(4,16)
    password = []
    password2 = []
    password3 = []
    #Esta variable se encarga de definir qué valores de los arreglos de arriba serán seleccionados
    selector = random.sample(range(length), length)
    #Esta variable define el orden de arreglos que usaremos para tomar valores
    order = []
    #contraseña final
    generatedPassword = ""
    #Este ciclo llena los 4 arreglos creados anteriormente
    for x in range(0, length):
        password.append(random.choice(string.ascii_letters))
        password2.append(random.choice(string.digits))
        password3.append(random.choice(string.punctuation))
        order.append(random.randint(1,3))


    for y in range(0,length):
        #aquí se llenan los arreglos, mediante el uso de la variable order y mediante los valores de selector
        if(order[y] == 1):
            generatedPassword = generatedPassword + str(password[selector[y]])

        elif(order[y] == 2):
            generatedPassword = generatedPassword + str(password2[selector[y]])
        elif(order[y] == 3):
            generatedPassword = generatedPassword + str(password3[selector[y]])




    '''
    print(password)
    print(password2)
    print(password3)
    print(length)
    print(selector)
    print(order)
    '''
    print("La contraseña autogenerada es: "+generatedPassword)



randomPasswordGenerator()
