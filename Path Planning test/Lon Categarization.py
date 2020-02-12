from ReadCSV import read
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import math

# Get coordinate list
dataDir = "datasetTSP"

Name = input("\nEnter the TSP directory you would like to approximate: ")

clist = read(Name)

# Get long list
N = len(clist)

lon_list = []
for i in range (N):
    y = (clist[i][2])
    lon_list.append(y)

lowest_lon = min(lon_list)
highest_lon = max(lon_list)

dLon = round(highest_lon-lowest_lon,5)

print(dLon)


# Cal layer difference
NL = round((dLon/6),5)
print(NL)
# Classify by lon layer
layerlist = []
for j in range(6):
    layer = [k for k in lon_list if lowest_lon+(j*NL) <= k <= (lowest_lon+((j+1)*NL))]
    layerlist.append(layer)

corrected_list = {}
for a in range(len(layerlist)):
    item = []
    for b in range(N):
        if lon_list[b] in (layerlist[a]):
            item.append(clist[b])
    corrected_list[a] = item
    finallist = np.array(item)
    np.savetxt("lon"+str(a)+".csv", finallist, delimiter=",")

f0 = corrected_list[0]
f1 = corrected_list[1]
f2 = corrected_list[2]
f3 = corrected_list[3]
f4 = corrected_list[4]
f5 = corrected_list[5]

def listing(list1):
    x = [p[1] for p in list1]
    y = [p[2] for p in list1]

    return x , y

x0 = listing(f0)[0]
y0 = listing(f0)[1]
x1 = listing(f1)[0]
y1 = listing(f1)[1]
x2 = listing(f2)[0]
y2 = listing(f2)[1]
x3 = listing(f3)[0]
y3 = listing(f3)[1]
x4 = listing(f4)[0]
y4 = listing(f4)[1]
x5 = listing(f5)[0]
y5 = listing(f5)[1]
  
fig = plt.figure()
ax = fig.add_subplot(111)

ax.plot(x0,y0,'bo-',label='G1')
ax.plot(x1,y1,'ro-',label='G2')
ax.plot(x2,y2,'go-',label='G3')
ax.plot(x3,y3,'co-',label='G4')
ax.plot(x4,y4,'mo-',label='G5')
ax.plot(x5,y5,'yo-',label='G6')

plt.legend(loc='upper left');
plt.grid(True)
plt.show()
