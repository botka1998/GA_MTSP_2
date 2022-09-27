# This is a sample Python script.
import sys
from pyquaternion import Quaternion

from genetski import *
import json
import abb
import time
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import matplotlib.pyplot as plt
def init_robots(config: json):
    rob_dict = {}

    for robot in config["robots"]:
        name = robot["name"]
        ip = robot["ip"]
        port = robot["port"]
        toolData = robot["tool_data"]
        wobj = robot["wobj"]

        newRobot = abb.Robot(
            ip=ip,
            port_motion=port,
            port_logger=port + 1
        )

        newRobot.set_tool(toolData)
        newRobot.set_workobject(wobj)

        rob_dict[name] = newRobot
        time.sleep(1)
    return rob_dict

def is_reachable(target):
    is_reachable = True
    x, y, z = target[0]
    odgovor = ""
    odgovor = str(robots["ROB1"].isReachable(x, y, z))
    if odgovor == "False":
        is_reachable = False
    odgovor = ""
    odgovor = str(robots["ROB2"].isReachable(x, y, z))
    if odgovor == "False":
        is_reachable = False

    return is_reachable

def ukloni_nedohvatljive():
    cntr = 0
    i = 0
    while i < len(Globalne.lista_targeta):
        if not (is_reachable(Globalne.lista_targeta[i])):
            Globalne.lista_targeta.pop(i)
            Globalne.broj_tacaka -= 1
            cntr += 1
        i += 1
    return cntr
def plott(ruta):
    ruta1 = ruta[0]
    ruta2 = ruta[1]
    pre = ruta1[0][0]
    for i in range(len(ruta1)):
        tacka = ruta1[i][0]
        plt.scatter(tacka[0],tacka[1])
        plt.plot([pre[0],tacka[0]], [pre[1],tacka[1]])
        pre = tacka
    pre = ruta2[0][0]
    for i in range(len(ruta2)):
        tacka = ruta2[i][0]
        plt.scatter(tacka[0],tacka[1])
        plt.plot([pre[0],tacka[0]], [pre[1],tacka[1]])
        pre = tacka
    plt.show()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    file = open("config.json")
    config_json = json.load(file)
    robots = init_robots(config_json)
    robots["ROB1"].set_speed(speed=[Globalne.v1, 200, 200, 200])
    robots["ROB2"].set_speed(speed=[Globalne.v2, 200, 200, 200])
    robots["ROB1"].set_workobject(work_obj=Globalne.wobj)
    robots["ROB2"].set_workobject(work_obj=Globalne.wobj)
    robots["ROB1"].set_tool(tool=[[0, 0, 100], [1, 0, 0, 0]])
    robots["ROB2"].set_tool(tool=[[0, 0, 100], [1, 0, 0, 0]])


    print("Uklonjeno je {} tačaka iz optimizacije".format(ukloni_nedohvatljive()))
    start = time.time()
    top_resenja = []
    gen = Generacija(init=True)
    globalno_resenje = gen.get_najbolja()
    y_osa = []
    x_osa = []

    for i in range(Globalne.broj_generacija):
        gen = GA.sledeca(gen)
        lokalno = gen.get_najbolja()
        if lokalno.fitness > globalno_resenje.fitness:
            globalno_resenje = lokalno
            top_resenja.append(lokalno)
            #print(globalno_resenje.fitness)
        y_osa.append(lokalno.fitness)
        x_osa.append(i)
    end = time.time()
    print("vreme optimizacije: {}".format(end-start))
    print("\n")
    print(globalno_resenje.fitness)
    
    
    #izvuci targete rob1
    rob1_targets = globalno_resenje.rute[0].copy()
    #izvuci targete rob2
    rob2_targets = globalno_resenje.rute[1].copy()
    #iscrtaj resenje
    plt.plot(x_osa, y_osa, 'r-')
    plt.show()
    plott(globalno_resenje.rute)
    #pocetna pozicija
    robots["ROB1"].set_cartesian(Globalne.home1)
    robots["ROB2"].set_cartesian(Globalne.home2)
    time.sleep(2)
    
    if len(rob1_targets) > 2:
        for i in range(len(rob1_targets)):
            robots["ROB1"].set_cartesian(rob1_targets[i])

    if len(rob2_targets) > 2:
        for i in range(len(rob2_targets)):
            robots["ROB2"].set_cartesian(rob2_targets[i])


    '''
    for i in range(len(top_resenja)):
        rob1_targets = top_resenja[i].rute[0]
        rob2_targets = top_resenja[i].rute[1]
        if len(rob1_targets) > 2:
            for i in range(len(rob1_targets)):
                robots["ROB1"].set_cartesian(rob1_targets[i])
        if len(rob2_targets) > 2:
            for i in range(len(rob2_targets)):
                robots["ROB2"].set_cartesian(rob2_targets[i])
        plott(top_resenja[i].rute)
    '''
    sys.exit()