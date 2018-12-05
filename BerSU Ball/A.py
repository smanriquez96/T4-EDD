#!/usr/bin/python3
num_h = int(input())
lista_h = list(map(lambda x: int(x),input().strip().split(" ")))
num_m = int(input())
lista_m = list(map(lambda x: int(x),input().strip().split(" ")))
lista_h.sort()
lista_m.sort()
p_h = 0
p_m = 0
contador = 0

if num_h >= num_m:
    while p_m < num_m and p_h < num_h:
        if abs(lista_m[p_m] - lista_h[p_h]) <= 1:
            contador += 1
            p_m += 1
            p_h += 1
        else:
            if lista_m[p_m] > lista_h[p_h]:
                p_h += 1
            else:
                p_m += 1

else:
    while p_h < num_h and p_m < num_m:
        if abs(lista_h[p_h] - lista_m[p_m]) <= 1:
            contador += 1
            p_m += 1
            p_h += 1
        else:
            if lista_m[p_m] > lista_h[p_h]:
                p_h += 1
            else:
                p_m += 1

print(contador)
