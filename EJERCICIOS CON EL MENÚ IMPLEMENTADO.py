def menu():
    print("")
    print("---------------------------------------=== MENU PRINCIPAL ===---------------------------------------")
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
    choice = int(input("Elige una opcion (1-20). Para salir (0): "))
    print("")
    return choice

"""------------------------- POO --------------------------"""

def ejercicio_persona():
    print("\n--- Ejercicio Persona ---")
    class persnona:
        def __init__(self, nombre, apellido, edad, estadoCivil, numeroDocumentoIdentidad):
            self.nombre = nombre
            self.apellido = apellido
            self.edad = edad
            self.estadoCivil = estadoCivil
            self.numeroDocumentoIdentidad = numeroDocumentoIdentidad

        def obtener_nombre(self):
            return self.nombre

        def establecer_nombre(self, nombre):
            self.nombre = nombre
        
        def obtener_apellido(self):
            return self.apellido

        def establecer_apellido(self, apellido):
            self.apellido = apellido

        def obtener_edad(self):
            return self.edad

        def establecer_edad(self, edad):
            self.edad = edad

        def obtener_estadoCivil(self):
            return  self.estadoCivil

        def establecer_estadoCivil(self, estadoCivil):
            self.estadoCivil = estadoCivil
            
        def obtener_numeroDocumentoIdentidad(self):
            return self.numeroDocumentoIdentidad
        
        def establecer_numeroDocumentoIdentidad(self, numeroDocumentoIdentidad):
            self.numeroDocumentoIdentidad = numeroDocumentoIdentidad
        
    persona1 = persnona("Harry", "Potter", 17, False, 203471235)
    print(f"la edad de {persona1.nombre} es {persona1.obtener_edad()}")

    persona2 = persnona("Hermione", "Granger", 17, False, 203896545)
    print(f"el estado civil de {persona2.nombre} es: {persona2.estadoCivil}")

    persona3 = persnona("Ron", "Weasly", 0, False, 203964235)
    persona3.establecer_edad(45)
    print(f"el senior {persona3.apellido} tiene {persona3.obtener_edad()} anios")

    persona4 = persnona("Albus", "", 68, False, 203101255)
    persona4.establecer_apellido("Dumbledore")
    print(f"el apellido del senior {persona4.nombre} es {persona4.obtener_apellido()}")

    persona5 = persnona("Sirius", "Black", 45, False, 203785235)
    print(f"la identificacion del senior {persona5.apellido} es: {persona5.obtener_numeroDocumentoIdentidad()}")

    persona6 = persnona("Draco", "Malfoy", 17, False, 0)
    persona6.establecer_numeroDocumentoIdentidad(203366575)
    print(f"la nueva identificacion del senior {persona6.nombre} es {persona6.obtener_numeroDocumentoIdentidad()}")

    persona7 = persnona("Bellatrix ", "Lestrange", 49, False, 203894225)
    persona7.establecer_estadoCivil(True)
    print(f"la seniorita {persona7.nombre} es casada: {persona7.obtener_estadoCivil()}")
    print("")

