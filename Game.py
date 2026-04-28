import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.turno_x = True
        self.movimientos = 0
        self.botones = []

        # Crear la cuadrícula de 3x3
        for i in range(9):
            btn = tk.Button(self.window, text="", font=("Arial", 24, "bold"), 
                            width=5, height=2, command=lambda i=i: self.boton_click(i))
            btn.grid(row=i//3, column=i%3)
            self.botones.append(btn)

    def boton_click(self, index):
        btn = self.botones[index]
        
        # Si el botón ya tiene texto, no hacer nada
        if btn["text"] != "":
            return

        # Poner X o O según el turno
        btn["text"] = "X" if self.turno_x else "O"
        self.movimientos += 1
        
        if self.verificar_ganador():
            ganador = "X" if self.turno_x else "O"
            messagebox.showinfo("Fin del juego", f"¡Ganó {ganador}!")
            self.reiniciar()
        elif self.movimientos == 9:
            messagebox.showinfo("Fin del juego", "¡Empate!")
            self.reiniciar()
        else:
            self.turno_x = not self.turno_x

    def verificar_ganador(self):
        # Combinaciones ganadoras (índices de la lista de botones)
        ganadoras = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8), # Horizontales
            (0, 3, 6), (1, 4, 7), (2, 5, 8), # Verticales
            (0, 4, 8), (2, 4, 6)             # Diagonales
        ]
        for a, b, c in ganadoras:
            if self.botones[a]["text"] == self.botones[b]["text"] == self.botones[c]["text"] != "":
                return True
        return False

    def reiniciar(self):
        for btn in self.botones:
            btn["text"] = ""
        self.turno_x = True
        self.movimientos = 0

    def iniciar(self):
        self.window.mainloop()

if __name__ == "__main__":
    juego = TicTacToe()
    juego.iniciar()
