def menu():
    print("")
    print("---------------------------------=== MENU PRINCIPAL -------------------------------------=== ")
    print("")
    print(
    "Ejercicios POO:\n"
        "1. Ejercicio Personas                           | "
        "2. Ejercicio Cuenta\n"
        "3. Ejercicio Fraccion                           | "
        "4. Ejercicio Complejo\n"
        "5. Cliente y Banco                              | "
        "6. Clases Cuenta, Plazo Fijo y Caja Ahorro\n\n"

    "Ciclo While:\n"
        "7. Notas Alumnos                                | "
        "8. Sueldos de Empleados\n"
        "9. Aprobados y Suspendidos de Alumnos\n\n"
    
    "Ciclo For:\n"
        "10. Suma de Últimos 5 Números                   | "
        "11. Tabla de Multiplicar\n"
        "12. Ingreso de Puntos en Cuadrantes             | "
        "13. Clasificación de Triángulos\n\n"
    
    "Funciones:\n"
        "14. Cuadrado y Producto de Números              | "
        "15. Conteo de Vocales en un String\n"
        "16. Separación de Números Positivos y Negativos | "
        "17. Conteo de Personas Mayores de 18 Años\n\n"
    
    "Simples:\n"
        "18. Análisis de String\n\n"
    
    "Otros:\n"
        "19. Validación de Nombres de Usuario            | "
        "20. Adivina el Número"
    )
    print("")
    choice = int(input("Elige una opcion (1-20). Para salir (0): "))    #dejar como entero.
    print("")
    return choice

