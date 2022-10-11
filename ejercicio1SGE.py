


#Tenemos el siguiente registro:
#
#cod_articulo
#nombre
#descripcion
#precio
#
#Tenemos que realizar una aplicación, que realice el mantenimiento de una lista, cada elemento de la lista 
#sera un diccionario del registro anterior.
#
#La aplicación constara de:
#
#Altas
#Bajas
#Modificaciones
#Búsquedas

import code
#from curses.ascii import isdigit
from operator import truediv
from pydoc import describe
from xml.dom import NoModificationAllowedErr



###########################     los metodos que se nos piden    ####################################################

# ALTA


def alta():
    base = {
        "cod_articulo" : "",
        "nombre" : "",
        "descripcion" : "",
        "precio" : ""
    }

    print()
    print("CREACION DE UN ARTICULO")
    print()

    cod = input("introduce el codigo: ")
    nom = input("introduce el nombre: ")
    desc = input("introduce la descripcion: ")
    prec = input("introduce el precio: ")

    if cod.isdigit() and prec.isdigit():
        base.update({"cod_articulo" : cod})
        base.update({"nombre" : nom})
        base.update({"descripcion" : desc})
        base.update({"precio" : prec})

        articulos.append(base)
    else:
        print("no se puede crear el articulo, los campos codigo y precio son numericos")

     




###############################################################################################################################

# BAJA



def baja():

    print()
    print("BAJA DE ARTICULOS")
    print()

    print("Hay un total de " , len(articulos) , " articulos")
    index = input("introduce el indice del articulo en la lista de articulos")
    if index.isdigit():
        index = int(index)
        if index >=0  and index < len(articulos):
            articulos.remove(articulos[index])
        else:
            print("El indice introducido no es valido")
    else:
        print("El indice introducido no es valido")



###############################################################################################################################

#MODIFICACION



def claveModificar()-> str:
    clave = ""
    while True:
        print("las claves a modificar son las siguientes:")
        print("     cod_articulo")
        print("     nombre")
        print("     descripcion")
        print("     precio")
        clave= input("introduce la clave a modificar: ")
        if clave=="cod_articulo" or clave=="nombre" or clave=="descripcion" or clave=="precio" :
            break
        else:
            print("lo introducido no es valido")
    return clave

def valorModificar(clave)-> str:
    valor = input("intoduzca la modificacion: ")
    if clave=="cod_articulo" or clave=="precio" :
        while True:
            if not valor.isdigit():
                print("el valor debe ser numerico: ")
                valor=input("intoduzca la modificacion: ")
            else: 
                return valor
    return valor

def modificacion():

    print()
    print("MODIFICACION DE ARTICULOS")
    print()

    print("Hay un total de " , len(articulos) , " articulos")
    index = input("introduce el indice del articulo en la lista de articulos: ")
    if index.isdigit():
        index = int(index)
        if index >=0  and index < len(articulos):
            clave = claveModificar()
            valor = valorModificar(clave)

            articulos[index].update({clave : valor})
        else:
            print("El indice introducido no es valido")
    else:
        print("El indice introducido no es valido")

###############################################################################################################################

#BUSQUEDA



def busqueda():

    print()
    print("BUSQUEDA DE ARTICULOS A TRAVES DEL CODIGO")
    print()

    codigo=input("introduzca el codigo del articulo:")
    artres = {}

    for i in range (0,len(articulos),+1):
        art = articulos[i]
        if (art.get("cod_articulo")==codigo):
            artres=articulos[i]
            break
        else:
            artres=0
    
    if artres==0:
        print("no se ha encontrado el articulo")
    else:
        print(artres)



###########################     MENU PARA EL USUARIO     #######################################################


def printMenu():
    print()
    print()
    print("MENU PARA EL USUARIO")
    print()
    print("1. ALTA")
    print("2. BAJA")
    print("3. MODIFICACION")
    print("4. BUSQUEDA")
    print("5. SALIR")
    

def seleccionar():
    while True:
        printMenu()
        numuser = input("introduzca el numero de funcion: ")
        if numuser=="1":
            alta()
        elif numuser=="2":
            baja() 
        elif numuser=="3":
            modificacion()
        elif numuser=="4":
            busqueda()
        elif numuser=="5":
            break
        else:
            print("Numero no valido")

articulos=[]
seleccionar()