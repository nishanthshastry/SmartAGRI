import csv
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
           a=a+float(row[5])
        if row[0]=="COTTON":
           b=b+float(row[5])
        if row[0]=="GRAM":
           c=c+float(row[5])
        if row[0]=="GROUNDNUT":
           d=d+float(row[5])
        if row[0]=="MAIZE":
           e=e+float(row[5])
        if row[0]=="MOONG":
           f=f+float(row[5])
        if row[0]=="PADDY":
           g=g+float(row[5])
        if row[0]=="RAPESEED":
           h=h+float(row[5])
        if row[0]=="SUGARCANE":
           i=i+float(row[5])
        if row[0]=="WHEAT":
           j=j+float(row[5])
        
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

import matplotlib.pyplot as plt

# Data to plot
labels = 'ARHAR', 'COTTON', 'GRAM', 'GROUNDNUT', 'MAIZE', 'MOONG','PADDY','RAPESEED','SUGARCANE','WHEAT'
sizes = [a1,b1,c1,d1,e1,f1,g1,h1,i1,j1]
colors = ['Blue', 'Red','Orange','Green','Brown','Yellow','Grey','White','Pink','Black']

# Plot
plt.pie(sizes, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.show()