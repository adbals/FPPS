import pandas as pd
import numpy as np

cat_list = []
for i in range(6):
    df = pd.read_csv('lon'+str(i)+'.csv')
    xy = df.values.tolist()
    xy.sort(key=lambda x:x[2])
    index = [round(p[0]) for p in xy]
    print(index)
    cat_list.append(index)

print(cat_list)
