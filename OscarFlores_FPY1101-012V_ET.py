import os
import csv
import random
trabajadores=[
    "Juan Perez","Maria Garcia","Carlos Lopez","Ana Martinez","Pedro Rodriguez","Laura Hernandez","Miguel Sanchez","Isabel Gomez","Francisco Diaz","Elena Fernandez"
]
nomina=[]
sueldos=[]
def clear():
    os.system("cls")
def asignarsueldo():
    for i in trabajadores:
        nombre=i
        sueldo=random.randint(300000,2500000)
        descuentosalud=sueldo*0.07
        descuentoafp=sueldo*0.12
        sueldoliquido=sueldo-descuentoafp-descuentosalud
        cargar={
            "Nombre Empleado": nombre,
            "Sueldo Base": sueldo,
            "Descuento Salud": descuentosalud,
            "Descuento AFP": descuentoafp,
            "Sueldo Liquido": sueldoliquido
        }
        nomina.append(cargar)
        sueldos.append(sueldo)
    print("Sueldos asignados exitosamente!!!")
def cargarcsv():
    try:
        if os.path.exists:
            with open("Archivo.csv",mode="r",newline="") as file:
                nomina.extend(csv.DictReader(file))
    except FileNotFoundError:
        print("Archivo no encontrado, creando uno nuevo...")
def guardarcsv():
    with open("Archivo.csv",mode="w",newline="")as file:
        fieldnames=("Nombre Empleado","Sueldo Base","Descuento Salud","Descuento AFP","Sueldo Liquido")
        writer=csv.DictWriter(file,fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(nomina)
def clasificarsueldo():
    if len(sueldos)>0:
        contador=0
        contador2=0
        contador3=0
        rango1=(f"Sueldos menores a $800.000 total:\nNombre Empleado  Sueldo Base\n")
        rango2=(f"Sueldos entre $800.000 y $2.000.000\nNombre Empleado    Sueldo Base\n")
        rango3=(f"Sueldos mayores a $2.500.000\nNombre Empleado   Sueldo Base\n")
        for i in nomina:
            if int(i["Sueldo Base"])<800000:
                rango1+=(f"{i['Nombre Empleado']}       ${i['Sueldo Base']}\n")
                contador+=1
        for a in nomina:
            if int(a["Sueldo Base"])>=800000<=2000000:
                rango2+=(f"{a['Nombre Empleado']}       ${a['Sueldo Base']}\n")
                contador2+=1
        for b in nomina:
            rango3+=(f"{b['Nombre Empleado']}       ${b['Sueldo Base']}\n")
            contador3+=1
        print(f"{rango1}Total Rango 1: {contador}\n{rango2}Total Rango 2: {contador2}\n{rango3}Total Rango 3: {contador3}")
    else:
        print("Recuerde asignar los sueldos primero...")
        return

def estadisticas():
    if len(sueldos)>0: #en este caso usare el len para control de errores en caso de que utilicen una funcion antes de asignar los sueldos, me parecio mas simple y apropiado bajo el contexto del ejercicio
        menustats=0
        while menustats==0:
            try:
                print("1>Ver sueldo mas alto \n2>Ver sueldo mas bajo \n3>Promedio de Sueldos \n4>Media Geometrica \n5Volver al menu principal")
                response=int(input("Ingrese la opcion deseada: "))
                if response==1:
                    sueldomasalto=max(sueldos)
                    print(f"El sueldo mas alto es: ${sueldomasalto}")
                    menustats=0
                elif response==2:
                    sueldomasbajo=min(sueldos)
                    print(f"El sueldo mas bajo es: ${sueldomasbajo}")
                    menustats=0
                elif response==3:
                    suma=sum(sueldos)
                    cantidad=len(sueldos)
                    prom=suma/cantidad
                    print(f"El promedio de sueldos es : ${prom}")
                    menustats=0
                elif response==4:
                    producto=1
                    for i in sueldos:
                        producto*=i
                    mediag=producto**(1/len(sueldos))
                    print(f"La media geometrica de los sueldos es: %{mediag:.2f}")
                    menustats=0
                elif response==5:
                    clear()
                    print("Volviendo al menu principal...")
                    break
                else:
                    clear()
                    ("Ingrese una opcion valida...")
            except ValueError:
                clear()
                print("Ingrese una opcion valida...")
    else:
        print("Recuerde asignar los sueldos primero...")
        return
def reporte():
    if len(sueldos)>0:
        salida=("Nombre Empleado    Sueldo Base     Descuento Salud     Descuento AFP       Sueldo Liquido\n")
        for i in nomina:
            salida+=(f">{i['Nombre Empleado']}      ${i['Sueldo Base']:.2f}         ${i['Descuento Salud']:.2f}         ${i['Descuento AFP']:.2f}           ${i['Sueldo Liquido']:.2f}\n")
        print(salida)
    else:
        print("Recuerde asignar los sueldos primero...")
        return
def MainMenu():
    cargarcsv()
    menu=0
    clear()
    while menu==0:
            print("1>Asignar Sueldos Aleatorios \n2>Clasificar Sueldos \n3>Ver Estadisticas \n4>Reporte de Sueldos \n5>Guardar y Salir del programa\n")
            respuesta=(input("Ingrese la opcion que desea realizar: "))
            if respuesta=="1":
                clear()
                asignarsueldo()
                menu=0
            elif respuesta=="2":
                clear()
                clasificarsueldo()
                print("Clasificar sueldos PENDIENTE")
                menu=0
            elif respuesta=="3":
                clear()
                estadisticas()
            elif respuesta=="4":
                clear()
                reporte()
            elif respuesta=="5":
                clear()
                guardarcsv()
                print("Guardando y finalizando... \nDesarrollado por Oscar Flores \nRut:19.216.338-2")
                menu=5
                break
            else:
                clear()
                print("Ingrese Una opcion valida2")
MainMenu()