def ejecicio_cuenta():
    print("\n--- Ejercicio Cuenta ---")

    class Cuenta:
        def __init__(self, saldo):
            self.saldo = saldo
                
        def ingresar(self, monto):
            if monto > 0:
                self.saldo += monto
                print(f"ingreso realizado. Nuevo saldo es: {self.saldo}")
            else:
                print(f"el monto debe ser positivo para realizar el ingreso")
        
        def reintegro(self, monto):
            if monto > 0 and monto <= self.saldo:
                self.saldo -= monto
                print(f"reintegro realizado. Nuevo saldo es: {self.saldo}")
            else:
                print(f"el monto es invalido para realizar el reintegro")
        
        def transferecias(self, otra_cuenta, monto):
            if monto > 0 and monto <= self.saldo:
                self.saldo -= monto
                otra_cuenta.ingresar(monto)
                print(f"transferencia realizada. Nuevo saldo: {self.saldo}")
            else:
                print("el monto es inválido para realizar la transferencia.")

        def mostrar(self):
            print(f"saldo actual: {self.saldo}")   

    cuenta1 = Cuenta(100)
    cuenta2 = Cuenta(50) 

    while True:
        print(
            "\n--- Menu de Cuenta ---"
            "\n1. Ingresar Dinero"
            "\n2. Reintegro de Dinero"
            "\n3. Transferencias Bancarias"
            "\n4. Mostrar Saldo"
            "\n5. Salir"
        )
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                monto = float(input("Digite la cantidad a ingresar: "))
                print("")
                cuenta1.ingresar(monto)
                input("\nPresiona Enter para volver al menu de cuenta...")
            except ValueError:
                print("Ingrese un número válido.")
        
        elif opcion == "2":
            try:
                monto = float(input("Digite la cantidad a retirar: "))
                print("")
                cuenta1.reintegro(monto)
                input("\nPresiona Enter para volver al menu de cuenta...")
            except ValueError:
                print("Ingrese un número válido.")

        elif opcion == "3":
            try:
                monto = float(input("Ingrese la cantidad a transferir: "))
                print("")
                cuenta1.transferencias(cuenta2, monto)
                input("\nPresiona Enter para volver al menu de cuenta...")
            except ValueError:
                print("Ingrese un número válido.")
        
        elif opcion == "4":
            print("")
            cuenta1.mostrar()
            input("\nPresiona Enter para volver al menu de cuenta...")

        elif opcion == "5":
            print("Saliendo del menú de cuenta.")
            break

        else:
            print("Digite un número válido.")

def ejercicio_fraccion():
    print("\n--- Ejercicio Fraccion ---")
    print("")

    from math import gcd 

    class Fraccion:
        def __init__(self, numerador, denominador):
            if denominador == 0:
                raise ValueError("el denominador no debe estar en cero")
            self.numerador = numerador
            self.denominador = denominador
            self.simplificar()
        
        def simplificar(self):
            divisor_comun = gcd(self.numerador, self.denominador)
            self.numerador //= divisor_comun
            self.denominador //= divisor_comun

        def suma(self, otra):
            nuevo_numerador = (self.numerador * otra.denominador) + (otra.denominador * self.numerador) 
            nuevo_denominador = self.denominador * self.denominador
            resultado = Fraccion(nuevo_numerador, nuevo_denominador)
            resultado.simplificar()
            return resultado 

        def restar(self, otra):
            nuevo_numerador = (self.numerador * otra.denominador) - (otra.denominador * self.numerador) 
            nuevo_denominador = self.denominador * self.denominador
            resultado = Fraccion(nuevo_numerador, nuevo_denominador)
            resultado.simplificar()
            return resultado 

        def multiplicar(self, otra):
            nuevo_numerador = self.numerador * otra.numerador  
            nuevo_denominador = self.denominador * otra.denominador
            resultado = Fraccion(nuevo_numerador, nuevo_denominador)
            resultado.simplificar()
            return resultado 
        
        def dividir(self, otra):
            nuevo_numerador = self.numerador * otra.denominador  
            nuevo_denominador = self.denominador * otra.numerador
            resultado = Fraccion(nuevo_numerador, nuevo_denominador)
            resultado.simplificar()
            return resultado 
        
        def __str__(self):
            return f"{self.numerador} / {self.denominador}"
        
    numerador1 = int(input("ingrese el numerador de la primera fraccion: "))
    denominador1 = int(input("ingrese el denominador de la primera fraccion: "))
    Fraccion1 = Fraccion(numerador1, denominador1)
    print("")

    numerador2 = int(input("ingrese el numerador de la segunda fraccion: "))
    denominador2 = int(input("ingrese el denominador de la segunda fraccion: "))
    Fraccion2 = Fraccion(numerador2, denominador2)
    print("")

    print(f"{numerador1} / {denominador1}")
    print(f"{numerador2} / {denominador2}")
    print("")

    suma = Fraccion1.suma(Fraccion2)
    print(f"Suma: {suma}")
    print("")

    resta = Fraccion1.restar(Fraccion2)
    print(f"resta: {resta}")
    print("")

    multiplicar = Fraccion1.multiplicar(Fraccion2)
    print(f"multiplicar: {multiplicar}")
    print("")

    dividir = Fraccion1.dividir(Fraccion2)
    print(f"dividir: {dividir}")
    print("")

