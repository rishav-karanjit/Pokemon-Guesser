import tkinter
from tkinter import *

import backend
import frontend

root = Tk()
root.title('Pokémon Guesser')
root.minsize(800, 650)
root.configure(background='black')

fake_root = Label(master=root, background='black')
fake_root.pack(expand=1, fill=tkinter.BOTH)
fake_root.rowconfigure(0, weight=1)
fake_root.rowconfigure(1, weight=1)

backend.toggleGeneration(0)
frontend.drawStart(fake_root)

root.mainloop()
