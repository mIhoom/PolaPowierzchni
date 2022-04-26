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


#Ustawienia okna 
root = tkinter.Tk()
root.title("Pola Powierzchni by MM")
root.geometry('500x500')
root.resizable(width=False, height=False)
# Komunikat okna
tekst = tkinter.Label(root, text = "Wybierz figurę, której pole chcesz obliczyć\n Podaj niezbędne dane i wciśnij przycisk figury:", font = 15)
tekst.place(x = 10, y = 10)

# Dane dotyczące kwadratu
wybor1 = tkinter.Button(root, text = "Kwadrat", font = 10,)
wybor1.place(x = 30, y = 80)
wybor1a = tkinter.Entry(root, width = 5) 
wybor1a.place(x =300, y = 86)
wybor1d = tkinter.Label(root, text = "a", font = 10)
wybor1d.place(x = 280, y =84)

#Dane dotyczące prostokąta
wybor2 = tkinter.Button(root, command = 1, text = "Prostokąt", font = 10)
wybor2.place(x = 30, y = 140)
wybor2a = tkinter.Entry(root, width = 5)
wybor2a.place(x = 300, y = 146)
wybor2b = tkinter.Entry(root, width = 5)
wybor2b.place(x = 400, y = 146)
wybor2d = tkinter.Label(root, text = "a", font = 10)
wybor2d.place(x = 280, y = 144)
wybor2e = tkinter.Label(root, text = "b", font = 10)
wybor2e.place(x = 380, y = 144)

#Dane dotyczęce koła
wybor3 = tkinter.Button(root, command = 1, text = "Koło", font = 10)
wybor3.place(x = 30, y = 200)
wybor3a = tkinter.Entry(root, width = 5)
wybor3a.place(x = 300, y = 206)
wybor3b = tkinter.Label(root, text = "r", font = 10)
wybor3b.place(x = 280, y = 204)

#Dane dotyczące trójkąta
wybor4 = tkinter.Button(root, command = 1, text = "Trójkąt", font = 10)
wybor4.place(x = 30, y = 260)
wybor4a = tkinter.Entry(root, width = 5)
wybor4a.place(x= 300, y = 266)
wybor4b = tkinter.Entry(root, width=  5)
wybor4b.place(x = 400, y = 266)
wybor4c = tkinter.Label(root, text = "a", font = 10)
wybor4c.place(x = 280, y = 264)
wybor4d = tkinter.Label(root, text = "h", font = 10)
wybor4d.place(x = 380, y = 264)

#Dane dotyczące trapezu
wybor5 = tkinter.Button(root, command = 1, text = "Trapez", font = 10)
wybor5.place(x = 30, y = 320)
wybor5a = tkinter.Entry(root, width = 5)
wybor5a.place(x = 200, y = 326)
wybor5b = tkinter.Entry(root, width = 5)
wybor5b.place(x = 300, y = 326)
wybor5c = tkinter.Entry(root, width = 5)
wybor5c.place(x = 400, y = 326)
wybor5d = tkinter.Label(root, text = "a", font = 10)
wybor5d.place(x = 180, y = 324)
wybor5e = tkinter.Label(root, text = "b", font = 10)
wybor5e.place(x = 280, y = 324)
wybor5f = tkinter.Label(root, text = "h", font = 10)
wybor5f.place(x = 380, y = 324)

#Wyniki obliczeń
wynik = tkinter.Label(root, font = 20, fg = "green", width = 20, height = 3)
wynik.place(x = 118, y = 410)
wynik1 = tkinter.Label(root, font = 10, text = "Pole powierzchni figury wynosi: ")
wynik1.place(x = 90 ,y = 380)

#Uruchomienie cłości
root.mainloop()