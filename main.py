import pandas as pd
from random import choice

path = "pc_config.csv"
data = pd.read_csv(path)

proc         = [[], []]
culer        = [[], []]
matplat      = [[], []]
mod_pam      = [[], []]
vent         = [[], []]
videokart    = [[], []]
block_pit    = [[], []]
korp         = [[], []]
wifi_adapter = [[], []]

for i, v in data.iterrows():

    if "Процессор" in v['Name']:
        proc[0].append(v['Price'])
        proc[1].append(v['Name'])

    elif "Устройство охлаждения(кулер)" in v['Name']:
        culer[0].append(v['Price'])
        culer[1].append(v['Name'])

    elif "Материнская плата" in v['Name']:
        matplat[0].append(v['Price'])
        matplat[1].append(v['Name'])

    elif "Модуль памяти" in v['Name']:
        mod_pam[0].append(v['Price'])
        mod_pam[1].append(v['Name'])

    elif "Вентилятор" in v['Name']:
        vent[0].append(v['Price'])
        vent[1].append(v['Name'])

    elif "Видеокарта" in v['Name']:
        videokart[0].append(v['Price'])
        videokart[1].append(v['Name'])

    elif "Блок питания" in v['Name']:
        block_pit[0].append(v['Price'])
        block_pit[1].append(v['Name'])

    elif "Корпус" in v['Name']:
        korp[0].append(v['Price'])
        korp[1].append(v['Name'])

    elif "Сетевой адаптер" in v['Name']:
        wifi_adapter[0].append(v['Price'])
        wifi_adapter[1].append(v['Name'])


print("максимальная цена сборки - ", sum([max(wifi_adapter[0]), max(korp[0]), max(block_pit[0]), max(videokart[0]), max(vent[0]), max(mod_pam[0]), max(matplat[0]), max(culer[0]), max(proc[0])]))
print("минимальная цена сборки - ", sum([min(wifi_adapter[0]), min(korp[0]), min(block_pit[0]), min(videokart[0]), min(vent[0]), min(mod_pam[0]), min(matplat[0]), min(culer[0]), min(proc[0])]))

while 1:
    inp = int(input("Введите цену за которую хотите собрать ПК: "))
    while 1:
        cong = [choice(proc[1]), choice(culer[1]), choice(matplat[1]), choice(mod_pam[1]) + choice(vent[1]),  choice(videokart[1]), choice(block_pit[1]), choice(korp[1]), choice(wifi_adapter[1])]
        cong_price = [choice(proc[0]), choice(culer[0]), choice(matplat[0]), choice(mod_pam[0]) + choice(vent[0]),  choice(videokart[0]), choice(block_pit[0]), choice(korp[0]), choice(wifi_adapter[0])]
        summy = sum(cong_price)
        if summy in range(inp-5000, inp+5000):
            print("цена - ", summy)
            print("сборка - ", cong)
            break