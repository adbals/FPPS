import pandas as pd
import numpy as np
from itertools import accumulate
from matplotlib import pyplot as plt
'''
dataset consist of lat and long
'''
instanceName = input ("File name : ")
dir = "dataset/%s/%s_xy.csv" % (instanceName,instanceName)
ds = pd.read_csv(dir).values.tolist()
# dp = ds.sort_values(by='Latitude',ascending=False).values.tolist()
# dp = ds.sort(reverse=True,key='Latitude')
print("Sorted dataSet")
print(ds)

for (num,item) in enumerate(ds):
    print(num+1,item)

'''
Transform data into half completed matrix
'''
length_to_split = [11, 11, 10, 10, 9, 9]

# Using islice
dz = [ds[x - y: x] for x, y in zip(
          accumulate(length_to_split), length_to_split)]

print(type(dz))

'''
Add zeros to create mxn matrix
'''
length = max(map(len, dz))
y=[xi+[0]*(length-len(xi)) for xi in dz]
print("Test")
print(type(y))

'''
zig zag Algorithm
'''
def zigzag(row,col,a):
    evenRow = 0
    oddRow = 1
    index = []
    while evenRow < row:
        for i in range(col):
            x = (a[evenRow][i])
            index.append(x)
        evenRow = evenRow + 2

        if oddRow < row:
            for i in range(col - 1, -1, -1):
                x = (a[oddRow][i])
                index.append(x)
        oddRow = oddRow + 2
    return (index)


print("waypoint")
wp =zigzag(6 , 11 , y)
print(wp) #zigzag pattern including zeros

'''
Remove zeros from list and create mission.txt File
'''

nwp=np.array([x for x in wp if x != 0])
print('final list')
print(nwp)

def waypoint (gps_points,instanceName):
    print('Get home location')
    lat = input("Enter Latitude: ")
    long = input("Enter Longitude: ")
    alt = input("Enter Alt:")
    print ('\nGet Mission Parameters')
    hgt = input("Enter Mission Height:")
    spraytime = input('Enter Spray Time:')
    flow = input('Enter flow rate (%): ')

    flow1 = 1100 + (int(flow)*8)

    # Function to write mission file with cooordinates

    def mission_writing():
        x = 3*i+1
        y = 3*i+2
        z = 3*i+3
        file.write ('\n'+str(x)+'\t0\t10\t16\t1\t0\t0\t0\t'+str(gps_points[i, 0])+'\t'+str(gps_points[i, 1])+'\t'+str(hgt)+'\t1\n'+str(y)+'\t0\t10\t184\t9\t'+str(int(flow1))+'\t1\t'+str((int(spraytime)*2))+'	0	0	0	1')
        file.write ('\n'+str(z)+'\t0\t10\t93\t'+str(spraytime)+'\t0\t0\t0\t0\t0\t0\t1')

    # Write
    file = open("dataset/%s/%s_mission.txt"%(instanceName,instanceName),"w")
    file.write ('QGC WPL 110\n0	1	0	16	0	0	0	0\t'+str(lat)+'\t'+str(long)+'\t'+str(alt)+'\t1')

    nrows = len(gps_points)

    for i in range(nrows):
        mission_writing()
    print('Mission written as dataset/%s/%s_mission.txt'%(instanceName,instanceName))
    file.close()

wps = waypoint(nwp,instanceName)
