import numpy as np
import pandas as pd
from math import radians,sin,cos,sqrt,asin

def distance_points(point_a,point_b):
    lat1,lon1= point_a
    lat2,lon2= point_b
    R = 6371
    
    dLat = radians(lat2 - lat1)
    dLon = radians(lon2 - lon1)
    lat1 = radians (lat1)
    lat2 = radians (lat2)
    
    a = sin(dLat/2)**2 + cos(radians(lat1))*cos(radians(lat2))*sin(dLon/2)**2
    c = 2*asin(sqrt(a))
    Return R*c*1000
            
def createAdjMatrixFile(fileName):
    dirName = "datasetTSP/%s/%s_xy.txt" % (fileName, fileName)
    data = pd.read_csv(dirName,header = None,  delimiter=r"\s+").as_matrix()
    newMatrix = np.zeros((len(data),len(data)))
    for i in range(len(data)):
        for j in range(len(data)):
            newMatrix[i][j] =distance_points(data[i], data[j])
    saveDir = "datasetTSP/%s/%s_d.txt" % (fileName, fileName)
    np.savetxt(saveDir, newMatrix, delimiter=' ')