#Bucle while para mostrar el menú hasta que se ingrese 0 "Para salir", por teclado.
while True:
    
    #Ejercicios de Jheinel:
    # Fin ejercicios de Jheinel
    
    #Ejercicios de jhael:
    # Fin ejercicios de Jhael
    
    #Ejercicios de Ronny:

    # Realizar un programa que solicite la carga de un valor entero del 1 al 10. Mostrar
    # después la tabla de multiplicar de dicho número.
    def tabla_multiplicar():
        print("\n--- Tabla de Multiplicar ---"),
        print("")

        #Pedimos el numero
        num = int(input("Ingresa un valor del 1 al 10: "))

        #Bucle para multiplicar el numero ingresado por la tabla
        if 1 <= num <= 10: #num debe estar entre 1 y 10
            for i in range(1,12):
                print(f"{num} x {i} = {num * i}")
        else:
            print("El número debe estar entre 1 y 10.")

    
    """Esto es lo que hay que hacer para poder llamar al menú y elegir una opcion."""
    ##Llamar a la funcion si elige su opcion
    opcion = menu()     #pregunta "porqué si no instancio la funcion se imprime dos veces el menú, ejemplo si hago if menu() == 11: tabla_multiplicar()
    if opcion == 11:
        tabla_multiplicar()

    # Realizar un programa que pida ingresar dos datos enteros (coordenadas x e y). Al
    # comenzar el programa se pedirá ingresar el total de puntos a procesar. Informar de
    # cuantos puntos se han ingresado en cada uno de los cuatro cuadrantes.

    def puntos_cuandrantes():
        print("\n--- Ingreso de Puntos en Cuadrantes ---\n")

        # Contadores para cada cuadrante y puntos sobre ejes
        cuadrante_1 = 0
        cuadrante_2 = 0
        cuadrante_3 = 0
        cuadrante_4 = 0
        sobre_ejes = 0

        # Pedir al usuario el total de puntos a procesar
        puntos_totales = int(input("Ingresa el total de puntos a procesar: "))

        # Procesar cada punto
        for i in range(puntos_totales):
            coord_x = int(input(f"Ingrese la coordenada x del punto {i + 1}: "))
            coord_y = int(input(f"Ingrese la coordenada y del punto {i + 1}: "))
            
            # Determinar en qué cuadrante se encuentra el punto o si está sobre los ejes
            if coord_x > 0 and coord_y > 0:
                cuadrante_1 += 1
            elif coord_x < 0 and coord_y > 0:
                cuadrante_2 += 1
            elif coord_x < 0 and coord_y < 0:
                cuadrante_3 += 1
            elif coord_x > 0 and coord_y < 0:
                cuadrante_4 += 1
            else:
                sobre_ejes += 1  # Punto está sobre los ejes

        # Resultados
        print(f"\nPuntos en el cuadrante 1: {cuadrante_1}")
        print(f"Puntos en el cuadrante 2: {cuadrante_2}")
        print(f"Puntos en el cuadrante 3: {cuadrante_3}")
        print(f"Puntos en el cuadrante 4: {cuadrante_4}")
        print(f"Puntos sobre los ejes: {sobre_ejes}")

    ##Llamar a la funcion si elige su opcion
    #(No volver a llamar a la funcion menú, solo usar la instancia opcion)
    if opcion == 12:
        puntos_cuandrantes()


    # Realizar un programa que lea los lados de n triángulos. Informar después de cada
    # triángulo si es equilátero (tres lados iguales), isósceles (dos lados iguales) o
    # escaleno (ningún lado igual). Informar después del total de triángulos de cada tipo.

    def clasificion():
        print("\n--- Clasificación de Triángulos ---")
        print("")

    #Clasificacion
    def clasificar_triangulo(lado1, lado2, lado3):
            if lado1 == lado2 == lado3:
                return "equilátero"
            elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
                return "isósceles"
            else:
                return "escaleno"

    # Función principal
    def princip():
        #números de triángulos
        n = int(input("Ingrese la cantidad de triángulos a clasificar: "))
            
        # Contadores para cada tipo de triángulo
        equilateros = 0
        isosceles = 0
        escalenos = 0

        # clasificaciion
        for i in range(n):
            print(f"\nTriángulo {i + 1}:")
            lado1 = float(input("Ingrese el primer lado: "))
            lado2 = float(input("Ingrese el segundo lado: "))
            lado3 = float(input("Ingrese el tercer lado: "))
                
            tipo = clasificar_triangulo(lado1, lado2, lado3)
                
                # Tipo de triangulo
            print(f"El triángulo {i + 1} es {tipo}.")
                
                # Incrementar el contador de cada var
            if tipo == "equilátero":
                    equilateros += 1
            elif tipo == "isósceles":
                    isosceles += 1
            elif tipo == "escaleno":
                escalenos += 1

            # Totales
        print("\nResumen:")
        print(f"Total de triángulos equiláteros: {equilateros}")
        print(f"Total de triángulos isósceles: {isosceles}")
        print(f"Total de triángulos escalenos: {escalenos}")

    ##Llamar a la funcion si elige su opcion
    if opcion == 13:
        clasificion()
        princip()


    # Realizar un programa con dos funciones. La primera debe solicitar la carga de un 
    # valor entero y mostrar el cuadrado de dicho valor. La segunda que solicite la carga 
    # de dos valores y muestre el producto de los mismos. Deberán llamar a estas dos 
    # funciones desde el bloque principal (Fuera de toda función, como en el ejemplo 
    # realizado al principio de este tema).

    def cuadrado_producto_numero():
        print("\n--- Cuadrado y Producto de Números ---")
        print("")

    #Funcion para el primer numero al cuadrado
    def cuadrado():
        num1 = int(input("Ingrese el primer numero: "))
        result_cuadrado = num1**2
        print( f" {num1}^2 = {result_cuadrado}")

    #Funcion para multiplicar los 2 numeros
    def producto():
        num1 = int(input("Ingrese el primer numero: "))
        num2 = int(input("Ingrese el segundo numero: "))
        result_producto = num1 * num2
        print (f"{num1} x {num2} = {result_producto}")

    ##Llamar a la funcion si elige su opcion
    if opcion == 14:
        cuadrado_producto_numero()
        cuadrado()
        producto()

    # Realizar un programa que tenga una función que reciba un string como parámetro.
    # Debe mostrar la cantidad de vocales que tiene dicho string. Se deberá llamar 3
    # veces desde el bloque principal, con 3 strings diferentes.

    def conteo_vocales():
        print("\n--- Conteo de Vocales en un String ---")
        print("")

    def contar_vocales(texto):
        try:
            if not texto.isalpha(): #verificar si hay un numero en el texto
                raise ValueError("El texto no debe contener numeros, ni caracteres especiales.\n")   #forzar manejo de error
                    
            vocales = 'aeiou'
            cant_vocales = sum(1 for letra in texto.lower() if letra in vocales)    #se suma 1 a cant_vocales si en si en texto hay una vocal
            print(f"{texto} tiene {cant_vocales} vocales")
                    
        except ValueError as error:
                print("¡Ha ocurrido un error!: ",error) #imprime el error

    ##Llamar a la funcion si elige su opcion
    if opcion == 15:
        conteo_vocales()
        contar_vocales('0')
        contar_vocales('Ronny')
        contar_vocales('ITLA')
    

#Fin ejercicios de Ronny

#Ejercicios de Ricardo
#Realizar un programa que cargue una lista de n valores enteros. Generar dos listas,
#una con valores negativos y otra con los valores positivos e imprimir ambas listas.

def negativos_positivos(valores):
    negativos = []
    positivos = []
        
    for valor in valores:
        if valor < 0:
            negativos.append(valor)
        elif valor > 0:
            positivos.append(valor)
        
    return negativos, positivos

valores = [-3, 7, 0, 2, -1, 5, -4]  

# Separar y obtener las listas
negativos, positivos = negativos_positivos(valores)
print("Lista de valores negativos:", negativos)
print("Lista de valores positivos:", positivos)

#para llamar al menu y elegir la opcion:
if opcion == 16:
    negativos_positivos()

#---------------------------------------------------------------------------------------------

#Realizar un programa que reciba una serie de edades y retorne la cantidad de
#personas con una edad igual o superior a 18 (como mínimo deben introducirse 3
#valores enteros)

def adultos(edades):
    contador = 0
    for edad in edades:
        if edad >= 18:
            contador += 1
    return contador

