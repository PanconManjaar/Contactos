import os,time
import csv
Contactos=[]
os.system('cls')
def Menu():
    
    while True:
        os.system('cls')
        print("Menú contactos")
        print("1. Agregar contacto")
        print("2. Ver contactos")
        print("3. Exportar archivo CSV")
        print("4. Salir")
        opc=validad_opc()

        if opc==1:
            opción_1()
        elif opc==2:
            opción_2()
        elif opc==3:
            opción_3()
        elif opc==4:
            opción_4()
def opción_1():
    os.system('cls')
    print("AGREGAR CONTACTOS")
    Nombre = validar_nombre()
    Telefono = validar_Telefono()
    Correo = validar_correo()

    Contacto={"Nombre":Nombre,
              "Telefono":Telefono,
              "Correo":Correo,}
    Contactos.append(Contacto)

    print("Contacto agregado!")
    time.sleep(3)
    os.system('cls')
def opción_2():
    os.system('cls')
    if not Contactos:
        print("No hay contactos agregados...")
    else:
        print("LISTA DE CONTACTOS")
        for c in Contactos:
            print(f"Nombre: {c['Nombre']}\nTelefono: {c['Telefono']}\nCorreo: {c['Correo']}")
            print("")
    time.sleep(3)
def opción_3():
    os.system('cls')
    if len(Contactos)==0:
        print("No hay contactos agregados...")
    else:
        nombre_archivo = input("Ingrese nombre del archivo: ")
        try:
            with open (nombre_archivo+".csv","x",newline="") as archivo: 
                Escritor = csv.DictWriter(archivo,["Nombre","Telefono","Correo"])
                Escritor.writerows(Contactos)
        except:
            print("ERROR! El nombre del archivo ya existe")

        print("ARCHIVO GUARDADO!")
        time.sleep(3)
        os.system('cls')
def opción_4():
    os.system('cls')
    print("Cerrando programa...")
    
    exit()
    
def validad_opc():
    try:
        opc=int(input("Ingrese una opción: "))
        if opc in (1,2,3,4):
            return opc
        else:
            print("ERROR! Debe ingresar una de las opciones mostrada!")
    except:
        print("ERROR! Debe ingresar un número entero!")
    time.sleep(3)


def validar_nombre():
    while True:
        nom = input("Ingrese nombre:")
        if len(nom.strip())>=3 and nom.isalpha():
            return nom
        else: 
            print("ERROR! Ingrese un nombre mayor a 3 y sólo letras!")

def validar_Telefono():
    while True:
        try:
            tel = int(input("Ingrese número telefonico: "))
            if len(str(tel))==9 and str(tel)[0]==9:
                return tel
            else: 
                print("ERROR! El telefono debe comenzar con 9 y tener 9 digitos!")
        except:
            print("ERROR! Debe ingresar números enteros!")

def validar_correo():
    while True:
        cor = input("Ingrese correo(Solo @gmail.com):")
        if cor.strip().lower().endswith("@gmail.com") and len(cor.strip())>=13:
            return cor
        else: 
            print("ERROR! Ingrese un correo mayor a 10 y sólo letras!")

