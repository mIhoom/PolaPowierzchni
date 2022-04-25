import math
import tkinter
from tkinter import *

def pole_kwadratu(a):
    return a * a

def pole_prostokata(a, b):
    return a * b

def pole_kola(r):
    return math.pi * r ** 2

def pole_trojkata(a, h):
    return 0.5 * a * h

def pole_trapezu(a, b, h):
    return (a + b) / 2 * h

root = tkinter.Tk()
root.title("Pola Powierzchni by MM")
root.geometry('500x500')
root.resizable(width=False, height=False)

tekst = tkinter.Label(root, text = "Wybierz figurę, której pole chcesz obliczyć:", font = 15)
tekst.place(x = 30, y = 30)
wybor1 = tkinter.Button(root, command = 1, text = "Kwadrat", font = 10)
wybor1.place(x = 30, y = 80)
wybor2 = tkinter.Button(root, command = 1, text = "Prostokąt", font = 10)
wybor2.place(x = 30, y = 140)
wybor3 = tkinter.Button(root, command = 1, text = "Koło", font = 10)
wybor3.place(x = 30, y = 200)
wybor4 = tkinter.Button(root, command = 1, text = "Trójkąt", font = 10)
wybor4.place(x = 30, y = 260)
wybor5 = tkinter.Button(root, command = 1, text = "Trapez", font = 10)
wybor5.place(x = 30, y = 320)





wybor = input("""Wybierz figurę, której pole chcesz obliczyć:
1. Kwadrat
2. Prostokąt
3. Koło
4. Trójkąt
5. Trapez
""")





root.mainloop()