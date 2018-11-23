n = int(input())
lista = list(map(lambda x: int(x), input().strip().split(" ")))
lista.sort()
lista2 = list(map(lambda x: str(x), lista))
del lista
print(" ".join(lista2))
del lista2
del n