def ejercicio_complejo():
    print("\n--- Ejercicio Complejo ---")
    print("")

    class Complejo:

        def __init__(self, real, imaginario):
            self.real = real
            self.imaginario = imaginario
            
        def __str__(self):
            signo = "+" if self.imaginario >= 0 else "-"
            return f"{self.real} {signo} {abs(self.imaginario)}i"
        
        def suma(self, otro):
            real = self.real + otro.real
            imaginario = self.imaginario + otro.imaginario
            return Complejo(real, imaginario)

        def resta(self, otro):
            real = self.real - otro.real
            imaginario = self.imaginario - otro.imaginario
            return Complejo(real, imaginario)

        def multiplicar(self, otro):
            real = self.real * otro.real - self.imaginario * otro.imaginario
            imaginario = self.real * otro.imaginario + self.imaginario * otro.real
            return Complejo(real, imaginario)

        def dividir(self, otro):
            if otro.real == 0 and otro.imaginario == 0:
                raise ValueError("No se puede dividir por cero")
            divisor = otro.real**2 + otro.imaginario**2
            real = (self.real * otro.real + self.imaginario * otro.imaginario) / divisor
            imaginario = (self.imaginario * otro.real - self.real * otro.imaginario) / divisor
            return Complejo(real, imaginario)
        
    real1 = float(input("ingrese la parte real del primer numero complejo: "))
    imag1 = float(input("ingrese la parte imaginaria del primer número complejo: "))
    print("")

    real2 = float(input("ingrese la parte real del segundo numero complejo: "))
    imag2 = float(input("ingrese la parte imaginaria del segundo numero complejo: "))

    complejo1 = Complejo(real1, imag1)
    complejo2 = Complejo(real2, imag2)

    print("\nResultados de operaciones entre números complejos:")
    print(f"{complejo1} + {complejo2} = {complejo1.suma(complejo2)}")
    print(f"{complejo1} - {complejo2} = {complejo1.resta(complejo2)}")
    print(f"{complejo1} * {complejo2} = {complejo1.multiplicar(complejo2)}")
    try:
        print(f"{complejo1} / {complejo2} = {complejo1.dividir(complejo2)}")
    except ValueError as e:
        print(e)

def cliente_banco():
    print("\n--- Cliente y Banco  ---")
    print("")

    class Cliente:
        def __init__(self, nombre, cantidad_inicial):
            self.nombre = nombre
            self.cantidad = cantidad_inicial

        def depositar(self, monto):
            if monto > 0:
                self.cantidad += monto
                print(f"{self.nombre} deposito {monto}. Saldo actual: {self.cantidad}")
            else:
                print("El monto debe ser positivo para depositar")

        def extraer(self, monto):
            if 0 < monto <= self.cantidad:
                self.cantidad -= monto
                print(f"{self.nombre} retiro {monto}. Saldo actual: {self.cantidad}")
            else:
                print("El monto es invalido o insuficiente para retirar.")

        def mostrar_total(self):
            print(f"{self.nombre} tiene un saldo de: {self.cantidad}")
            return self.cantidad


    class Banco:
        def __init__(self):
            self.clientes = [
                Cliente("Cliente 1", 1000),
                Cliente("Cliente 2", 1500),
                Cliente("Cliente 3", 2000)
            ]

        def operar(self):
            self.clientes[0].depositar(500)
            self.clientes[1].extraer(300)
            self.clientes[2].depositar(1000)

        def deposito_total(self):
            total = sum(cliente.mostrar_total() for cliente in self.clientes)
            print(f"Deposito total en el banco: {total}")

    banco = Banco()
    banco.operar()        
    banco.deposito_total() 

