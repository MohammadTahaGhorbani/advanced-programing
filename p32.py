import random

daneshjoha = []

esmha = [
    "علی رضایی",
    "محمد احمدی",
    "حسین کریمی",
    "امیر محمدی",
    "رضا حسینی",
    "مهدی موسوی",
    "پارسا جعفری",
    "آرمان قاسمی"
]

kode_dars = [101, 102, 103, 104, 105, 106, 107, 108]

for i in range(100):

    shomare_daneshjo = random.randint(10000000, 99999999)

    if i < 8:
        esm = esmha[i]
    else:
        esm = "دانشجو " + str(i + 1)

    nomreha = []

    for j in range(8):
        nomre = random.randint(0, 20)
        nomreha.append(nomre)

    jam_nomreha = sum(nomreha)
    moadel = jam_nomreha / 8

    daneshjo = {
        "esm": esm,
        "shomare": shomare_daneshjo,
        "kode_dars": kode_dars,
        "nomreha": nomreha,
        "jam": jam_nomreha,
        "moadel": moadel
    }

    daneshjoha.append(daneshjo)

for daneshjo in daneshjoha:
    print(daneshjo)