# Solicitar al usuario que ingrese al menos 3 edades mayores a cero
edades = []
while len(edades) < 3:
    try:
        edad = int(input(f"Ingrese la edad {len(edades) + 1} (mayor a 0): "))
        if edad > 0:
            edades.append(edad)
        else:
            print("La edad debe ser mayor a 0.")
    except ValueError:
        print("Por favor, ingrese un número entero válido.")

print(f"La cantidad de personas con edad igual o superior a 18 es: {adultos(edades)}")

#para llamar al menu y elegir la opcion:
if opcion == 17:
    adultos()

#-----------------------------------------------------------------------------------------------
#Solicitar la carga por teclado de un string. Mostrar el total de caracteres del string y
#utilizar las funciones explicadas anteriormente (upper, lower y capitalize).

def obtener_total_caracteres(texto):
    return len(texto)

def convertir_mayusculas(texto):
    return texto.upper()

def convertir_minusculas(texto):
    return texto.lower()

def capitalizar_texto(texto):
    return texto.capitalize()

def procesar_texto():
    # Solicita la entrada de un string por teclado
    texto = input("Introduce un texto: ").strip()
    
    # Verifica si el texto está vacío
    if not texto:
        print("El texto ingresado está vacío. Inténtalo de nuevo.")
        return
    
    # Llama a las funciones y muestra los resultados
    print(f"Total de caracteres: {obtener_total_caracteres(texto)}")
    print(f"Texto en mayúsculas: {convertir_mayusculas(texto)}")
    print(f"Texto en minúsculas: {convertir_minusculas(texto)}")
    print(f"Texto capitalizado: {capitalizar_texto(texto)}")

# Ejecuta la función principal
procesar_texto()

#para llamar al menu y elegir la opcion:
if opcion == 18:
    obtener_total_caracteres()
    convertir_mayusculas()
    convertir_minusculas()
    capitalizar_texto()
    procesar_texto()
#-----------------------------------------------------------------------------------------------

"""
Crear un módulo para validación de nombres de usuarios. Dicho módulo, deberá
cumplir con los siguientes criterios de aceptación:
El nombre de usuario debe contener un mínimo de 6 caracteres y un máximo de 12.
El nombre de usuario debe ser alfanumérico.
Nombre de usuario con menos de 6 caracteres, retorna el mensaje "El
nombre de usuario debe contener al menos 6 caracteres".
Nombre de usuario con más de 12 caracteres, retorna el mensaje "El nombre
de usuario no puede contener más de 12 caracteres".
Nombre de usuario con caracteres distintos a los alfanuméricos, retorna el
mensaje "El nombre de usuario puede contener solo letras y números".
Nombre de usuario válido, retorna True.
"""

def validar_usuario(nombre_usuario):
    # Verificar la longitud del nombre de usuario
    if len(nombre_usuario) < 6:
        return "El nombre de usuario debe contener al menos 6 caracteres."
    elif len(nombre_usuario) > 12:
        return "El nombre de usuario no puede contener más de 12 caracteres."
    
    # Verificar si el nombre de usuario es alfanumérico
    if not nombre_usuario.isalnum():
        return "El nombre de usuario puede contener solo letras y números."
    
    # Si todas las validaciones pasan
    return True


# Bucle para pedir un nombre de usuario hasta que sea válido
while True:
    nombre = input("Introduce un nombre de usuario: ")
    resultado = validar_usuario(nombre)

    if resultado is True:
        print("Nombre de usuario válido.")
        break  # Salir del bucle si el nombre es válido
    else:
        print(resultado)  # Imprimir el mensaje de error
        
#para llamar al menu y elegir la opcion:
if opcion == 19:
    validar_usuario()
#-----------------------------------------------------------------

#Escribe un programa que almacene un número y pida al usuario
#adivinarlo.
import random

def adivinar_numero():
    numero_secreto = random.randint(1, 50)
    intentos = 0
    
    print("He elegido un número entre 1 y 50. ¡Intenta adivinarlo!")
    
    while True:
        try:
            intento = int(input("Introduce tu número: "))
            intentos += 1
            
            if intento < numero_secreto:
                print("Demasiado bajo. Intenta de nuevo.")
            elif intento > numero_secreto:
                print("Demasiado alto. Intenta de nuevo.")
            else:
                print(f"¡Felicidades! Adivinaste el número {numero_secreto} en {intentos} intentos.")
                break
        except ValueError:
            print("Por favor, introduce un número válido.")
            
#para llamar al menu y elegir la opcion:
if opcion == 20:
    adivinar_numero()
#-----------------------------------------------------------------

# Fin ejercicios de Ricardo

    #Poner sus los bloques de codigo de sus programas encima de el siguiente bloque de codigo:
    """OJO DEJAR ESTO SIEMPRE AL FINAL DE EL PROGRAMA EN GENERAL"""
    #Con esto cerramos el menú.
    if opcion == 0:
        print("Haz salido del programa.")
        break
