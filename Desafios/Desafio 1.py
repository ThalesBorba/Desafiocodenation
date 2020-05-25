import datetime
taxa = 0.36
tarifas = []
final = []
total = 0
temp = {}

records = [
    {'source': '48-996355555', 'destination': '48-666666666',
        'end': 1564610974, 'start': 1564610674},
    {'source': '41-885633788', 'destination': '41-886383097',
        'end': 1564506121, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-886383097',
        'end': 1564630198, 'start': 1564629838},
    {'source': '48-999999999', 'destination': '41-885633788',
        'end': 1564697158, 'start': 1564696258},
    {'source': '41-833333333', 'destination': '41-885633788',
        'end': 1564707276, 'start': 1564704317},
    {'source': '41-886383097', 'destination': '48-996384099',
        'end': 1564505621, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '48-996383697',
        'end': 1564505721, 'start': 1564504821},
    {'source': '41-885633788', 'destination': '48-996384099',
        'end': 1564505721, 'start': 1564504821},
    {'source': '48-996355555', 'destination': '48-996383697',
        'end': 1564505821, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '41-886383097',
        'end': 1564610750, 'start': 1564610150},
    {'source': '48-996383697', 'destination': '41-885633788',
        'end': 1564505021, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-885633788',
        'end': 1564627800, 'start': 1564626000}
]
# Botando na ordem do maior telefone para o menor
sort = sorted(records, key=lambda k: k['source'], reverse=True)

"""sort.append({'source': '0', 'destination': '48-666666666',
            'end': 1564610974, 'start': 1564610674})
"""
def calcula_tarifa(taxa, duracao):
    return taxa + int(duracao / 60) * 0.09

numeroTarifaDicionario = {}

for c in range(len(sort)):
    # Transformando epoch em data
    inicio = datetime.datetime.fromtimestamp(sort[c]['start'])
    # Transformando data em minutos
    inicioHM = int(inicio.strftime("%H")) * 3600 + int(inicio.strftime("%M")) * 60 + int(inicio.strftime("%S"))
    fim = datetime.datetime.fromtimestamp(sort[c]['end'])
    fimHM = int(fim.strftime("%H")) * 3600 + int(fim.strftime("%M")) * 60 + int(fim.strftime("%S"))
    # Horário sem cobrança de minutos (22h às 6h)
    if inicioHM > 79200 or fimHM < 21600:
        duracao = 0
    # Caso haja interpolação, ignora o horário livre de cobrança
    else:
        if inicioHM < 21600 >= fimHM:
            inicioHM = 21600
        if fimHM > 79200 <= inicioHM:
            fimHM = 79200
        duracao = fimHM - inicioHM
    # Cria entrada para o número
    tarifas.append(f'{taxa + int(duracao / 60) * 0.09:.2f}')
    # Juntando os números iguais e somando respectivas taxas
    numeroAtual = sort[c]['source']

    if numeroAtual not in numeroTarifaDicionario:
        numeroTarifaDicionario[numeroAtual] = calcula_tarifa(taxa, duracao)
    else:
        tarifaAntiga = numeroTarifaDicionario[numeroAtual]
        tarifaNova = calcula_tarifa(taxa, duracao)
        tarifaTotal = tarifaAntiga + tarifaNova
        numeroTarifaDicionario[numeroAtual] = tarifaTotal

""" 
    if sort[c]['source'] == sort[c + 1]['source']:
        total += float(tarifas[c])
    else:
        total += float(tarifas[c])
        temp['source'] = sort[c]['source']
        temp['total'] = float(f'{total:.2f}')
        final.append(temp.copy())
        total = 0 ggghgfhfghf
"""


print(numeroTarifaDicionario)





def classify_by_phone_number():
    return final