def clase_cuenta():
    print("\n--- Clases Cuenta, Plazo Fijo y Caja Ahorro ---")
    print("")

    class Cuenta:
        def __init__(self, titular, cantidad):
            self.titular = titular
            self.cantidad = cantidad

        def imprimir_datos(self):
            print(f"Titular: {self.titular}")
            print(f"Cantidad: {self.cantidad}")


    class CajaAhorro(Cuenta):
        def __init__(self, titular, cantidad):
            super().__init__(titular, cantidad)

        def mostrar_informacion(self):
            print("\n--- Información de Caja de Ahorro ---")
            self.imprimir_datos()


    class PlazoFijo(Cuenta):
        def __init__(self, titular, cantidad, plazo, interes):
            super().__init__(titular, cantidad)
            self.plazo = plazo
            self.interes = interes

        def calcular_importe_interes(self):
            return self.cantidad * self.interes / 100

        def mostrar_informacion(self):
            print("\n--- Información de Plazo Fijo ---")
            self.imprimir_datos()
            print(f"Plazo: {self.plazo} meses")
            print(f"Interés: {self.interes}%")
            print(f"Total de interés: {self.calcular_importe_interes()}")

    caja_ahorro = CajaAhorro("Ana Perez", 1500)
    plazo_fijo = PlazoFijo("Juan Gomez", 2000, 12, 5)


    caja_ahorro.mostrar_informacion()
    plazo_fijo.mostrar_informacion()
    
    """------------------------- CICLO WHILE --------------------------"""

def notas_alumnos():
    print("\n--- Notas Alumnos ---")
    print("")

    contador = 1
    aprobados = 0
    reprobados = 0


    while contador <= 10:
        print(f'\nIngrese las notas del estudiante {contador}:')

        
        nota_1 = int(input('Ingrese la primera nota: '))
        nota_2 = int(input('Ingrese la segunda nota: '))
        nota_3 = int(input('Ingrese la tercera nota: '))
        nota_4 = int(input('Ingrese la cuarta nota: '))


        promedio = (nota_1 + nota_2 + nota_3 + nota_4) / 4
        print(f'El promedio del estudiante {contador} es de {promedio}')


        if promedio >= 90:
            print('El promedio fue excelente')
            aprobados += 1
        elif promedio >= 80:
            print('El promedio fue bueno')
            aprobados += 1
        elif promedio >= 70:
            print('El promedio es más o menos')
            aprobados += 1
        else:
            print('Reprobado')
            reprobados += 1

        contador += 1

    print(f'\nTotal de estudiantes aprobados: {aprobados}')
    print(f'Total de estudiantes reprobados: {reprobados}')    

def sueldo_empleados():
    print("\n--- Sueldos de Empleados ---")
    print("")


    gana = 0
    meno = 0
    contador = 1
    total_sueldos = 0

    while contador <= 5:
        n = int(input(f'Ingrese el sueldo del empleado {contador}: '))

        if 100 <= n <= 1000:
            if n >= 500:
                print('Ganas más de 500')
                gana += 1
            else:
                print('Ganas menos de 500')
                meno += 1

            total_sueldos += n
            contador += 1 
        else:
            print('El sueldo que ingresó no está entre el rango de 100 y 1000. Intente de nuevo.')

    print(f'\nEl total de empleados que ganan más de 500 son: {gana}')
    print(f'El total de empleados que ganan menos de 500 son: {meno}')
    print(f'El sueldo total que gasta la empresa es de: {total_sueldos}')


def aprobado_suspendido_alumno():
    print("\n--- Aprobados y Suspendidos de Alumnos ---")
    print("")

    contador = 1
    aprobados = 0
    reprobados = 0


    while contador <= 10:
        print(f'\nIngrese las notas del estudiante {contador}:')

        
        nota_1 = int(input('Ingrese la primera nota: '))
        nota_2 = int(input('Ingrese la segunda nota: '))
        nota_3 = int(input('Ingrese la tercera nota: '))
        nota_4 = int(input('Ingrese la cuarta nota: '))


        promedio = (nota_1 + nota_2 + nota_3 + nota_4) / 4
        print(f'El promedio del estudiante {contador} es de {promedio}')


        if promedio >= 90:
            print('El promedio fue excelente')
            aprobados += 1
        elif promedio >= 80:
            print('El promedio fue bueno')
            aprobados += 1
        elif promedio >= 70:
            print('El promedio es más o menos')
            aprobados += 1
        else:
            print('Reprobado')
            reprobados += 1

        contador += 1

    print(f'\nTotal de estudiantes aprobados: {aprobados}')
    print(f'Total de estudiantes reprobados: {reprobados}')    

