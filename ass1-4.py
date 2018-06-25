import sys
import math
try:
	name=input('Which data file do you want to use?')
	with open(name,'r') as f:
		data=f.readlines()
	matrix=[]
	for line in data:
            line=line.replace('R','')
            line=line.replace('(','')
            line=line.replace(')','')
            matrix.append(list(map(int,line.split(','))))
	f.close()
except IOError:
	print('Sorry, there is no such file.')
	sys.exit()
f.close
#print(matrix)
L=matrix
#矩阵长度
callength=[]
for i in range (len(L)):
    callength.append(L[i][0])
    callength.append(L[i][1])
length = max(callength)
#判断是否全0
def ifzero(A):
    result=True
    for i in range(len(A)):
        for j in range(len(A)):
            if A[i][j]!=0:
                result = False
                break
    return result
#矩阵乘法
def matrixmultiple(A,B):
    C=[]
    for i in range(len(A)):
        C.append([])
        for j in range(len(A)):
            C[i].append(0)
            for m in range(len(A)):
                C[i][j]+=A[i][m]*B[m][j]
    return C
            
#初始邻接矩阵
init_matrix=[]
for i in range(length):
    init_matrix.append([])
    for j in range(length):
        init_matrix[i].append(0)
for i in range (len(L)):
    init_matrix[L[i][0]-1][L[i][1]-1]=1
#复制出第一个可达矩阵初始,还有结果矩阵
matrixroute=init_matrix[:]
resultmatrix=init_matrix
#print(matrixroute)
#主程序
while ifzero(matrixroute)== False:
    matrixroute=matrixmultiple(matrixroute,init_matrix)
    for i in range (length):
        for j in range(length):
            if matrixroute[i][j]==1 and init_matrix[i][j]==1:
                resultmatrix[i][j]=0
#print(resultmatrix)
print('The nonredundant facts are:')
L1=[]
for i in range(len(L)):
    if L[i] not in L1:
        L1.append(L[i])
for i in range(len(L1)):
    if resultmatrix[L1[i][0]-1][L1[i][1]-1]==1:
        print (f'R({L1[i][0]},{L1[i][1]})')
