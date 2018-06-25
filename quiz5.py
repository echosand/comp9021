import sys
from random import seed, randint


dim = 10
grid = [[None] * dim for _ in range(dim)]

def display_grid():
    for i in range(dim):
        print('   ', ' '.join(str(int(grid[i][j] != 0)) for j in range(dim)))

# Possibly define other functions

try:
    arg_for_seed, density = input('Enter two nonnegative integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, density = int(arg_for_seed), int(density)
    if arg_for_seed < 0 or density < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(arg_for_seed)

# We fill the grid with randomly generated 0s and 1s,
# with for every cell, a probability of 1/(density + 1) to generate a 0.
for i in range(dim):
    for j in range(dim):
        grid[i][j] = int(randint(0, density) != 0)
print('Here is the grid that has been generated:')
display_grid()
#print(grid)
L=grid[:]
#for Q1
def bfs(L,SubL,n):
    color =[]
    a=n
    for i in range (10):
        color.append([])
        for j in range(10):
            color[i].append(0)

    queue=[]
    queue.append(SubL)
    while queue!=[]:
        if L[queue[0][0]][queue[0][1]]==a:
            color[queue[0][0]][queue[0][1]]=1
            #→
            if  queue[0][0]+1<=9 and color[queue[0][0]+1][queue[0][1]]==0:
                if L[queue[0][0]+1][queue[0][1]]==a:
                    queue.append([queue[0][0]+1,queue[0][1]])
                    color[queue[0][0]+1][queue[0][1]]=1
            #↓                 
            if queue[0][1]+1<=9 and color[queue[0][0]][queue[0][1]+1]==0 :
                if L[queue[0][0]][queue[0][1]+1]==a :
                    queue.append([queue[0][0],queue[0][1]+1])
                    color[queue[0][0]][queue[0][1]+1]=1
            #↑
            if  queue[0][0]-1>=0 and color[queue[0][0]-1][queue[0][1]]==0:
                if L[queue[0][0]-1][queue[0][1]]==a :
                    queue.append([queue[0][0]-1,queue[0][1]])
                    color[queue[0][0]-1][queue[0][1]]=1
            #←
            if queue[0][1]-1>=0 and color[queue[0][0]][queue[0][1]-1]==0 :
                if L[queue[0][0]][queue[0][1]-1]==a:
                    queue.append([queue[0][0],queue[0][1]-1])
                    color[queue[0][0]][queue[0][1]-1]=1
            queue.pop(0)

    count =0
    for i in range(10):
        for j in range(10):
            if color[i][j]==1:
                count+=1
    tuple1 = (count,color)
    return tuple1 

#for Q2
#生成一个0101矩阵，和1010矩阵
matrix01=[]
matrix10=[]
for i in range (10):
    matrix01.append([])
    for j in range (10):
        if i%2==0:
            if j %2 ==0:
                matrix01[i].append(0)
            else:
                matrix01[i].append(1)
        if i%2!=0:
            if j %2 ==0:
                matrix01[i].append(1)
            else:
                matrix01[i].append(0)

for i in range (10):
    matrix10.append([])
    for j in range (10):
        if i%2==0:
            if j %2 ==0:
                matrix10[i].append(1)
            else:
                matrix10[i].append(0)
        if i%2!=0:
            if j %2 ==0:
                matrix10[i].append(0)
            else:
                matrix10[i].append(1)
            

a=grid[0][0]
size_of_largest_homogenous_region_from_top_left_corner=bfs(grid,[0,0],a)[0]
path=[]
for i in range (10):
    path.append([])
    for j in range (10):
        path.append(0)

print('The size_of the largest homogenous region from the top left corner is '
      f'{size_of_largest_homogenous_region_from_top_left_corner}.'
     )

max_size_of_region_with_checkers_structure = 0
q2matrix1=[]
q2matrix2=[]
for i in range (10):
    q2matrix1.append([])
    q2matrix2.append([])
    for j in range (10):
        q2matrix1[i].append(0)
        q2matrix2[i].append(0)
for i in range(10):
    for j in range(10):
        if grid[i][j]==matrix01[i][j]:
            q2matrix1[i][j]=1
        else:
            q2matrix2[i][j]=1
def q2(L):
    count1=0
    visit =[]
    for i in range(10):
        for j in range(10):
            if L[i][j]==1:
                #print(f'({i},{j})')
                t=bfs(L,[i,j],1)
                for k in range(10):
                    for l in range(10):
                        if t[1][k][l]==1:
                             L[k][l]=0
                if t[0]>count1:
                    count1=t[0]               
    return count1
                
b=q2(q2matrix1)                
c=q2(q2matrix2)             
                
max_size_of_region_with_checkers_structure=max(b,c)             
            
print('The size of the largest area with a checkers structure is '
      f'{max_size_of_region_with_checkers_structure}.'
     )

