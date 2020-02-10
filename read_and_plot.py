import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

def read_plot(fileName):
    dirName = "datasetTSP/%s/%s_xy.csv" % (fileName, fileName)
    df = pd.read_csv(dirName, sep=",", usecols =["x"])
    df2 = pd.read_csv(dirName, usecols =["y"])
##    x = df.to_numpy()
##    y = df2.to_numpy()
    ax = df.values.tolist()
    ay = df2.values.tolist()
    lx = []
    ly = []
    for sublist in ax: 
        for item in sublist:
            lx.append(item)
    for sublist in ay:
        for item in sublist:
            ly.append(item)

    x = np.asarray(lx)
    y = np.asarray(ly)

    return (x , y)


def rotate_origin_only(x, y, radians):
    """Only rotate a point around the origin (0, 0)."""
    xx = float(x) * math.cos(radians) + float(y) * math.sin(radians)
    yy = -float(x) * math.sin(radians) + float(y) * math.cos(radians)

    return xx, yy

def rotate(x, y, radians, ox, oy):
    qx = ox + math.cos(radians) * (x - ox) + math.sin(radians) * (y - oy)
    qy = oy + -math.sin(radians) * (x - ox) + math.cos(radians) * (y - oy)

    return qx, qy

#Data directory names
dataDir = "datasetTSP"

instanceName = input("\nEnter the TSP directory you would like to approximate: ")
x = (read_plot(instanceName)[0])
y = (read_plot(instanceName)[1])

plt.scatter(x,y)
plt.show()

pi=22/7
degree = float(input("Input degrees: "))
radians = degree*(pi/180)

lxx = []
lyy = []
for i in range (len(x)):
    print(x[i-1],y[i-1])
    (xx,yy) = rotate(x[i-1],y[i-1],radians,x[0],y[0])
    print(xx,yy)
    lxx.append(xx)
    lyy.append(yy)

print (lxx)
print (lyy)



fig = plt.figure()
ax1 = fig.add_subplot(111)

ax1.scatter(x,y,s=1,c='b',marker='s',label="xy")
ax1.scatter(lxx,lyy,s=1,c='r',marker='o',label="transformed")
plt.legend(loc='upper left');
plt.show()

plt.scatter(lxx, lyy)
plt.show()

