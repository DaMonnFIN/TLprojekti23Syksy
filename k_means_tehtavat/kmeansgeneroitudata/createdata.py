import numpy as np


def createData(lkm, k):
    h = 1000                                                    # korkeat arvot   
    l = 500                                                     # matalat arvot
    data = np.zeros((lkm, 3))
    data[0:lkm//6, :] = np.array([h, l, l])                     # x ylös, muut alas
    data[lkm//6:lkm//3, :] = np.array([l, h, h])                # x alas, muut ylös
    data[lkm//3:lkm//2, :] = np.array([l, h, l])                # y ylös, muut alas
    data[lkm//2:2*lkm//3, :] = np.array([h, l, h])              # y alas, muut ylös
    data[2*lkm//3:5*lkm//6, :] = np.array([l, l, h])            # z ylös, muut alas
    data[5*lkm//6:lkm, :] = np.array([h, h, l])                 # z alas, muut ylös
    data = data+np.random.rand(lkm, 3)*k                        # lisätään kohinaa
    return data


def centralPointCreation(lkm, df):
    keskipisteet = np.zeros((lkm, 3))
    # arvotaan keskipisteet
    keskipisteet[:, 0] = np.random.rand(lkm) * df['x'].max()
    keskipisteet[:, 1] = np.random.rand(lkm) * df['y'].max()
    keskipisteet[:, 2] = np.random.rand(lkm) * df['z'].max()
    return keskipisteet

def distance(point1, point2):
    return np.linalg.norm(point1 - point2)


