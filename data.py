import numpy as np
import csv

dataSheet = []
dataA = []
dataB = []
dataC = []
dataD = []
dataE = []
dataF = []
dataG = []
ProbabilityA = []
ProbabilityB = []
ProbabilityC = []
ProbabilityD = []
ProbabilityE = []
ProbabilityF = []
ProbabilityG = []

with open('probabilityDistribution.csv', 'r+') as f:
    fr = csv.reader(f)
    i = 0
    for row in fr:
        i += 1
        if i < 15:
            dataA.append(int(row[0]))
            ProbabilityA.append(float(row[1][:-1])/100)
        elif i < 37:
            dataB.append(int(row[0]))
            ProbabilityB.append(float(row[1][:-1])/100)
        elif i < 66:
            dataC.append(int(row[0]))
            ProbabilityC.append(float(row[1][:-1])/100)
        elif i < 93:
            dataD.append(int(row[0]))
            ProbabilityD.append(float(row[1][:-1])/100)
        elif i < 119:
            dataE.append(int(row[0]))
            ProbabilityE.append(float(row[1][:-1])/100)
        elif i < 141:
            dataF.append(int(row[0]))
            ProbabilityF.append(float(row[1][:-1])/100)
        else:
            dataG.append(int(row[0]))
            ProbabilityG.append(float(row[1][:-1])/100)


while True:
    A = np.random.choice(np.asarray(dataA),p = ProbabilityA)
    B = np.random.choice(np.asarray(dataB),p = ProbabilityB)
    if B <= A:
        continue
    C = np.random.choice(np.asarray(dataC), p=ProbabilityC)
    if C <= B:
        continue
    D = np.random.choice(np.asarray(dataD), p=ProbabilityD)
    if D <= C:
        continue
    E = np.random.choice(np.asarray(dataE), p=ProbabilityE)
    if E <= D:
        continue
    F = np.random.choice(np.asarray(dataF), p=ProbabilityF)
    if F <= E:
        continue
    G = np.random.choice(np.asarray(dataG), p=ProbabilityG)
    if G <= F:
        continue

    newRow = [A,B,C,D,E,F,G]

    if newRow in dataSheet:
        continue

    npRow = np.asarray(newRow)

    if npRow.sum() < 138 or npRow.sum() > 210:
        continue

    if npRow.mean() < 20 or npRow.mean() >30:
        continue

    if newRow[6] - newRow[0] < 30 or newRow[6] - newRow[0] > 44:
        continue

    rowRoot = np.power(npRow, 1./7)

    if np.prod(rowRoot) < 10.54 or np.prod(rowRoot) > 25.18:
        continue

    if npRow.std() < 11.0001 and npRow.std() > 16.0001:
        continue

    dataSheet.append(newRow)

    if len(dataSheet) == 2000:
        break

with open('Result.csv', 'w+') as f:
    fw = csv.writer(f)
    for rw in dataSheet:
        fw.writerow(rw)