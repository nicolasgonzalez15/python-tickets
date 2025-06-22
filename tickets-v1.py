import random
import os
import json

#----------Función confirmación salida del sistema-----------------
#Confirma si se sale o no del programa o del módulo de altas y lectura de tickets.
#Se ingresa el tipo de acción a confirmar la salida (alta, leer, salir)
#SI o NO
def confirmación(tipo):

    mensaje = ""
    tipo = tipo.lower().strip()

    match tipo:
        case "alta":
            mensaje = "¿Desea generar un nuevo ticket?(SI/NO): "
        case "leer":
            mensaje = "¿Desea leer otro ticket?(SI/NO): "
        case "salir":
            mensaje = "¿Usted desea salir del programa?(SI/NO): "

    confirma = False
    invalido = True

    while invalido:
    
        valor = input(f"{mensaje}")

        #Convierto a minuscula sin espacios
        valor = valor.lower().strip()

        if valor == 'si':
            confirma = True
            invalido = False
        elif valor =='no':
            invalido = False
        else:
            print("\n")
            print("Error. Debe ingresar SI o NO.")
    
    return confirma

#Formato de ticket para que pueda ser legible para el usuario

def formatoTicket(nombre,sector,asunto,mensaje,nroTicket,tipo):

    tipo = tipo.lower().strip()
    match tipo:
        case "alta":
            leyenda = "Se generó el siguiente ticket"
        case "leer":
            leyenda = "Datos del ticket ingresado"
    
    print("\n")
    print("======================================")
    print(f"              {leyenda}              ")
    print("======================================")
    print("\n")
    print(f"Nombre: {nombre}     Ticket Nro: {nroTicket}")
    print(f"Sector: {sector}")
    print(f"Asunto: {asunto}")
    print("\n")
    print(f"Mensaje: {mensaje}")
    print("\n")
    print("            Recordar el número de ticket.           ")

#Formato de ticket para que pueda ser legible para el usuario, ingresando diccionario de cliente

def formatoTicketBeta(diccionarioCliente,tipo):
    
    tipo = tipo.lower().strip()
    match tipo:
        case "alta":
            leyenda = "Se generó el siguiente ticket"
        case "leer":
            leyenda = "Datos del ticket ingresado"

    print("\n")
    print("======================================")
    print(f"              {leyenda}              ")
    print("======================================")
    print("\n")
    print(f"Nombre: {diccionarioCliente['nombre']}     Ticket Nro: {diccionarioCliente['nroTicket']}")
    print(f"Sector: {diccionarioCliente['sector']}")
    print(f"Asunto: {diccionarioCliente['asunto']}")
    print("\n")
    print(f"Mensaje: {diccionarioCliente['mensaje']}")
    print("\n")
    print("            Recordar el número de ticket.           ")


#Ingresa número de ticket y lo devuelve si es válido, sino muestra mensaje de error
def ticketValido():

    nroTicket = 0
    incorrecto = True
    while incorrecto:

        valor = input("Ingrese su número de ticket entre 1000 y 9999: ")
        if valor.isdigit():
            nroTicket = int(valor)
            
            if 1000<= nroTicket <=9999:
                incorrecto = False
            else:
                print("Rango inválido. Ingrese de nuevo los datos.")
        else:
            print("Caracteres inválidos. Ingrese de nuevo los datos.")

    return nroTicket

#Función para generar diccionario con datos ingresados/generados del cliente

def crearDiccionario(nombre,sector,asunto,mensaje,nroTicket):

    diccionarioCliente = {
        'nombre':nombre,
        'sector':sector,
        'asunto':asunto,
        'mensaje':mensaje,
        'nroTicket': nroTicket}
    
    return diccionarioCliente

#Función para guardar diccionario en archivo json con los datos ingresados/generados del cliente
def guardarTicket(diccionario):

    with open("files/tickets.json",'r+',encoding="utf-8") as archivo:
        contenidoJson = json.load(archivo)
        contenidoJson["tickets"].append(diccionario)
        archivo.seek(0)
        json.dump(contenidoJson,archivo,indent=4)
        
        
        #json.dump(diccionario,archivo,indent=4,ensure_ascii=False)

