import numpy as np
class Globalne:
    home1 = [[400.182, -358.349, 619.5], [0.5,0,0.86603,0]]
    home2 = [[400.182, 721.651, 619.5], [0.5,0,0.86603,0]]
    v1 = 1000
    v2 = 100
    wobj = [[192.712,358.349,10],[1,0,0,0]]
    elitizam = True
    verovatnoca_mutacije = 0.5
    velicina_generacije = 100
    velicina_uzorka = 40
    broj_generacija = 80
    broj_tacaka = 12
    lista_targeta = []
    cntr = 0
    quat = [0.0, 0.0, 1.0, 0.0]
    for i in range(broj_tacaka):
        pos = [np.random.randint(0, 300), np.random.randint(0, 300), 0]
        lista_targeta.append([pos, quat])