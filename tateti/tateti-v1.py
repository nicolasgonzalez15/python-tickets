def matriz_no_contiene_numeros(matriz):
  """
  Verifica si una matriz no contiene números.

  Args:
    matriz: La matriz (lista de listas) a verificar.

  Returns:
    True si la matriz no contiene números, False en caso contrario.
  """
  for fila in matriz:
    for elemento in fila:
      if isinstance(elemento, (int, float)):
        return False
  return True

# Funciones para dar fomato a la matriz

def formatoMatriz(matriz):

    for fila in matriz:
        for valor in fila:
            print(valor, end="|")
        print("")

def diagonalCompleta(matriz):
    completa = False
    if (matriz[0][0] == 'X' and matriz[1][1] == 'X' and matriz[2][2] == 'X'):
        print("Diagonal 0 completa.")
        completa = True
    if (matriz[2][0] == 'X' and matriz[1][1] == 'X' and matriz[0][2] == 'X'):
        print("Columna 1 completa.")
        completa = True

    return completa

#Funciones para validar si filas, columnas o diagonales están ocupadas tanto para X como O

def filaCompletaBeta(matriz,valor):
    completa = False
    if (matriz[0][0] == valor and matriz[0][1] == valor and matriz[0][2] == valor):
        print(f"Fila 0 completa con valor {valor}.")
        completa = True
    if (matriz[1][0] == valor and matriz[1][1] == valor and matriz[1][2] == valor):
        print(f"Fila 1 completa con valor {valor}.")
        completa = True
    if (matriz[2][0] == valor and matriz[2][1] == valor and matriz[2][2] == valor):
        print(f"Fila 2 completa con valor {valor}.")
        completa = True

    return completa

def columnaCompletaBeta(matriz,valor):
    completa = False
    if (matriz[0][0] == valor and matriz[1][0] == valor and matriz[2][0] == valor):
        print(f"Columna 0 completa con valor {valor}.")
        completa = True
    if (matriz[0][1] == valor and matriz[1][1] == valor and matriz[2][1] == valor):
        print(f"Columna 1 completa con valor {valor}.")
        completa = True
    if (matriz[0][2] == valor and matriz[1][2] == valor and matriz[2][2] == valor):
        print(f"Columna 2 completa con valor {valor}.")
        completa = True

    return completa

def diagonalCompletaBeta(matriz,valor):
    completa = False
    if (matriz[0][0] == valor and matriz[1][1] == valor and matriz[2][2] == valor):
        print(f"Diagonal 0 completa con valor {valor}.")
        completa = True
    if (matriz[2][0] == valor and matriz[1][1] == valor and matriz[0][2] == valor):
        print(f"Diagonal 1 completa con valor {valor}.")
        completa = True

    return completa

def jugar():

    
    matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

    enJuego = True

    turno = 'X'
    intentosPrimero = 0
    intentosSegundo = 0

    while enJuego:


        if matriz_no_contiene_numeros(matriz):
            print("Juego terminado")
            enJuego = False
        
        else:

            if filaCompletaBeta(matriz,'X') or filaCompletaBeta(matriz,'O'):
                print("Terminó el juego")
                break

            if columnaCompletaBeta(matriz,'X') or columnaCompletaBeta(matriz,'O'):
                print("Terminó el juego")
                break

            if diagonalCompletaBeta(matriz,'X') or diagonalCompletaBeta(matriz,'O'):
                print("Terminó el juego")
                break
            
            print(f"Turno jugador {turno} \n")

            vi = input("Valor de x a cambiar (entre 0 y 2): ")
            vj = input("Valor de y a cambiar (entre 0 y 2): ")

            if vi.isdigit() and vj.isdigit():    
                
                #Convierto a enteros
                i = int(vi)
                j = int(vj)

                if 0<=i<=2 and 0<=j<=2:

                    if(matriz[i][j] == 'X'):
                        print("\n")
                        print("Posición ocupada. Elija otro par de valores.")

                    if(matriz[i][j] == 'O'):
                        print("\n")
                        print("Posición ocupada. Elija otro par de valores.")

                    if turno=='X':
                    
                        matriz[i][j] = 'X'
                        turno = 'O'
                    
                    elif turno == 'O':

                        matriz[i][j] = 'O'
                        turno = 'X'

                else:
                    print("\n")
                    print("Coordenada inválida. Vuelva a ingresar los valores de x e y (entre 0 y 2).")
                    #enJuego = False
            else:
                print("\n")
                print("Caracter ingresado inválido. Por favor, vuelva a ingresar los valores de x e y (entre 0 y 2).")
 
            print("\n")
            formatoMatriz(matriz)
    
jugar()
print("Gracias por jugar con nosotros.")