from tkinter import*

raiz=Tk()

raiz.title("Interfaz grafica")

raiz.resizable(1, 1)

raiz.iconbitmap("UAX.ico")


raiz.config(bg="black")

miFrame=Frame()

miFrame.pack(fill="both", expand="True")

miFrame.config(bg="grey")

miFrame.config(width="650", height="350")

miFrame.config(bd=35)

miFrame.config(relief="groove")

miFrame.config(cursor="pirate")

raiz.mainloop()

