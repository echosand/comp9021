import sys
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


#形成一个全0数组存放计算过程
lengthmatrix=[]
for k in range (len(matrix)):
    lengthmatrix.append([])
    for n in range(len(matrix[k])):
        lengthmatrix[k].append(0)

#计算最大sum
#定位行
for l in range (len(matrix)-1,-1,-1):
    #定位列
    for m in range(len(matrix[l])):
        #如果l是最后一行
        if l ==len(matrix)-1:
            lengthmatrix[l][m] = matrix[l][m]
        #其余情况
        if l < len(matrix)-1:
            lengthmatrix[l][m]=max(lengthmatrix[l+1][m],lengthmatrix[l+1][m+1])+matrix[l][m]
print (f'The largest sum is: {lengthmatrix[0][0]}')


#全0数组存放路径
path_count=[]
for q in range (len(lengthmatrix)):
    path_count.append([])
    for r in range(len(lengthmatrix[q])):
        path_count[q].append(0)

#计算路径数目
#定位行
for o in range (len(lengthmatrix)-1,-1,-1):
    #定位列
    for p in range (len(lengthmatrix[o])):
        #若为最后一排，则路径记为1条
        if o == len(lengthmatrix)-1:
            path_count[o][p]=1
        #其余情况
        if o < len(lengthmatrix)-1:
            if lengthmatrix[o+1][p] == lengthmatrix[o+1][p+1]:
                path_count[o][p] = path_count[o+1][p] + path_count[o+1][p+1]
            if lengthmatrix[o+1][p] > lengthmatrix[o+1][p+1]:
                path_count[o][p] = path_count[o+1][p]
            if lengthmatrix[o+1][p] < lengthmatrix[o+1][p+1]:
                path_count[o][p] = path_count[o+1][p+1]
print (f'The number of paths yielding this sum is: {path_count[0][0]}')

#leftmost
leftmost=[]
for u in range(len(lengthmatrix)):
    leftmost.append(0)


index = 0
for s in range(len(lengthmatrix)):
        if s == 0:
            leftmost[s]=matrix[s][0]
        if s > 0:
            if lengthmatrix[s][index+1]>lengthmatrix[s][index]:
                leftmost[s]=matrix[s][index+1]
            else:
                leftmost[s]=matrix[s][index]
        index = matrix[s].index(leftmost[s])
print (f'The leftmost path yielding this sum is: {leftmost}')
