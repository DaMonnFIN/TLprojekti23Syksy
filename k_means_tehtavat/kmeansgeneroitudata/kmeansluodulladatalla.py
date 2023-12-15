'''
K-means algoritmi luodulla datalla. Algoritmi opetetaan tulkitsemaan kiihtyvyysanturin dataa.

Tavoitteena opettaa algoritmi tunnistamaan kiihtyvyysanturin liikkeet. Kiihtyvyysanturin opetusdata on generoitu tässä vaiheessa.

'''


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import createdata as cd

# värit visualisointiin
otsikko = '#fbedff'
tausta = '#3c7569'


datamaara = 80
kohina = 200
data=cd.createData(datamaara,kohina)
df = pd.DataFrame(data, columns=['x', 'y', 'z'])

# Arvotaan keskipisteet
keskipisteet = cd.centralPointCreation(6, df)
centerPointCumulativeSum = np.zeros((6, 3))
counts = np.zeros((1, 6))
distances = np.zeros((1, 6))

iterations = 10
allCenterPoints = np.zeros((iterations, 6, 3))

# K-means algoritmin aloituskierros
while True:
    nollavoitot = 0

    # Lasketaan etäisyydet keskipisteisiin ja lisätään lähimmän keskipisteen koordinaatit kumulatiiviseen summaan
    for i in range(datamaara):
        for j in range(6):
            distances[0, j] = cd.distance(data[i, :], keskipisteet[j, :])
        nearest = np.argmin(distances)
        centerPointCumulativeSum[nearest, :] += data[i, :]
        counts[0, nearest] += 1

    # Tarkistetaan, paljonko kukin keskipiste sai voittoja. Nollille jääneiden lukumäärä lasketaan.
    for i in range(6):
        if counts[0, i] == 0:
            nollavoitot += 1
    
    # Jos on nollavoittoja, arvotaan uudet keskipisteet nollavoittojen tilalle.
    if nollavoitot > 0:
        for i in range(6):
            if counts[0, i] == 0: # nolla voittoa -> uusi piste
                keskipisteet[i, :] = cd.centralPointCreation(1, df)
            else:
                keskipisteet[i, :] = keskipisteet[i, :] # on voittoja -> sama piste
        counts = np.zeros((1, 6))
        centerPointCumulativeSum = np.zeros((6, 3))
        # laskurit nolliin ja päivitetyillä keskipisteillä uusi kierros niin kauan kun nollavoittoja tulee

    # Kun kaikilla keskipisteillä on voittoja, lasketaan uudet keskipisteet ja siirrytään eteenpäin.
    else:
        for i in range(6):
            keskipisteet[i, :] = centerPointCumulativeSum[i, :] / counts[0, i]
        break


# Aloitetaan visualisointi
fig=plt.figure(1)

# hifistelyä...
fig.set_facecolor(tausta)
fig.suptitle("K-means algoritmi & generoitu data", fontsize=20, color=otsikko,   fontweight='bold')
plt.subplots_adjust(hspace=0.5, wspace=0.5, top=0.85)

# Kuva 1: datapisteet
ax=fig.add_subplot(221, projection='3d', facecolor=tausta, axisbelow=True)
ax.set_title("Datapisteet", color=otsikko,   fontweight='bold', fontsize=15)
ax.scatter(df['x'], df['y'], df['z'], c='#2f0945', marker='o', s=10)
ax.set_xlabel('X', color=otsikko)
ax.set_ylabel('Y', color=otsikko)
ax.set_zlabel('Z', color=otsikko)

# Kuva 2: arvotut keskipisteet
ax=fig.add_subplot(222, projection='3d', facecolor=tausta, axisbelow=True)
ax.set_title("Arvotut keskipisteet", color=otsikko,   fontweight='bold', fontsize=15)
ax.scatter(keskipisteet[:, 0], keskipisteet[:, 1], keskipisteet[:, 2], c='#616e04', marker='o', s=25)
ax.set_xlabel('X', color=otsikko)
ax.set_ylabel('Y', color=otsikko)
ax.set_zlabel('Z', color=otsikko)



# Siirrytään k-means algoritmin toiseen vaiheeseen, jossa lasketaan uudet keskipisteet iterointiloopissa
for iteration in range(iterations):
    # Kerätään keskipisteet talteen visualisointia varten
    allCenterPoints[iteration, :, :] = np.copy(keskipisteet)

    # Lasketaan jälleen etäisyydet keskipisteisiin ja lisätään lähimmän keskipisteen koordinaatit kumulatiiviseen summaan
    for i in range(datamaara):
        for j in range(6):
            distances[0, j] = cd.distance(data[i, :], keskipisteet[j, :])
        nearest = np.argmin(distances)
        centerPointCumulativeSum[nearest, :] += data[i, :]
        counts[0, nearest] += 1

    # Lasketaan uudet keskipisteet   
    for i in range(6):
        keskipisteet[i, :] = centerPointCumulativeSum[i, :] / counts[0, i]


# Jatketaan visualisointi loppuun
# Kuva 3: keskipisteet jokaisella iteraatiokierroksella
ax=fig.add_subplot(223, projection='3d', facecolor=tausta, axisbelow=True)
ax.set_title("Algoritmin keskipisteet", color=otsikko,   fontweight='bold', fontsize=15)
for i in range(iterations):
    ax.scatter(allCenterPoints[i, :, 0], allCenterPoints[i, :, 1], allCenterPoints[i, :, 2], c='#616e04', marker='o', s=10)
ax.set_xlabel('X', color=otsikko)
ax.set_ylabel('Y', color=otsikko)
ax.set_zlabel('Z', color=otsikko)

# Kuva 4: lopulliset keskipisteet
ax=fig.add_subplot(224, projection='3d', facecolor=tausta, axisbelow=True)
ax.set_title("Lopulliset keskipisteet", color=otsikko,   fontweight='bold', fontsize=15)
ax.scatter(keskipisteet[:, 0], keskipisteet[:, 1], keskipisteet[:, 2], c='#2f0945', marker='o', s=25)
ax.set_xlabel('X', color=otsikko)
ax.set_ylabel('Y', color=otsikko)
ax.set_zlabel('Z', color=otsikko)
plt.show()
