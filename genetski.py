import random

from generacija import *

class GA:
    @classmethod
    def sledeca(cls, generacija):
        sledeca_generacija = Generacija(init=False)
        off = 0
        if Globalne.elitizam:
            sledeca_generacija.dodaj_kombinaciju(0,generacija.get_najbolja())
            off = 1

        for i in range(off, Globalne.velicina_generacije):
            p1 = GA.izaberi_roditelja(generacija)
            p2 = GA.izaberi_roditelja(generacija)
            p1.baza_od_ruta()
            p2.baza_od_ruta()
            nova_kombinacija = GA.uparivanje(p1,p2)
            sledeca_generacija.dodaj_kombinaciju(i,nova_kombinacija)

        for i in range(sledeca_generacija.velicina_generacije):
            cls.mutacija(sledeca_generacija.kombinacije[i])

        return sledeca_generacija
    @classmethod
    def izaberi_roditelja(cls,generacija):
        uzorak_generacija = Generacija(velicina_generacije=Globalne.velicina_uzorka, init=False)
        for i in range(Globalne.velicina_uzorka):
            uzorak_generacija.dodaj_kombinaciju(i, generacija.kombinacije[random.randint(0, generacija.velicina_generacije - 1)])
        najbolja = uzorak_generacija.get_najbolja()
        return najbolja
    @classmethod
    def uparivanje(cls,p1,p2):
        dete = Kombinacija()

        indx1 = random.randint(0, Globalne.broj_tacaka -1)
        indx2 = random.randint(0, Globalne.broj_tacaka -1)
        if indx1 > indx2:
            swap = indx2
            indx2 = indx1
            indx1 = swap
        baza = []
        if indx1 != indx2:
            for i in range(indx1, indx2):
                baza.append(p1.baza[i])
        j = 0
        while len(baza) < Globalne.broj_tacaka:
            if(baza.__contains__(p2.baza[j])):
                j += 1
                continue
            else:
                baza.append(p2.baza[j])
                j += 1

        indx = random.randint(0, Globalne.broj_tacaka - 1)
        rob1 = []
        rob2 = []
        rob1.insert(0, Globalne.home1)
        rob2.insert(0, Globalne.home2)
        for i in range(indx):
            rob1.append(baza[i])
        for i in range(indx, Globalne.broj_tacaka):
            rob2.append(baza[i])
        rob1.append(Globalne.home1)
        rob2.append(Globalne.home2)
        dete.dodaj_rutu(0, rob1)
        dete.dodaj_rutu(1,rob2)
        dete.baza_od_ruta()
        return dete
    @classmethod
    def mutacija(cls, kombinacija):
        rob_indx = round(random.random())
        if len(kombinacija.rute[rob_indx]) > 3:

            i1, i2 = random.randint(1, len(kombinacija.rute[rob_indx]) - 2), random.randint(1, len(kombinacija.rute[rob_indx]) - 2)
            while i1 == i2:
                i1, i2 = random.randint(1, len(kombinacija.rute[rob_indx]) - 2), random.randint(1,len(kombinacija.rute[rob_indx]) - 2)
            if random.random() < Globalne.verovatnoca_mutacije:
                swap = []
                swap = kombinacija.rute[rob_indx][i1].copy()
                kombinacija.rute[rob_indx][i1] = kombinacija.rute[rob_indx][i2].copy()
                kombinacija.rute[rob_indx][i2] = swap.copy()
                Globalne.cntr += 1
        return kombinacija