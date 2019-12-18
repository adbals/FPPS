#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 11:14:04 2019

@author: adib
"""
from functools import partial
import adjMatrix as adj
import numpy as np
import matplotlib.pyplot as plt

def nearest(point,more_points):
    distance_to_point = partial(adj.distance_points,point)
    return min(more_points,key = distance_to_point)    

def waypoint (gps_points,instanceName):
    print('Get home location')
    lat = input("Enter Latitude: ")
    long = input("Enter Longitude: ")
    alt = input("Enter Alt:")
    print ('\nGet Mission Parameters')
    hgt = input("Enter Mission Height:")
    spraytime = input('Enter Spray Time:')
    
    init_coord = [float(x) for x in [lat,long]]
    n= nearest(init_coord,gps_points).tolist()
    
    # Sort file according to nearest point to Home 
    d = gps_points.tolist()
    m = d.index(n)
    k = np.split(gps_points,(m,len(gps_points)))[1]
    l = np.split(gps_points,(m,len(gps_points)))[0]
    gpss_points = np.vstack((k,l))
                    
    #Visualize Path
    x=[]
    y=[]
    for row in gpss_points:
        x.append(float(row[1]))
        y.append(float(row[0]))
    arrow_properties = dict(facecolor = 'black',width= 0.005,headwidth = 0.1,shrink=0.1)
    plt.annotate('Start here',xy= (x[0],y[0]),arrowprops=arrow_properties)  
    plt.plot(x,y,marker='o',label= 'line1',color='k')
    # Function to write mission file with cooordinates

    def mission_writing():
        x = 3*i+1
        y = 3*i+2
        z = 3*i+3
        file.write ('\n'+str(x)+'\t0\t3\t16\t1\t0\t0\t0\t'+str(gpss_points[i, 0])+'\t'+str(gpss_points[i, 1])+'\t'+str(hgt)+'\t1\n'+str(y)+'\t0\t3\t184\t9\t1900\t1\t'+str((int(spraytime)*2))+'	0	0	0	1')
        file.write ('\n'+str(z)+'\t0\t3\t93\t'+str(spraytime)+'\t0\t0\t0\t0\t0\t0\t1')

    # Write
    file = open("%s/%s_mission.txt"%(instanceName,instanceName),"w")
    file.write ('QGC WPL 110\n0	1	0	16	0	0	0	0\t'+str(lat)+'\t'+str(long)+'\t'+str(alt)+'\t1')

    nrows = len(gpss_points)

    for i in range(nrows):
        mission_writing()
    print('Mission written as %s/%s_mission.txt'%(instanceName,instanceName))
    file.close()
