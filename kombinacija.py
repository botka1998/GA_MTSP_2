import math
import random

from globalne import *
class Kombinacija:
    def __init__(self):
        self.rute = []
        self.baza = []
        self.fitness = 0

    def ispuni_random(self):
        #ucitamo sve targete
        self.baza = []
        self.rute = []
        for i in range(Globalne.broj_tacaka):
            self.baza.append(Globalne.lista_targeta[i].copy())
        random.shuffle(self.baza) #promesamo ih

        #dodajemo u rute
        indx = random.randint(0,Globalne.broj_tacaka - 1)

        rob1 = []
        rob2 = []
        rob1.insert(0, Globalne.home1)
        rob2.insert(0, Globalne.home2)
        for i in range(indx):
            rob1.append(self.baza[i])
        for i in range(indx, Globalne.broj_tacaka):
            rob2.append(self.baza[i])
        rob1.append(Globalne.home1)
        rob2.append(Globalne.home2)

        self.rute.insert(0, rob1.copy())
        self.rute.insert(1, rob2.copy())





    def dodaj_rutu(self,indx,ruta):
        self.rute.insert(indx,ruta.copy())

    def get_duzina(self):
        duzina = 0
        prethodni = self.rute[0][0][0].copy()
        for i in range(len(self.rute[0])):
            trenutni = self.rute[0][i][0]
            duzina += math.dist(prethodni, trenutni)
            prethodni = trenutni
        prethodni = self.rute[1][0][0].copy()
        for i in range(len(self.rute[1])):
            trenutni = self.rute[1][i][0]
            duzina += math.dist(prethodni, trenutni)
            prethodni = trenutni
        return duzina
    def get_duzine(self):
        duzina1 = 0
        duzina2 = 0
        prethodni = self.rute[0][0][0].copy()
        for i in range(len(self.rute[0])):
            trenutni = self.rute[0][i][0]
            duzina1 += math.dist(prethodni, trenutni)
            prethodni = trenutni
        prethodni = self.rute[1][0][0].copy()
        for i in range(len(self.rute[1])):
            trenutni = self.rute[1][i][0]
            duzina2 += math.dist(prethodni, trenutni)
            prethodni = trenutni
        return duzina1, duzina2
    def baza_od_ruta(self):
        self.baza = []
        duzina1 = len(self.rute[0])
        duzina2 = len(self.rute[1])
        if duzina1 != 2:
            for i in range(1, duzina1-1):
                self.baza.append(self.rute[0][i].copy())
        if duzina2 != 2:
            for i in range(1, duzina2-1):
                self.baza.append(self.rute[1][i].copy())

    def get_fitness(self):
        d1, d2 = self.get_duzine()
        vreme = (d1 / Globalne.v1) + (d2 / Globalne.v2)
        #self.fitness = 1/self.get_duzina()
        self.fitness = 1 / vreme
        return self.fitness