#!/usr/bin/python3
n = int(input())
usuarios = {}

for i in range(n):
    dato = input().strip().split(" ")
    #print(dato)
    paso = False
    try:
        # Revisar values

        for key, value in usuarios.items():
            if dato[0] == value:
                usuarios[key] = dato[1]
                paso = True

        if not paso:
            raise KeyError

    except KeyError:
        #print("ERROR key")
        usuarios[dato[0]] = dato[1]

    #print(usuarios[dato[0]])
print(len(usuarios))
for k,v in usuarios.items():
    print(k, v)
