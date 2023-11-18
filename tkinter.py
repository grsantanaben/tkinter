import tkinter as tk

root = tk.Tk()
root.geometry('800x600')
button = tk.Button(root, text='BOTÃO')
label = tk.Label(root, text="Hello World")

#Pacotes

button.pack()
label.pack()


root.mainloop()