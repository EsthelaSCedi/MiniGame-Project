import random
import time

horca= ['''
   +---+
   |   |
       |
       |
       |
       |
=========''', '''
   +---+
   |   |
   o   |
       |
       |
       |
=========''', '''
   +---+
   |   |
   o   |
   |   |
       |
       |
=========''', '''
   +---+
   |   |
   o   |
  /|   |
       |
       |
=========''', '''
   +---+
   |   |
   o   |
  /|\  |
       |
       |
=========''', '''
   +---+
   |   |
   o   |
  /|\  |
  /    |
       |
=========''', '''
   +---+
   |   |
   o   |
  /|\  |
  / \  |
       |
=========''']

#JUEGO DEL GATO
board=[".",".",".",
       ".",".",".",
       ".",".","."]
juego_sigue=True
ganador=0
turnoxo= "X"
numeros=[1,2,3,4,5,6,7,8,9]
jugador="1"

def tablero():
    print("["+board[0]+" "+board[1]+" "+board[2]+"]")
    print("["+board[3]+" "+board[4]+" "+board[5]+"]")
    print("["+board[6]+" "+board[7]+" "+board[8]+"]")

def gato():
    global turnoxo
    global jugador
    print("\nBIENVENIDO AL JUEGO DEL GATO\n")
    #Desplegar tablero en pantalla
    tablero()
    while juego_sigue==True:
        juego(turnoxo)
        #checar si la partida ya termina 
        checar()
        #cambiar de jugador
        if turnoxo=="X":
            turnoxo="O"
            jugador="2"
        elif turnoxo=="O":
            turnoxo="X"
            jugador="1"
        else:
            print("Error")
        #Ver desenlace
    if ganador!=0:
        if ganador=="X":
            jugador='1'
        elif ganador=="O":
            jugador='2'
        print("El ganador es el jugador "+jugador)
        print("FELICIDADES!!!")
    else:
        print("Empate")
            
def juego(turnoxo):
    global numeros
    print("Turno de jugador "+ jugador)
    #el jugador introduce la posicion del tablero
    posicion=int(input("Elige una posición del 1 al 9: "))
    #En caso de que la posicion no se este disponible en el tablero
    while posicion not in numeros:
        posicion=int(input("Elige una posición del 1 al 9: "))
    posicion=posicion-1
    #En caso de que la posicion ya este ocupada
    if board[posicion]!=".":
        print("La posición ya está ocupada")
        posicion=int(input("Elige una posición del 1 al 9: "))
        posicion=posicion-1
    #Desplegar tablero con posicion marcada
    board[posicion]=turnoxo
    tablero()
    
def checar():
    global juego_sigue
    global ganador
    #ver si ganó por llenar algún renglón
    ganador_r=renglones()
    #ver si ganó por llenar alguna columna
    ganador_c=columnas()
    #ver si ganó por llenar alguna diagonal
    ganador_d=diagonales()
    if ganador_r == True:
        ganador=ganador_r
    elif ganador_c == True:
        ganador=ganador_c
    elif ganador_d==True:
        ganador=ganador_d
    #en caso de empate
    if "."  not in board:
        juego_sigue=False
        ganador=0
  
def renglones():
    global juego_sigue
    global ganador
    #revisa el primer renglón
    r1=board[0]==board[1]==board[2] !="."
    #revisa el segundo renglón
    r2=board[3]==board[4]==board[5] !="."
    #revisa el tercer renglón
    r3=board[6]==board[7]==board[8] !="."
    if (r1 or r2 or r3) == True:
        juego_sigue=False
    if r1==True:
        ganador=(board[0])
        ganador_renglones=True
    elif r2==True:
        ganador=(board[3])
        ganador_renglones=True
    elif r3==True:
        ganador=(board[6])
        ganador_renglones=True
    else:
        return None
    
def columnas():
    global juego_sigue
    global ganador
    #revisa la primera columna
    c1=board[0]==board[3]==board[6] !="."
    #revisa la segunda columna
    c2=board[1]==board[4]==board[7] !="."
    #revisa la tercera columna
    c3=board[2]==board[5]==board[8] !="."
    if (c1 or c2 or c3) == True:
        juego_sigue=False
    if c1==True:
        ganador=(board[0])
        ganador_columnas=True
    elif c2==True:
        ganador=(board[1])
        ganador_columnas=True
    elif c3==True:
        ganador=(board[2])
        ganador_columnas=True
    else:
        return None
    
