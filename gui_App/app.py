from tkinter import *
import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()

canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
canvas.pack()


frame = tk.Frame(root,bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile = tk.Button(root, text="Open File", padx=10, pady=5, fg="white", bg="#263D42")
openFile.pack()

runApps = tk.Button(root, text="Run Apps", padx=10, pady=5, fg="white", bg="#263D42")
runApps.pack()

root.mainloop()
'''
from tkinter import *

root = Tk()
root.title('Calculator Program')

button_1 = Button(root, text='1', width='30', height='20')
button_1.pack()

root.mainloop()
'''