"""------------------------- CICLO FOR --------------------------"""

def suma_numeros():
    print("\n--- Suma de Últimos 5 Números ---")
    print("")

    suma_ultimos_5 = 0

    for i in range(1, 11):
        numero = int(input(f'Ingrese el valor {i}: '))

        if i > 5:
            suma_ultimos_5 += numero

    print(f'La suma de los últimos 5 valores ingresados es: {suma_ultimos_5}')
    
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



# Realizar un programa que lea los lados de n triángulos. Informar después de cada
# triángulo si es equilátero (tres lados iguales), isósceles (dos lados iguales) o
# escaleno (ningún lado igual). Informar después del total de triángulos de cada tipo.

def clasificar_triangulo(lado1, lado2, lado3):
    if lado1 == lado2 == lado3:
        return "equilátero"
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        return "isósceles"
    else:
        return "escaleno"
 
# Función principal
def principal():
    print("\n--- Clasificación de Triángulos ---")
   
    # Número de triángulos
    n = int(input("Ingrese la cantidad de triángulos a clasificar: "))
   
    # Contadores para cada tipo de triángulo
    equilateros = 0
    isosceles = 0
    escalenos = 0
 
    # Clasificación
    for i in range(n):
        print(f"\nTriángulo {i + 1}:")
        lado1 = float(input("Ingrese el primer lado: "))
        lado2 = float(input("Ingrese el segundo lado: "))
        lado3 = float(input("Ingrese el tercer lado: "))
 
        # Clasificar el triángulo
        tipo = clasificar_triangulo(lado1, lado2, lado3)
       
        # Imprimir tipo de triángulo
        print(f"El triángulo {i + 1} es {tipo}.")
       
        # Incrementar el contador según el tipo de triángulo
        if tipo == "equilátero":
            equilateros += 1
        elif tipo == "isósceles":
            isosceles += 1
        elif tipo == "escaleno":
            escalenos += 1
 
    # Mostrar el resumen
    print("\nResumen:")
    print(f"Total de triángulos equiláteros: {equilateros}")
    print(f"Total de triángulos isósceles: {isosceles}")
    print(f"Total de triángulos escalenos: {escalenos}")


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
            
def positivos_negativos():
    negativos = []  # Lista para números negativos
    positivos = []  # Lista para números positivos y ceros

    while True:
        print("Introduce números enteros uno por uno. Escribe 'fin' para terminar.")
        
        valor_input = input("Introduce un número: ")
        
        # Termina el bucle si el usuario escribe "fin"
        if valor_input.lower() == "fin":
            break
        
        try:
            valor = int(valor_input.strip())  # Convertir la entrada en un entero
            
            # Clasificar el número en negativo o positivo
            if valor < 0:
                negativos.append(valor)  # Agregar a la lista de negativos
            else:
                positivos.append(valor)  # Agregar a la lista de positivos y ceros
        except ValueError:
            # Mensaje de error si no se puede convertir a entero
            print("Por favor, ingresa un número entero válido.")

    # Ordenar ambas listas de menor a mayor
    negativos.sort()  # Ordenar negativos
    positivos.sort()  # Ordenar positivos y ceros

    # Presentar resultados
    print("\nLista de números negativos ordenados de menor a mayor:")
    print(negativos)
    print("Lista de números positivos y ceros ordenados de menor a mayor:")
    print(positivos)
#---------------------------------------------------------------------------------------------

#Realizar un programa que reciba una serie de edades y retorne la cantidad de
#personas con una edad igual o superior a 18 (como mínimo deben introducirse 3
#valores enteros)

def contar_adultos(edades):
    """Cuenta cuántas edades son iguales o mayores a 18."""
    contador = 0
    for edad in edades:
        if edad >= 18:
            contador += 1
    return contador

