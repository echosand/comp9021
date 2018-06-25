import sys
import math
try:
	name=input('Which data file do you want to use?')
	with open(name,'r') as f:
		data=f.readlines()
	matrix=[]
	for line in data:
		matrix.append(list(map(int,line.split())))
	f.close()
except IOError:
	print('Sorry, there is no such file.')
	sys.exit()
f.close
L=matrix

def ifinside(x,y,l):
    a=False
    for i in range (len(l)):
        if x<max(l[i][0],l[i][2]) and x>min(l[i][0],l[i][2]):
            if y<max(l[i][1],l[i][3]) and y>min(l[i][1],l[i][3]):
                a=True
    return a

def ifonedge(x,y,l):
    a=0
    for i in range(len(l)):
        if y==l[i][1]or y==l[i][3]:
            if x<max(l[i][0],l[i][2]) and x>min(l[i][0],l[i][2]):
                a+=1
        if x==l[i][0]or x==l[i][2]:
            if y<max(l[i][1],l[i][3]) and y>min(l[i][1],l[i][3]):
                a+=1
    if a >1:
        return True
    else:
        return False
primeter=0
ifin0=True
ifin1=True
for i in range(len(L)):
    for j in range (min(L[i][0],L[i][2]),max(L[i][0],L[i][2])):
        x=j
        y=L[i][1]
        if ifinside(x,y,L)==True:
            ifin0=True
        else:
            if ifonedge(x,y,L)==True and ifin0==True:
                primeter+=1
                ifin0=False
            elif ifonedge(x,y,L)==True and ifin0==False:
                ifin0=False
            else:
                primeter+=1
        #print (primeter)
        x=j
        y=L[i][3]
        if ifinside(x,y,L)==True:
            ifin0=True
        else:
            if ifonedge(x,y,L)==True and ifin1==True:
                primeter+=1
                ifin1=False
            elif ifonedge(x,y,L)==True and ifin1==False:
                ifin1=False
            else:
                primeter+=1
        #print (primeter)
ifin0=True
ifin1=True
for m in range(len(L)):
    for n in range (min(L[m][1],L[m][3]),max(L[m][1],L[m][3])):
        x=L[m][0]
        y=n
        if ifinside(x,y,L)==True:
            ifin0=True
        else:
            if ifonedge(x,y,L)==True and ifin0==True:
                primeter+=1
                ifin0=False
            elif ifonedge(x,y,L)==True and ifin0==False:
                ifin0=False
            else:
                primeter+=1
        x=L[m][2]
        y=n
        if ifinside(x,y,L)==True:
            ifin0=True
        else:
            if ifonedge(x,y,L)==True and ifin1==True:
                primeter+=1
                ifin1=False
            elif ifonedge(x,y,L)==True and ifin1==False:
                ifin1=False
            else:
                primeter+=1
        #print (primeter)
print(f'The perimeter is: {primeter}')
