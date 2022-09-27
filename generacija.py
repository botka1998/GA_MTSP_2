from kombinacija import *
class Generacija:
    def __init__(self, velicina_generacije=Globalne.velicina_generacije, init=False):
        self.kombinacije = []
        self.velicina_generacije = velicina_generacije
        if init:
            for i in range(self.velicina_generacije):
                nova_kombinacija = Kombinacija()
                nova_kombinacija.ispuni_random()
                self.kombinacije.append(nova_kombinacija)

    def dodaj_kombinaciju(self, indx, kombinacija):
        nova_kombinacija = Kombinacija()
        nova_kombinacija.dodaj_rutu(0, kombinacija.rute[0])
        nova_kombinacija.dodaj_rutu(1,kombinacija.rute[1])
        nova_kombinacija.baza_od_ruta()
        self.kombinacije.insert(indx,nova_kombinacija)
    def get_najbolja(self):
        najbolja = Kombinacija()
        najbolja.baza = self.kombinacije[0].baza.copy()
        najbolja.dodaj_rutu(0,self.kombinacije[0].rute[0])
        najbolja.dodaj_rutu(1,self.kombinacije[0].rute[1])
        for i in range(self.velicina_generacije):
            if self.kombinacije[i].get_fitness() > najbolja.get_fitness():
                najbolja = self.kombinacije[i]
        return najbolja