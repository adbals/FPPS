import pandas as pd
import matplotlib.pyplot as plt

# Define read file
def read(fileName):
    dirName = "datasetTSP/%s/%s_xy.csv" % (fileName, fileName)
    df = pd.read_csv(dirName, sep=",", usecols =["no","x","y","z"])
    xy = df.values.tolist()
    clist = []
    for item in xy:
        clist.append(item)

    return clist
