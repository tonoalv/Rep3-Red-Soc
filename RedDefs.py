import os

def existe_archivo(ruta):
    return os.path.isfile(ruta)

def obtener_nombre():
    nombre = input("Hola, bienvenido. ¿Cómo te llamas?")
    return nombre

def obtener_edad():
    edad = int(input("¿En que año naciste?"))
    return 2020 - edad

def obtener_estatura():
    estatura = float(input("¿Cuanto mides? (En metros)"))
    return estatura

def obtener_lista_amigos():
    linea = input("Escribe una lista con los nombres de tus amigos, separados por una ',': ")
    amigos = linea.split(",")
    return amigos

def mostrar_perfil (nombre, edad, estatura, genero, nacionalidad, amigos):
    print("---------------------------------")
    print("Nombre: ", nombre)
    print("Edad: ", edad, "años")
    print("Estatura: ", estatura, "m")
    print("Genero: ", genero)
    print("Nacionalidad: ", nacionalidad)
    print("Amigos: ", len(amigos))
    print("---------------------------------")

def obtener_genero ():
    genero = input("Selecciona tu género H/M")
    return genero

def obtener_nacionalidad ():
    nacionalidad = input("Escribe tu nacionalidad")
    return nacionalidad

def obtener_datos():
    n = obtener_nombre()
    e = obtener_edad()
    es = obtener_estatura()
    g = obtener_genero()
    na = obtener_nacionalidad()
    return(n, e, es, g, na)

def obtain_data():
    nam = obtain_name()
    a = obtain_age()
    h = obtain_height()
    ge = obtain_gender()
    nat = obtain_nationality()
    return(nam, a, h, ge, nat)

def opcion_menu ():
    print("Acciones disponibles")
    print("  1. Publicar estado")
    print("  2. Timeline")
    print("  3. Mostrar datos de perfil")
    print("  4. Actualizar datos del perfil")
    print("  0. Salir")
    opcion = int(input("Selecciona una opción del menu"))
    while opcion < 0 or opcion > 5:
        print("Respuesta invalida. Intenta de nuevo")
        opcion = int(input("Selecciona una opcion del menu"))
    return opcion

def obtener_mensaje():
    mensaje = input("Escribe un mensaje")
    return mensaje

def mostrar_mensaje(origen, mensaje):
    print("---------------------------------")
    print(origen+": ", mensaje)
    print("---------------------------------")

def mostrar_muro(muro):
    print("----------------------------------------")
    print("              TIMELINE                  ")
    print("                          ("+str(len(muro))+" mensajes)   ")
    for mensaje in muro:
        print(mensaje)
    print("----------------------------------------")

def publicar_mensaje(origen, amigos, mensaje, muro):
    print("-------------------------------------------")
    print(origen, "dice: ", mensaje)
    print("-------------------------------------------")
    muro.append(mensaje)
    for amigo in amigos:
        if existe_archivo(amigo+".user"):
            archivo = open(amigo+".user", "a")
            archivo.write(origen+": "+mensaje+"\n")
            archivo.close()
        

def mensaje_salida():
    salida = print("¿Estás seguro que deseas salir?")
    opciones_salida = int(input("1Si   2No"))
    while opciones_salida < 1 or opciones_salida > 2:
        print("Intenta de nuevo")
        opciones_salida = int(input("1Si   2No"))
    return opciones_salida

def leer_usuario(nombre):
    archivo_usuario = open(nombre+".user", "r")
    nombre = archivo_usuario.readline().rstrip()
    edad = archivo_usuario.readline()
    estatura = archivo_usuario.readline()
    genero = archivo_usuario.readline().rstrip()
    nacionalidad = archivo_usuario.readline().rstrip()
    amigos = archivo_usuario.readline().rstrip().split(",")
    estado = archivo_usuario.readline().rstrip()
    muro = []
    mensaje = archivo_usuario.readline().rstrip()
    while mensaje != "":
        muro.append(mensaje)
        mensaje = archivo_usuario.readline().rstrip
    archivo_usuario.close()
    return (nombre, edad, estatura, genero, nacionalidad, amigos, estado, muro)

def escribir_usuario(nombre, edad, estatura, genero, nacionalidad, amigos, estado, muro):
    archivo_usuario = open(nombre+".user", "w")
    archivo_usuario.write(nombre+"\n")
    archivo_usuario.write(str(edad)+"\n")
    archivo_usuario.write(str(estatura)+"\n")
    archivo_usuario.write(genero+"\n")
    archivo_usuario.write(nacionalidad+"\n")
    archivo_usuario.write(",".join(amigos)+"\n")
    archivo_usuario.write(estado+"\n")
    for mensaje in muro:
        archivo_usuario.write(mensaje+"\n")
    archivo_usuario.close()
    
                    
def obtener_idioma():
    print("-----------------------------------------")
    print(" 1. English")
    print(" 2. Español")
    print("-----------------------------------------")
    idioma = int(input("Selecciona un idioma   Choose a language"))
    while idioma  < 1 or idioma  > 2:
        print("Try again     Intenta de nuevo")
        idioma = int(input("Selecciona un idioma    Choose a language"))
    return idioma

def obtain_name():
    name = input("Hello. What's your name?")
    return name

def obtain_age():
    age = int(input("What year were you born in?"))
    return 2020 - age

def obtain_height():
    height = float(input("How tall are you? (In meters)"))
    return height

def show_profile (name, age, height, nationality, gender):
    print("------------------------------")
    print("Name:", name)
    print("Age:", age, "years old")
    print("Height:", height, "tall")
    print("Nationality:", nationality)
    print("Gender:", gender)
    print("-----------------------------")

def obtain_gender():
    gender = input("Select your gender  M/F")
    return gender

def obtain_nationality():
    nationality = input("What's your nationality?")
    return nationality

def option_menu():
    print("-----------------------------")
    print("Actions")
    print(" 1. Post status")
    print(" 2. Write to friends")
    print(" 3. Show profile")
    print(" 4. Update profile")
    print(" 0. Exit")
    option = int(input("Type the number of the action you wish to perform"))
    while option < 0 or option > 4:
        print("Invalid answer. Try again")
        option = int(input("Type the number of the action you wish to perform"))
    return option

def obtain_message():
    message = input("Write a message")
    return message

def show_message(origin, destinatary, message):
    if destinatary == None:
        print(origin, "says", message)
    else:
        print(origin, "says", "@", destinatary, message)
    
