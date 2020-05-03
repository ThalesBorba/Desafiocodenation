import json
import string
import os

alfabeto = list(string.ascii_lowercase)
decifrado_lista = []
with open("answer.json") as json_file:
    dados = json.load(json_file)
for c in range(0, len(dados["cifrado"])):
    if dados["cifrado"][c] in alfabeto:
        for d in range(0, len(alfabeto)):
            if dados["cifrado"][c] == alfabeto[d]:
                decifrado_lista.append(alfabeto[d - 1])
                break
    else:
        decifrado_lista.append(dados["cifrado"][c])
decifradoobj = "".join(decifrado_lista)
print(decifradoobj)

with open("answer.json", "r") as f:
    json_data = json.load(f)
    json_data["decifrado"] = decifradoobj

with open("answer.json", "w") as f:
    f.write(json.dumps(json_data))
