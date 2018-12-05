#!/usr/bin/python3
# miembro = {"id": int, "rival": int , "precio": int}
lista_dsp = []
lista_ppp = []
dsp, ppp, rivales, presupuesto = input().strip().split(" ")
ppp = int(ppp)
dsp = int(dsp)
rivales = int(rivales)
presupuesto = int(presupuesto)
precios_DSP = [int(elem) for elem in input().strip().split(" ")]
precios_PPP = [int(elem) for elem in input().strip().split(" ")]
for i in range(dsp):
    lista_dsp.append({"id": i + 1 , "rival": [] , "precio": int(precios_DSP[i])})
for i in range(ppp):
    lista_ppp.append({"id": i + 1 , "rival": [] , "precio": int(precios_PPP[i])})
for i in range(rivales):
    x, y = input().strip().split(" ")
    lista_dsp[int(x) - 1]["rival"].append(int(y))
    lista_ppp[int(y) - 1]["rival"].append(int(x))

lista_dsp.sort(key= lambda x: x["precio"])
lista_ppp.sort(key= lambda x: x["precio"])
print(lista_dsp)
print(lista_ppp)
posibles_ppp = list(filter(lambda x: len(x["rival"]) == 0, lista_dsp)) # Para cambiar al ppp
posibles_dsp = list(filter(lambda x: len(x["rival"]) == 0, lista_ppp)) # Para cambiar al DSP
print(posibles_dsp)
print(posibles_ppp)
