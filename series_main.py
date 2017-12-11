import os
import requests
import ast

SERIES = []
URL_PASTEBIN = 'PRIVATE_URL_DB'

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
    print("*******************************\n")

def print_menu():
    print("1) Cargar series disponibles")
    print("2) Buscar serie")
    print("0) Salir ")

#get series from pastebin
def get_series():
    response = requests.get(URL_PASTEBIN)
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
        busqueda = input("Introduce el nombre de la serie a buscar\n")
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
                    print("RESULTADOS ENCONTRADOS -->",len(resultados))
                    print(resultados)
                    break
                else:
                    print("\nNo se han encontrado coincidencias con", busqueda)



def main():
    cls()
    print_cabecera()
    get_series()
    print("En total hay", len(SERIES),"series disponibles")
    print_menu()


    while True:
        choice = input()

        if choice=="1":
            print("1")
            break

        if choice=="2":
            menu2()
            break

        if choice=="0":
            print("Saliendo")
            exit()

        else:
            cls()
            print_cabecera()
            print_menu()


main()
