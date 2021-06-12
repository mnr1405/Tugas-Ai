import random
import numpy as np
import math
import copy



def genKrom(iskrom):
    kromosom = []
    for i in range(iskrom):
        kromosom.append(random.randint(0,9))

    return kromosom


def genPop(ispop):
    populasi = []
    for i in range(ispop):
        populasi.append(genKrom(8))

    return populasi

def dcodekrom(kromosom):
    x1 = -1 + (3 / (9 * (10**-1 + 10**-2 + 10**-3 + 10**-4))) * \
        ((kromosom[0]*10**-1)+(kromosom[1]*10**-2) +
         (kromosom[2]*10**-3)+(kromosom[3]*10**-4))
    x2 = -1 + (2 / (9 * (10**-1 + 10**-2 + 10**-3 + 10**-4))) * \
        ((kromosom[4]*10**-1)+(kromosom[5]*10**-2) +
         (kromosom[6]*10**-3)+(kromosom[7]*10**-4))
    
    return[x1,x2]
def hitfitness(krom):
    nilaifit= dcodekrom(krom)
    hasil= 1 / (math.cos(nilaifit[0])) * (math.sin(nilaifit[1])) - (nilaifit[0] / (nilaifit[1] ** + 1)) + 0.2
    return hasil

def hitfitnessall(populasi, ispop, ):
    fitness_all = []
    for i in range(ispop):
        d = populasi[i]
        fitness = hitfitness(populasi[i])
        fitness_all.append(fitness)

    return fitness_all
    
    return all

def TurneySelection(populasi, istour, ispop):
    kromosom_terbaik = []
    for i in range(0, istour-1):
        kromosom = populasi[random.randint(0, ispop-1)]
        if (kromosom_terbaik == [] or hitfitness(kromosom) > hitfitness(kromosom_terbaik)):
            kromosom_terbaik = kromosom
    return kromosom_terbaik

def crossover(parent1, parent2, probc):

    x = random.random()
    if(x <= probc):
        point1 = random.randint(0, 7)
        point2 = random.randint(0, 7)
        for i in range(point1+1, point2-1):
            parent1[i], parent2[i] = parent2[i], parent1[i]

    return parent1, parent2

def mutasi(parent1, parent2, probm):
    x = random.random()
    if (x <= probm):
        parent1[random.randint(0, 7)] = random.randint(0, 9)
        parent2[random.randint(0, 7)] = random.randint(0, 9)
    return parent1, parent2


def getElitisme(ispop, fitall):
    fitall.sort()
    return fitall.index(max(fitall))
    
ispop= 50
istour= 5
probc= 0.8
probm= 0.5
generasi= 20

populasi = genPop(ispop)
print("Populasi: ", populasi)
for i in range(generasi):
    # print("i: ", i)
    fitness = hitfitnessall(populasi, ispop)
    #print("Fitness: ", fitness)
    new_populasi = []

    best = getElitisme(ispop, fitness)
    print("Best:", best)
    if(ispop % 2 != 0):
        new_populasi.append(populasi[best])
    else:
        new_populasi.append(populasi[best])
        new_populasi.append(populasi[best-1])
    #print("1: ",new_populasi)
    # new_populasi.append(populasi[best])
    #print("2: ",new_populasi)

    j = 0
    while (j < ispop-1):
        #print("j: ", j)
        # parent1 = TurneySelection(populasi, istour, ispop)
        # parent2 = TurneySelection(populasi, istour, ispop)
        parent1 = TurneySelection(populasi, istour, ispop)
        parent2 = TurneySelection(populasi, istour, ispop)
        while (parent1 == parent2):
            parent2 = TurneySelection(populasi, istour, ispop)
        # print("Parent1: ", parent1)
        # print("Parent2: ", parent2)
        ortu1 = copy.deepcopy(parent1)
        ortu2 = copy.deepcopy(parent2)
        # par1 = populasi[parent1]
        # par2 = populasi[parent2]
        children = crossover(ortu1,ortu2,probc)
        children = mutasi(children[0], children[1], probm)
        # print(children)
        new_populasi += children
        j += 2
    populasi = new_populasi
    # x = len(populasi)
    # print("Jumlah populasi setelah mutasi: ", x)
    #print("populasi: ",populasi)
fitness = hitfitnessall(populasi, ispop)
result = getElitisme(ispop, fitness)

print('           Output')
print()
print('Kromosom terbaik:', populasi[result])
print('Hasil decode    :', dcodekrom(populasi[result]))