#Función para leer ticket/diccionario en archivo json con los datos ingresados/generados del cliente
def buscarTicket(ticketBuscado):

    with open("files/tickets.json",'r',encoding="utf-8") as archivo:
        #datos_json  = archivo.read()
        datos_json = json.load(archivo)

        listaTickets = datos_json["tickets"]

        ticketEncontrado = None

        for item in listaTickets:
            #print(f"Item {item.get('nroTicket')}")
            if item.get('nroTicket') == ticketBuscado:
                ticketEncontrado = item
                break

        if ticketEncontrado:
            return ticketEncontrado
        else:
            return None


    #print(datos_json["tickets"][0]['nroTicket'])
    



#----------Función alta de ticket en el sistema-----------------
#Genera un nuevo ticket en el sistema
#Ingreso de datos:  nombre - sector - asunto - problema
#Genera número de ticket con random
#Aparece menu que pregunta si quiere crear otro o salir del módulo de altas de tickets
def altaTicket():

    while True:

        print("\n")
        print("Ingrese los datos para generar un nuevo ticket: \n")
        nombre = input("Ingrese su nombre: ")
        sector = input("Ingrese su sector: ")
        asunto = input("Ingrese el asunto: ")
        mensaje = input("Ingrese un mensaje: ")

        nroTicket = random.randrange(1000, 9999) #con esto genero un numero de ticket random

        diccionarioCliente = crearDiccionario(nombre,sector,asunto,mensaje,nroTicket)
        
        formatoTicketBeta(diccionarioCliente,'alta')

        guardarTicket(diccionarioCliente) #Guardo diccionario creado para ticket en un archivo json

        listaDiccionariosClientes.append(diccionarioCliente) #Guardo diccionario creado en lista de diccionarios

        #print(f"Diccionarios clientes:{listaDiccionariosClientes}")

        #formatoTicket(nombre,sector,asunto,mensaje,nroTicket,"alta")

        confirma = confirmación("alta")

        #Si no desea generar otro ticket sale, sino sigue leyendo.
        if not confirma:
            print("Gracias por usar el módulo de alta Vuelva pronto.")
            break

#----------Función leer ticket en el sistema-----------------
#Lee un ticket existente en el sistema
#Ingreso de datos:  nro. de ticket
#Devuelve nombre - sector - asunto - mensaje
#Pregunta si quiere leer otro ticket
def leerTicket():

    while True:

        #Ingresa nro. de ticket y se valida que sea un nro. y esté entre los rangos
        nroTicket = ticketValido()

        #Devuelve el diccionario del ticket encontrado, o None si no se encuentra el nroTicket
        ticketEncontrado= buscarTicket(nroTicket)

        #Si se encuentra, se imprime con formato, sino se indica que no existe el nroTicket
        if ticketEncontrado:
            formatoTicketBeta(ticketEncontrado,"leer")
        #formatoTicket(nombre,sector,asunto,mensaje,nroTicket,"leer")
        else:
            print(f"El nro. de ticket {nroTicket} no existe. Vuelva a buscar.")

        confirma = confirmación("leer")

        #Si no desea leer otro ticket sale, sino sigue leyendo.
        if not confirma:
            print("Gracias por usar el módulo de leer mensajes. Vuelva pronto.")
            break



#----------Main - Programa principal del sistema-----------------
while True:

    listaDiccionariosClientes = [] #Inicializo lista de diccionarios de clientes en vacío

    #-------------
    print("\n")
    print("  Hola, bienvenido al sistema de Tickets.   ")
    print("\n")

    print("1 - Generar un nuevo ticket")
    print("2 - Leer un ticket")
    print("3 - Salir")
    opcion = input("Selecciona: ")

    if opcion.isdigit():
        
        nro = int(opcion)
    
        match nro:
            case 1:
                print("Agregar ticket. ")
                altaTicket()
                print("\n")

            case 2:
                print("Leer ticket.")
                leerTicket()
                print("\n")
            case 3:
                #print("Salir del programa. ")
                print("\n")
                confirma = confirmación("salir")
                if confirma:
                    print("\n")
                    print("Gracias por usar el sistema de tickets. Vuelva pronto. ")
                    break

                """confirmacion = input("Desea salir del programa (SI/NO): ")
                if confirmacion.lower().strip() == 'si':
                    print("Gracias por usar el sistema de tickets. Vuelva pronto. ")
                    break"""

            case _:
                print("\n")
                print("Error. Debe ingresar uno de los valores permitidos. ")
                print("\n")

    else:
        print("\n")
        print("Caracteres inválidos. Ingrese uno de los valores permitidos. ")
        print("\n")


