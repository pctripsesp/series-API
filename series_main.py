import os
import requests
import ast

SERIES = []
URL_PASTEBIN = 'https://pastebin.com/raw/xFJTbn9T'
VERSION = "1.0"

#Creamos la funcion cls para limpiar consola, en funcion de la consola utilizada (en caso de Linux "posix")
def cls():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == ("ce", "nt", "dos"):
        os.system ("cls")

def print_cabecera():
    print("*******************************")
    print("** BIENVENIDO A SERIES FACIL **")
    print("** by @pctripsesp            **")
    print("** VERSION "+VERSION+"               **")
    print("*******************************\n")


def print_menu():
    print("1) Cargar series disponibles")
    print("2) Buscar serie")
    print("0) Salir ")

#get series from pastebin
def get_series():
    response1 = requests.get(URL_PASTEBIN)
    data1 = response1.text
    response = requests.get('https://pastebin.com/raw/'+data1)
    data = response.text
    global SERIES
    SERIES = ast.literal_eval(data)

#MUESTRA SERIES DISPONIBLES
def menu1():
    cls()
    print_cabecera()


def menu2_seleccionSerie(resultados):
    cls()
    print_cabecera()



#BUSCA SERIE
def menu2():
    cls()
    print_cabecera()
    resultados=[]
    while True:
        print("Pulsa 'M' para volver al MENU")
        busqueda = input("Introduce el nombre de la serie a buscar\n")
        cls()
        print_cabecera()
        resultados=[]
        if busqueda == "M" or busqueda=="m":
            main()
        else:
            for serie in SERIES:
                if serie[0].__contains__(busqueda):
                    resultados.append(serie)

            #Comprobamos si hay demasiados match
            if len(resultados)>10:
                print("Debe mejorar la busqueda, demasiados resultados")

            else:
                if len(resultados) > 0:
                    print("Pulse 'M' para volver al MENU")
                    print("RESULTADOS ENCONTRADOS -->",len(resultados))
                    n = 1
                    for resultado in resultados:
                        print(str(n)+") "+resultado[0])
                        n+=1

                    while True:
                        try:
                            seleccion_serie = input()
                            if seleccion_serie == 'M' or seleccion_serie == 'm':
                                return main()
                            seleccion_serie = int(seleccion_serie)

                        except:
                            cls()
                            print_cabecera()
                            print("Introduzca un numero")
                            print("RESULTADOS ENCONTRADOS -->",len(resultados))
                            n = 1
                            for resultado in resultados:
                                print(str(n)+") "+resultado[0])
                                n+=1
                            continue

                        if (int(seleccion_serie) in range(len(resultados)+1)) and (int(seleccion_serie != 0)):

                            return verSerie(resultados[seleccion_serie-1])


                else:
                    print("\nNo se han encontrado coincidencias con", busqueda)


def verSerie(seleccion_serie):
    cls()
    print_cabecera()
    print("Pulse 'M' para volver al MENU")
    print("--> Ha escogido", seleccion_serie[0])
    cargar_serie = requests.get('https://pastebin.com/raw/'+seleccion_serie[1])
    cargar_serie_response = cargar_serie.text
    serieCargada = ast.literal_eval(cargar_serie_response)
    print("--------------------------")
    print("- TEMPORADAS DISPONIBLES -")
    print("--------------------------")
    n = 0
    for temporada in serieCargada:
        print(str(n)+") "+temporada[0])
        n+=1

    while True:
        try:
            seleccion_temporada = input()
            if seleccion_temporada == 'M' or seleccion_serie == 'm':
                return main()
            seleccion_temporada = int(seleccion_temporada)

        #No introduce un numero
        except:
            cls()
            print_cabecera()
            print("Pulse 'M' para volver al MENU")
            print("--------------------------")
            print("- TEMPORADAS DISPONIBLES -")
            print("--------------------------")
            print("Introduzca un numero")
            n = 0
            for temporada in serieCargada:
                print(str(n)+") "+temporada[0])
                n+=1
            continue

        if int(seleccion_temporada) in range(len(serieCargada)):
            while True:
                try:
                    print("La"+serieCargada[seleccion_temporada][0]+"tiene "+str(len(serieCargada[seleccion_temporada])-1)+" capitulos")
                    sel_capitulo = input("¿Que capitulo quieres ver?\n")
                    if sel_capitulo == 'M' or seleccion_serie == 'm':
                        return main()
                    sel_capitulo = int(sel_capitulo)

                except:
                    cls()
                    print_cabecera()
                    print("Pulse 'M' para volver al MENU")
                    print("La"+serieCargada[seleccion_temporada][0]+"tiene "+str(len(serieCargada[seleccion_temporada])-1)+" capitulos")
                    print("Introduzca un numero")
                    continue

                if (sel_capitulo > 0) and (sel_capitulo in range(len(serieCargada[seleccion_temporada]))):
                    print(sel_capitulo)
                    #return

                #No escoge un capitulo posible
                else:
                    cls()
                    print_cabecera()
                    print("Pulse 'M' para volver al MENU")
                    print("La"+serieCargada[seleccion_temporada][0]+"tiene "+str(len(serieCargada[seleccion_temporada])-1)+" capitulos")
                    print("Introduzca un numero")
                    continue

        #No escoge una temporada posible
        else:
            cls()
            print_cabecera()
            print("Pulse 'M' para volver al MENU")
            print("--------------------------")
            print("- TEMPORADAS DISPONIBLES -")
            print("--------------------------")
            print("Introduzca un numero")
            n = 0
            for temporada in serieCargada:
                print(str(n)+") "+temporada[0])
                n+=1
            continue

    #idioma_escogido = input ("Seleccione un idioma")



def main():
    cls()
    print_cabecera()
    buscar_actualizaciones()
    get_series()
    print("En total hay", len(SERIES),"series disponibles")
    print_menu()


    while True:
        choice = input()

        if choice=="1":
            return print("1")

        if choice=="2":
            return menu2()

        if choice=="0":
            print("Saliendo")
            break

        else:
            cls()
            print_cabecera()
            print_menu()


#Busca si es la ultima version del script
def buscar_actualizaciones():

    lastVersion = requests.get("https://pastebin.com/raw/8BdD3FsL")
    lastVersionResponse = lastVersion.text
    if lastVersionResponse != VERSION:
        print("HAY UNA NUEVA VERSION DE ESTE SCRIPT")
        r = input("¿QUIERES ACTUALIZARLA? --> Pulsa 'S' o 'N'\n")

        if r == "s" or r == "S":
            currentDirectory = os.path.dirname(os.path.abspath(__file__))
            getLastVersion = requests.get("https://pastebin.com/raw/1v0J4nzZ")
            getLastVersionResponse = getLastVersion.text
            f = open(currentDirectory+"/series_facil.py","w")
            f.write(getLastVersionResponse)
            f.close()
            print("Por favor, ejecute la nueva version")
            exit()


main()
