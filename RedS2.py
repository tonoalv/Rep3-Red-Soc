import RedDefs as Red

idioma = Red.obtener_idioma()
if idioma == 2:
    nombre = Red.obtener_nombre()
    print("Hola, ", nombre, ". Bienvenido.")

    if Red.existe_archivo(nombre+".user"):
        (nombre, edad, estatura, genero, nacionalidad, amigos, estado, muro) = Red.leer_usuario(nombre)
    else:
        edad = Red.obtener_edad()
        estatura = Red.obtener_estatura()
        genero = Red.obtener_genero()
        nacionalidad = Red.obtener_nacionalidad()
        amigos = Red.obtener_lista_amigos()
        estado = ""
        muro = []
    print("Muy bien, ", nombre, ". Hemos creado tu perfil con estos datos.")
    Red.mostrar_perfil(nombre, edad, estatura, genero, nacionalidad, amigos)
    Red.mostrar_mensaje(nombre, estado)

    opcion = 1
    while opcion != 0:
        opcion = Red.opcion_menu()
        if opcion == 1:
            mensaje = Red.obtener_mensaje()
            Red.publicar_mensaje(nombre, amigos, mensaje, muro)
        elif opcion == 2:
            Red.mostrar_muro(muro)
        elif opcion == 3:
            Red.mostrar_perfil(nombre, edad, estatura, genero, nacionalidad, amigos)
        elif opcion == 4:
            nombre = Red.obtener_nombre()
            edad = Red.obtener_edad()
            estatura = Red.obtener_estatura()
            genero = Red.obtener_genero()
            nacionalidad = Red.obtener_nacionalidad()
            amigos = Red.obtener_lista_amigos()
            Red.mostrar_perfil(nombre, edad, estatura, genero, nacionalidad, amigos)
        elif opcion == 0:
                print("Has salido exitosamente.")
                Red.escribir_usuario(nombre, edad, estatura, genero, nacionalidad, amigos, estado, muro)
                
    print("Hasta pronto.")
                

else:
    (name, age, height, gender, nationality) = Red.obtain_data()
    print("Ok, ", name, ". We have successfully created your profile.")
    option = 1
    while option != 0:
        option = Red.option_menu()
        if option == 1:
            message = Red.obtain_message()
            Red.show_message(name, None, message)
        elif option == 2:
            message = Red.obtain_message()
            friend_name = input("Write your friend's name: ")
            Red.show_message(name, friend_name, message)
        elif option ==3:
            Red.show_profile(name, age, height, gender, nationality)
        elif option== 4:
            name = Red.obtain_name()
            age = Red.obtain_age()
            height = Red.obtain_height()
            nationality = Red.obtain_nationality()
            gender = Red.obtain_gender
            Red.show_profile(name, age, height, gender, nationality)
        elif option == 0:
            print("You have successfully logged out")
    print("Bye")
