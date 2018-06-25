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
#print (matrix)

#二分法算法
def divide(A,B):
	minvalue=min(B)
	maxvalue=max(B)
	target=(sum(B))//len(B)
	C=B[:]
	minus=0
	while C[len(C)-1]!=target:
		C=B[:]
		for i in range(len(A)):
			if i < len(C)-1:
				C[i]-= minus
				minus=target - C[i]+abs(A[i+1]-A[i])
			if i==len(C)-1:
				C[i]=C[i]-minus
				minus=0
		if C[len(C)-1] > target:
			minvalue=target
			if target !=(maxvalue+minvalue)//2:
				target=(maxvalue+minvalue)//2
			else:
				break
		if C[len(C)-1]< target:
			maxvalue = target
			if target !=(maxvalue+minvalue)//2:
				target= (maxvalue+minvalue)//2
			else:
				break
	return target
		
				

#主程序
#按照距离大小进行排序
matrix=sorted(matrix,key=lambda matrix:matrix[0])
#print(matrix)
distance = []
weight = []
for i in range(len(matrix)):
	distance.append(matrix[i][0])
	weight.append(matrix[i][1])
#print(distance,weight)
print(f'The maximum quantity of fish that each town can have is {divide(distance,weight)}.')
