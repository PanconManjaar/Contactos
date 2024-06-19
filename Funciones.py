import os,time
import csv
Contactos=[]
os.system('cls')
def Menu():
    
    while True:
        print("Menú contactos")
        print("1. Agregar contacto")
        print("2. Ver contactos")
        print("3. Exportar archivo CSV")
        print("4. Salir")
        opc=int(input("Ingrese una opción: "))

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
    Nombre=input("Ingrese nombre del contacto: ")
    Telefono=int(input("Ingrese número de telefono: "))
    Correo=input("Ingrese correo electronico: ")

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
        with open (nombre_archivo+".csv","w") as archivo: 
            pass

def opción_4():
    os.system('cls')
    print("Cerrando programa...")
    
    exit()
    
