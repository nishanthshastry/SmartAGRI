import numpy as np
import pandas as pd
import csv
df=pd.read_csv("datafile1.csv")
a=0
b=0
c=0
d=0
e=0
f=0
g=0
h=0
i=0
j=0
with open('datafile1.csv') as z:
    reader = csv.reader(z)
    arr=[]
    for row in reader:
        if row[0]=="ARHAR":
           a=a+float(row[4])
        if row[0]=="COTTON":
           b=b+float(row[4])
        if row[0]=="GRAM":
           c=c+float(row[4])
        if row[0]=="GROUNDNUT":
           d=d+float(row[4])
        if row[0]=="MAIZE":
           e=e+float(row[4])
        if row[0]=="MOONG":
           f=f+float(row[4])
        if row[0]=="PADDY":
           g=g+float(row[4])
        if row[0]=="RAPESEED":
           h=h+float(row[4])
        if row[0]=="SUGARCANE":
           i=i+float(row[4])
        if row[0]=="WHEAT":
           j=j+float(row[4])

a1=int(a)
b1=int(b)
c1=int(c)
d1=int(d)
e1=int(e)
f1=int(f)
g1=int(g)
h1=int(h)
i1=int(i)
j1=int(j)

import matplotlib.pyplot as plt; 

x=[1,2,3,4,5,6,7,8,9,10]
height=[a1,b1,c1,d1,e1,f1,g1,h1,i1,j1]
labels = ['ARHAR', 'COTTON', 'GRAM', 'GROUNDNUT', 'MAIZE', 'MOONG','PADDY','RAPESEED','SUGARCANE','WHEAT']

plt.bar(x, height, align='center', width=0.5)
plt.xticks(x, labels,rotation =65)
plt.title('Crops vs Cost')
plt.xlabel('Crops')
plt.ylabel('Cost of Cultivation (`/Hectare) C2')

plt.show()