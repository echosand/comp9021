from random import seed, randint
import sys
from collections import defaultdict


def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(int(grid[i][j] != 0)) for j in range(len(grid))))


def judge(L,size):
    #建矩阵记录[size,count]
    z=True
    count1 = []
    count=[]
    for l in range (size):
        count1.append([])
        for m in range (2):
            count1[l].append(0)
    #标记是否当过三角顶点矩阵
    L_record=[]
    for i in range(len(L)):
        L_record.append([])
        for j in range (len(L[i])):
            L_record[i].append(0)
            
    for i in range(len(L)):
        for j in range(len(L[i])):
            #每个点形成size为s的三角形
            for s in range (size,1,-1):
                count1[s-1][0]=s
                #检测三角形每行是否含0
                for k in range (s,1,-1):
                    if j+k-1< len(L) and i+k-1 < len(L) and L[i][j]!=0:
                        if i+k-1>=0 and j-k+1>=0 and L_record[i][j] == 0:
                            if 0 in (L[i+k-1][j-k+1:j+k]):
                                z=False
                                break
                            else:
                                z= True
                        else:
                            z=False
                            break
                    else:
                        z=False
                        break
                if z==True:
                    L_record[i][j]=1
                    count1[s-1][1]+=1
                    #print (L_record)
    #倒序排列一下
    for l in range(len(count1)):
        count.append(count1[len(count1)-l-1])
    length=len(count)
    #print(count)
    #删除所有0个的三角形元素
    for y in range(len(count)-1,-1,-1):
        if count[y][1]==0:
            count.remove(count[y])
    #由于老师自动删除最后一个元素，因此补0,0
    count.append([0,0])
    return count
    # Replace return {} above with your code

# Possibly define other functions

#矩阵转置
def transfer(L):
    L_transfer=[]
    for i in range(len(L)):
        L_transfer.append([])
        for j in range (len(L[i])):
            L_transfer[i].append(0)
    for k in range(len(L)):
        for l in range (len(L[k])):
            L_transfer[len(L)-1-k][l]=L[l][k]
    return L_transfer

#建立字典
def triangles_in_grid(list,size):
    dictionary={}
    gridE= transfer(grid)
    gridS= transfer(gridE)
    gridW= transfer(gridS)
    dictionary={'N':judge(grid,size)[:-1],'E':judge(gridE,size)[:-1],'S':judge(gridS,size)[:-1],'W':judge(gridW,size)[:-1]};
    if judge(gridS,size)[:-1] ==[]:
        del dictionary['S']
    if judge(grid,size)[:-1] ==[]:
        del dictionary['N']
    if judge(gridE,size)[:-1] ==[]:
        del dictionary['E']
    if judge(gridW,size)[:-1] ==[]:
        del dictionary['W']
   
    return dictionary

#主程序
try:
    arg_for_seed, density, dim = input('Enter three nonnegative integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, density, dim = int(arg_for_seed), int(density), int(dim)
    if arg_for_seed < 0 or density < 0 or dim < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(arg_for_seed)
grid = [[randint(0, density) for _ in range(dim)] for _ in range(dim)]
print('Here is the grid that has been generated:')
display_grid()

#设定size
length=len(grid)
if length % 2 == 0:
    size = length // 2
else:
    size = (length +1)//2


# A dictionary whose keys are amongst 'N', 'E', 'S' and 'W',
# and whose values are pairs of the form (size, number_of_triangles_of_that_size),
# ordered from largest to smallest size.

triangles = triangles_in_grid(grid,size)
for direction in sorted(triangles, key = lambda x: 'NESW'.index(x)):
    print(f'\nFor triangles pointing {direction}, we have:')
    for size, nb_of_triangles in triangles[direction]:
        triangle_or_triangles = 'triangle' if nb_of_triangles == 1 else 'triangles'
        print(f'     {nb_of_triangles} {triangle_or_triangles} of size {size}')
