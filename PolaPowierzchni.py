import math
from multiprocessing.connection import wait
from pickle import TRUE


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

wybor = input("""Wybierz figurę, której pole chcesz obliczyć:
1. Kwadrat
2. Prostokąt
3. Koło
4. Trójkąt
5. Trapez
""")
while True:
    if wybor == '1':
        a = float(input("Podaj bok kwadratu:" ))
        print("Pole kwadratu wynosi:", pole_kwadratu(a))
    
    if wybor =='2':
        a = float(input("Podaj pierwszy bok prostokąta:"))
        b = float(input("Podaj drugi bok prostokąta:"))
        print("Pole prostokąta wynosi:", pole_prostokata(a, b))
    
    if wybor == '3':
        r = float(input("Podaj promień koła:"))
        print("Pole koła wynosi:", pole_kola(r))
    
    if wybor == '4':
        a = float(input("Podaj bok trójkąta:"))
        h = float(input("podaj wysokość trójkąta:"))
        print("Pole trójkąta wynosi:", pole_trojkata(a, h))
    
    if wybor == '5':
        a = float(input("Podaj pierwszy bok trapezu:"))
        b = float(input("Podaj drugi bok trapezu:"))
        h = float(input("Podaj wysokość trapezu:"))
        print("Pole trapezu wynosi:", pole_trapezu(a, b, h))
            