#!/usr/bin/python3
num_h = int(input())
lista_h = list(map(lambda x: int(x),input().strip().split(" ")))
num_m = int(input())
lista_m = list(map(lambda x: int(x),input().strip().split(" ")))
lista_h.sort()
lista_m.sort()
lista = list(filter(lambda x: abs(x[0]-x[1]) <= 1 ,zip(lista_h, lista_m)))
print(len(lista))
