import tkinter as tk
from tkinter import messagebox
import tkinter.font as font

# Función para verificar si hay un ganador
def verificar_ganador():
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] != "":
            return tablero[i][0], [(i, 0), (i, 1), (i, 2)]  # Devuelve el símbolo ganador y las coordenadas
        if tablero[0][i] == tablero[1][i] == tablero[2][i] != "":
            return tablero[0][i], [(0, i), (1, i), (2, i)]
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != "":
        return tablero[0][0], [(0, 0), (1, 1), (2, 2)]
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != "":
        return tablero[0][2], [(0, 2), (1, 1), (2, 0)]
    return None, []

# Función para manejar el clic en un botón del tablero
def clic_casilla(i, j):
    if tablero[i][j] == "" and not ganador:
        if turno:
            tablero[i][j] = "X"
            boton = botones[i][j]
            boton.config(text="X", state="disabled")
        else:
            tablero[i][j] = "O"
            boton = botones[i][j]
            boton.config(text="O", state="disabled")
        ganador_actual, coordenadas_ganadoras = verificar_ganador()
        if ganador_actual:
            for coord in coordenadas_ganadoras:
                x, y = coord
                botones[x][y].config(bg="yellow")  # Cambia el fondo de las casillas ganadoras
            messagebox.showinfo("¡Ganador!", f"Ganador: {ganador_actual}")
            # No salir del juego
        elif "" not in [casilla for fila in tablero for casilla in fila]:
            messagebox.showinfo("Empate", "El juego terminó en empate.")
            # No salir del juego
        else:
            turno_actual()

# Función para cambiar el turno
def turno_actual():
    global turno
    turno = not turno
    if turno:
        turno_label.config(text="Turno de X", fg="blue")
    else:
        turno_label.config(text="Turno de O", fg="red")

# Función para reiniciar el juego
def reiniciar_juego():
    global turno, ganador, tablero
    turno = True
    ganador = None
    tablero = [["" for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            botones[i][j].config(text="", state="active", bg="SystemButtonFace")
    turno_label.config(text="Turno de X")

# Crear ventana
ventana = tk.Tk()
ventana.title("Tateti ISFT N°240")
ventana.config(pady=2)

# Obtener dimensiones de la pantalla
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()

# Definir las dimensiones de la ventana
ancho_ventana = 500
alto_ventana = 500

# Calcular las coordenadas para centrar la ventana
x = (ancho_pantalla - ancho_ventana) // 2
y = (alto_pantalla - alto_ventana) // 2

# Establecer la geometría de la ventana centrada
ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

# Crear un marco para el tablero que se expandirá
tablero_frame = tk.Frame(ventana)
tablero_frame.pack(expand=True, fill="both")

# Inicializar variables
turno = True  # True para X, False para O
ganador = None
tablero = [["" for _ in range(3)] for _ in range(3)]

# Crear botones para el tablero
botones = []
for i in range(3):
    fila_botones = []
    for j in range(3):
        boton = tk.Button(tablero_frame, text="", width=10, height=3,
                          command=lambda i=i, j=j: clic_casilla(i, j))
        boton.config(font=("Arial", 24, "bold"), fg="black")  # Cambia el tamaño y el color de la fuente aquí
        boton.grid(row=i, column=j, sticky="nsew")  # "sticky" expande el botón para llenar la celda
        fila_botones.append(boton)
    botones.append(fila_botones)

# Configurar el marco para expandirse automáticamente
for i in range(3):
    tablero_frame.grid_rowconfigure(i, weight=1)
    tablero_frame.grid_columnconfigure(i, weight=1)

# Etiqueta para mostrar el turno actual
turno_label = tk.Label(ventana, text="Turno de X", font=("Arial", 16), fg="blue")
turno_label.config()
turno_label.pack()

# Botón para reiniciar el juego
boton_reiniciar = tk.Button(ventana, text="Reiniciar Juego", command=reiniciar_juego)
boton_reiniciar.config(bg="grey", fg="white", font="Arial")
boton_reiniciar.pack()

# Iniciar la ventana
ventana.mainloop()
