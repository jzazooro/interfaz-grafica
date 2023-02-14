from tkinter import*

raiz=Tk()

raiz.title("Interfaz grafica")

raiz.iconbitmap("UAX.ico")

raiz.config(bg="blue")

miFrame=Frame()

miFrame.pack(fill="y", expand="True")

miFrame.config(bg="grey")

miFrame.config(width="1200", height="600")

miFrame.config(bd=35)

miFrame.config(relief="groove")

miFrame.config(cursor="pirate")

Label(miFrame, text="Practica de interfaz grafica", font= ("Arial", 20)).place(x=400, y=30)

Label(miFrame, text="Nombre y apellidos: ", font=("Arial", 12)).place(x=175, y=150)

textouno=Entry(miFrame)

textouno(font=("Arial", 12))

textouno.place(x=350, y=150)

raiz.mainloop()