def ejecutar_adultos():
    """Solicita al usuario que ingrese una serie de edades y cuenta las personas mayores o iguales a 18."""
    edades = []

    # Solicitar al usuario que ingrese edades mayores a cero
    print("Ingrese las edades. Escriba 'fin' para terminar. Debe ingresar al menos 3 edades.")

    while True:
        entrada = input(f"Ingrese la edad #{len(edades) + 1} (o 'fin' para terminar): ")
        
        if entrada.lower() == 'fin':
            if len(edades) < 3:
                print("Se requieren al menos 3 edades. Intente nuevamente.")
                continue
            break

        try:
            edad = int(entrada)  # Convertir la entrada en un entero
            if edad > 0:
                edades.append(edad)
            else:
                print("La edad debe ser mayor a 0.")
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

    # Imprimir la cantidad de personas con edad igual o superior a 18
    cantidad_adultos = contar_adultos(edades)
    print(f"La cantidad de personas con edad igual o superior a 18 es: {cantidad_adultos}")


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

def ejecutar_usuario():

# Bucle para pedir un nombre de usuario hasta que sea válido
    while True:
        nombre = input("Introduce un nombre de usuario: ")
        resultado = validar_usuario(nombre)

        if resultado is True:
            print("Nombre de usuario válido.")
            break  # Salir del bucle si el nombre es válido
        else:
            print(resultado)  # Imprimir el mensaje de error

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


def main():
    while True:
        choice = menu()
        #------------------------- POO --------------------------
        if choice == 1:
            print("")
            ejercicio_persona()
            input("\nPresiona Enter para volver al menú...")

        elif choice == 2:
            print("")
            ejecicio_cuenta()
            input("\nPresiona Enter para volver al menú...")
        
        elif choice == 3:
            print("")
            ejercicio_fraccion()
            input("\nPresiona Enter para volver al menú...")

        elif choice == 4:
            print("")
            ejercicio_complejo()
            input("\nPresiona Enter para volver al menú...")
        
        elif choice == 5:
            print("")
            cliente_banco()
            input("\nPresiona Enter para volver al menú...")

        elif choice == 6:
            print("")
            clase_cuenta()
            input("\nPresiona Enter para volver al menú...")
            
          #------------------------- CICLO WHILE --------------------------
        elif choice == 7:
            print("")
            notas_alumnos()
            input("\nPresiona Enter para volver al menú...")
        
        elif choice == 8:
            print("")
            sueldo_empleados()
            input("\nPresiona Enter para volver al menú...")

        elif choice == 9:
            print("")
            aprobado_suspendido_alumno()
            input("\nPresiona Enter para volver al menú...")
        #------------------------- CICLO FOR --------------------------
        elif choice == 10:
            print("")
            suma_numeros()
            input("\nPresiona Enter para volver al menú...")   
            
        elif choice == 11:
            print("")
            tabla_multiplicar()
            input("\nPresiona Enter para volver al menú...")

        elif choice == 12:
            print("")
            puntos_cuandrantes()
            input("\nPresiona Enter para volver al menú...")

        elif choice == 13:
            print("")
            principal()
            input("\nPresiona Enter para volver al menú...")
        #------------------------- FUNCIONES --------------------------
        elif choice == 14:
            print("")
            cuadrado()
            producto()
            input("\nPresiona Enter para volver al menú...")

        elif choice == 15:
            print("")
            contar_vocales('0')
            contar_vocales('Ronny')
            contar_vocales('ITLA')
            input("\nPresiona Enter para volver al menú...")
        
        elif choice == 16:
            print("")
            positivos_negativos()
            input("\nPresiona Enter para volver al menú...")

        elif choice == 17:
            print("")
            ejecutar_adultos()
            input("\nPresiona Enter para volver al menú...")

        elif choice == 18:
            print("")
            procesar_texto()
            input("\nPresiona Enter para volver al menú...")

        elif choice == 19:
            print("")
            ejecutar_usuario()
            input("\nPresiona Enter para volver al menú...")

        elif choice == 20:
            print("")
            adivinar_numero()
            input("\nPresiona Enter para volver al menú...")
            
        elif choice == 0:
            print("saliendo del programa")
            break
        else:
            print("numero incorrecto")


        

if __name__ == "__main__":
    main()