def diagonales():
    global juego_sigue
    global ganador
    #revisa la primera diagonal
    d1=board[0]==board[4]==board[8] !="."
    #revisa la segunda diagonal
    d2=board[2]==board[4]==board[6] !="."
    if (d1 or d2) == True:
        juego_sigue=False
    if d1==True:
        ganador=(board[0])
    elif d2==True:
        ganador=(board[2])
    else:
        return None

#JUEGO DEL AHORCADO 
def ahorcado():
    #variable para contar las letras correctas
    a=0
    #variable para revisar que la letra no haya sido introducida ya 
    c=0
    print("\nBIENVENIDO AL JUEGO DEL AHORCADO")
    print(horca[0])
    #lista de palabras que se elegirán al azar
    palabras = [ "NARCISOS", "ASTRONAUTA", "PARABRISAS", "PROGRAMA",
             "FACULTAD", "UNIVERSIDAD", "ALABANZA", "LIMPIEZA", "OMBLIGO"]
    palabra = random.choice(palabras)
    print(palabra)
    #variable para medir el largo de la palabra elegida al azar
    b=len(palabra)
    #imprimir los espacios por cada letra que haya en la palabra aleatoria
    for i in (palabra):
        print("_ ",end="")
    #numero de veces que el jugador puede fallar antes de perder
    intentos=6
    #variable en la que se van acumulando las letras que introduce el usuario
    intento=("")
    #errores que lleva el usuario
    error=0
    alfabeto=("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    while intentos>0 and a!=b:
        a=0
        c=0
        error=error
        #el usuario introduce una letra 
        letra=input("\nEscribe la letra: ")
        #la letra introducida se convierte en mayuscula 
        letra=(letra.upper())
        #verificar que la letra no se haya introducido ya 
        if letra in intento:
            c=c+1
        intento=intento+letra
        #si la letra no está en la palabra aleatoria, quitar un intento y avanzar en el ahorcado
        if letra not in palabra or c!=0:
            intentos=intentos-1
            error=error+1
            print(horca[error])
            #en caso de que no se introduzca una letra (un número, un signo, etc.)
            if letra not in alfabeto:
                print("CARACTER INVALIDO")
            #en caso de que ya se haya introducido la letra 
            if c!=0:
                print("YA HABIAS PUESTO ESTA LETRA")
        else:
            #si la letra está en la palabra, ir revisando letra por letra
            for letra in palabra:
                #si la letra introducida está en la palabra aleatoria, se imprime la letra 
                if letra in intento:
                    print(letra, end="" )
                    a=a+1
                #si aun faltan letras por adivinar, se imprimen los espacios
                else:
                    print("_ ", end="")
            print("\n\nMUY BIEN")
    #se revisa si el usuario ganó o perdió
    if a==b:
        print("FELICIDADES!!! Has ganado :D")
    if intentos==0:
        print("PERDISTE :'c")

#JUEGO DE ADIVINAR EL NUMERO
def lista_digitos( n ):
    cadena = n
    lista = list()
    
    for caracter in cadena:
        numero = int(caracter)
        lista.append(numero)
        
    return( lista )

def adivina():
    print("\nBIENVENIDO AL JUEGO DE ADIVINA EL NÚMERO")
    print("Ingresa el nivel deseado en números, NO EN LETRAS\n\nNiveles disponibles:1, 2 y 3\n(1=Bajo, 2=Medio, 3=Alto)")
    #el usuario introduce el nivel deseado
    nivel=int(input("NIVEL: "))
    if nivel==0:
        nivel=5
    nivel=nivel+1
    a=""
    intentos=8
    intentou=""
    b=1
    c=0
    #en caso de que el usuario introduzca un nivel que no está disponible
    while nivel<1 or nivel>4:
        print ("NIVEL NO DISPONIBLE")
        nivel=int(input("NIVEL: "))
        if nivel==0:
            nivel=5
        nivel=nivel+1
    print("Tienes 8 oportunidades para adivinar el número de ",nivel," digitos")
    #se elige un numero al azar y el usuario lo tendrá que adivinar
    for i in range(nivel):
        numero= random.choice(['0','1','2','3','4','5','6','7','8','9'])
        a=a+numero
        print('_ ',end="")
    print('\n\n',a)
    while intentos>0 and c!=nivel:
        intentos=intentos-1
        c=0
        intentou=('')
        print("\nDame el numero (intento",b,")")
        intentou=input("")
        b=b+1
        #el intento del usuario se convierte a una lista
        digitos = lista_digitos( intentou )
        #el numero aleatorio se convierte a una lista
        amy= lista_digitos(a)
        #*se van comparando las posiciones de las dos listas*
        if nivel==2:
            if digitos[0]==amy[0]:
                print(digitos[0], end="" )
                c=c+1
            else:
                print("_ ", end="")
            if digitos[1]==amy[1]:
                print(digitos[1], end="")
                c=c+1
            else:
                print("_ ", end="")
#       
        elif nivel==3:
            if digitos[0]==amy[0]:
                print(digitos[0], end="" )
                c=c+1
            else:
                print("_ ", end="")
            if digitos[1]==amy[1]:
                print(digitos[1], end="")
                c=c+1
            else:
                print("_ ", end="")
        #Nivel 2
            if digitos[2]==amy[2]:
                print(digitos[2], end="")
                c=c+1
            else:
                print("_ ", end="")
#
        elif nivel==4:
            if digitos[0]==amy[0]:
                print(digitos[0], end="" )
                c=c+1
            else:
                print("_ ", end="")
            if digitos[1]==amy[1]:
                print(digitos[1], end="")
                c=c+1
            else:
                print("_ ", end="")
        #Nivel 2
            if digitos[2]==amy[2]:
                print(digitos[2], end="")
                c=c+1
            else:
                print("_ ", end="")
        #Nivel 3
            if digitos[3]==amy[3]:
                print(digitos[3], end="")
                c=c+1
            else:
                print("_ ", end="")
#
        else:
            print("Error")
    #se revisa si el usuario ganó o perdió
    if intentos==0 and intentou!=a:
        print("\n\nPERDISTE :'C")
    if intentou==a or c==a:
        print("\n\nFELICIDADES!! Has ganado")

#JUEGO DE MEMORIA
def memoria():
    print("\nBIENVENIDO AL JUEGO DE MEMORIA")
    #numero de caracteres iniciales
    caracteres=5
    memoriza = ""
    error=0
    #numero de veces que el usuario ha acertado
    a=0
    #tiempo (en segundos) que tiene el usuario para ver los digitos a memorizar
    tm=3
    while error<1:
        #se genera una imagen aleatoria para memorizar
        for i in range(caracteres):
            simbolo= random.choice([".","-"])
            memoriza= memoriza + simbolo
        #se le muestra al usuario los digitos a memorizar    
        print("Memoriza: "+ memoriza)
        time.sleep(tm)
        print("\n"*50 )
        #el usuario inserta sus digitos 
        adivina = input("¿Cuál fue?  ")
        #si el usuario acierta
        if memoriza == adivina :
            print("BIEN !!")
            caracteres= caracteres+1
            memoriza=""
            a=a+1
            if a%2==0:
                tm=tm+1
        #si el usuario falla
        else:
            print("ERROR")
            print("ACIERTOS: ", a)
            error=error+1
            
#TERMINAR
def terminar():
    #si el usuario ya no quiere jugar
    print("\nGRACIAS POR PARTICIPAR")
    
# 
def proyecto():
    opcion=1
    while opcion >= 1 and opcion <=4:
        print("""
    Menú de opciones:
    (1) Gato
    (2) Ahorcado
    (3) Adivina el número
    (4) Memoria
    (5) Terminar""")
        opcion= int(input("Escribe la opción: "))
        if opcion==1:
            gato()
        elif opcion==2:
            ahorcado()
        elif opcion==3:
            adivina()
        elif opcion==4:
            memoria()
        elif opcion==5:
            terminar()
            
proyecto()