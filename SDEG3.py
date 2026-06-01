import tkinter as tk
from tkinter import font
import random
import string


# Sistema De Emergencia Garantizada 3

class MatrixPrankApp:

    def __init__(self, root):
        self.root = root
        self.root.title("SDEG1")
        self.root.geometry("500x400")
        self.root.config(bg="#1e1e1e")

        self.fuente_grande = font.Font(family="Times New Roman", size=20, weight="bold")
        self.fuente_normal = font.Font(family="Times New Roman", size=15)

        self.paso_actual = 0

        self.mensajes = [
            "...",
            "Inicializando AI",
            "Esta pagina no puede ser cerrada, si quieres intentalo.",
            "Como se siente que esta pagina no puede ser cerrada?",
            "No solo eso...\nTambien te he robado todos tus datos y los publicare uno a uno.",
            "JAJAJAJAJA, tienes miedo?\nPresiona otra vez el boton para que sepas que es el TERROR."
        ]

        self.crear_interfaz()

        self.root.protocol("WM_DELETE_WINDOW", self.impedir_cierre)
        self.root.bind("<Key>", self.cerrar_secreto)

    def crear_interfaz(self):

        self.etiqueta = tk.Label(
            self.root,
            text="Inicializando procesos de analisis de datos",
            fg="#00ff00",
            bg="#1e1e1e",
            font=self.fuente_normal
        )
        self.etiqueta.pack(pady=20)

        self.boton = tk.Button(
            self.root,
            text="...",
            command=self.siguiente_paso,
            bg="#3a3a3a",
            fg="#00ff00",
            activebackground="#555555"
        )
        self.boton.pack(pady=10)

        self.canvas = tk.Canvas(self.root, bg="#1e1e1e", highlightthickness=0)

    def siguiente_paso(self):

        if self.paso_actual < len(self.mensajes):
            self.etiqueta.config(text=self.mensajes[self.paso_actual])
            self.paso_actual += 1
        else:
            self.iniciar_animacion()

    def iniciar_animacion(self):

        self.etiqueta.pack_forget()
        self.boton.pack_forget()

        self.root.attributes("-fullscreen", True)

        self.canvas.pack(fill="both", expand=True)

        self.root.update_idletasks()

        self.ancho = self.root.winfo_width()
        self.alto = self.root.winfo_height()

        self.inicializar_columnas()

        self.animar_lluvia()

    def inicializar_columnas(self):

        self.columnas = []

        caracteres = string.digits + string.ascii_letters + "!@#$%^&*()[]{}<>?/|\\~"

        for x in range(0, self.ancho, 12):

            columna = {
                "x": x,
                "y": random.uniform(-self.alto, 0),
                "longitud": random.randint(8, 25),
                "velocidad": random.uniform(30, 50),
                "caracteres": [random.choice(caracteres) for _ in range(25)]
            }

            self.columnas.append(columna)

    def animar_lluvia(self):

        self.canvas.delete("all")

        for col in self.columnas:

            col["y"] += col["velocidad"]

            if col["y"] > self.alto + 200:
                col["y"] = random.uniform(-self.alto, 0)

            for i in range(col["longitud"]):

                y_pos = col["y"] - i * 20

                if 0 <= y_pos <= self.alto:

                    if i == 0:
                        color = "#FFFFFF"
                    elif i < 4:
                        color = "#AAFFAA"
                    else:
                        verde = max(20, 255 - (i * 20))
                        color = f"#00{verde:02x}00"

                    self.canvas.create_text(
                        col["x"],
                        y_pos,
                        text=random.choice(string.ascii_letters + string.digits),
                        fill=color,
                        font=self.fuente_grande
                    )

        self.root.after(30, self.animar_lluvia)

    def impedir_cierre(self):

        self.popup("Nop", "No lo vas a cerrar tan fácil.")

    def popup(self, titulo, mensaje):

        ventana = tk.Toplevel(self.root)
        ventana.title(titulo)
        ventana.config(bg="#1e1e1e")
        ventana.geometry("300x150")

        label = tk.Label(
            ventana,
            text=mensaje,
            bg="#1e1e1e",
            fg="#00ff00",
            wraplength=260,
            font=self.fuente_normal
        )

        label.pack(pady=20)

        boton = tk.Button(
            ventana,
            text="...",
            command=ventana.destroy,
            bg="#3a3a3a",
            fg="#00ff00"
        )

        boton.pack()

    def cerrar_secreto(self, event):

        if event.char == "j":
            self.root.destroy()


if __name__ == "__main__":

    root = tk.Tk()

    app = MatrixPrankApp(root)

    root.mainloop()