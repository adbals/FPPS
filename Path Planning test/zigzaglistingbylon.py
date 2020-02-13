import pandas as pd
import numpy as np
import zigzag as zg
from ReadCSV import read
import matplotlib.pyplot as plt

# Get coordinate list
dataDir = "datasetTSP"

Name = input("\nEnter the TSP directory you would like to approximate: ")

clist = read(Name)

# 
cat_list = []
len_list = []
for i in range(6):
    df = pd.read_csv('lon'+str(i)+'.csv',header=None)
    xy = df.values.tolist()
    xy.sort(key=lambda x:x[1])
    n = len(xy)
    index = [round(p[0]) for p in xy]
    cat_list.append(index)
    len_list.append(n)

length = max(len_list)
y = [ xi+[0]*(length - len(xi)) for xi in cat_list]

print(y)


zzlist = zg.zigzag(6,length,y)

while(i<len(zzlist)):
	if(zzlist[i]==0):
		zzlist.remove (zzlist[i])
		# as an element is removed	
		# so decrease the length by 1	
		length = length -1  
		# run loop again to check element							
		# at same index, when item removed 
		# next item will shift to the left 
		continue
	i = i+1
	
zzlist = [x - 1 for x in zzlist]
print(zzlist)


# Arrange original list
arr = np.array(clist)
path = arr[zzlist]

print(path)
# Plot and compare
list1 = path.tolist()
x = [p[1] for p in list1]
y = [p[2] for p in list1]

fig = plt.figure()
ax1 = fig.add_subplot(111)

ax1.plot(x,y,'bo-',marker='s',label="xy")
plt.legend(loc='upper left');
#plt.grid(True)
plt.show()

