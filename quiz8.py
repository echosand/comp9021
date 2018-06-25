import sys
from random import seed, randrange

from queue_adt import *


def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(grid[i][j]) for j in range(len(grid[0]))))

def leftmost_longest_path_from_top_left_corner(L,root):
    queue=Queue()
    length=len(L)
    path=None
    if L[root[0]][root[1]]==0:
        return path
    pathrecord=[tuple(root)]
    if L[1][0]!=0:
        #print(L[1][0])
        queue.enqueue([[(0,0),(1,0)],2])
    if L[0][1]!=0:
        #print(L[0][1])
        queue.enqueue([[(0,0),(0,1)],1])
    while not queue.is_empty():
        item=queue.dequeue()
        path=item[0]
        direct=item[1]
        n=len(path)
        if n>=len(pathrecord):
            pathrecord=path
        #print(item)
        node=path[-1]
        if direct==0:
            if node[1]+1<length  and (node[0],node[1]+1) not in path and L[node[0]][node[1]+1]==1:
                path.append((node[0],node[1]+1))
                queue.enqueue([path,1])
                path=path[:-1]
            if node[0]-1>=0 and (node[0]-1,node[1]) not in path and L[node[0]-1][node[1]]==1:
                path.append((node[0]-1,node[1]))
                queue.enqueue([path,0])
                path=path[:-1]
            if node[1]-1>=0 and (node[0],node[1]-1) not in path  and L[node[0]][node[1]-1]==1:
                path.append((node[0],node[1]-1))
                queue.enqueue([path,3])
                path=path[:-1]
        if direct==1:
            if node[0]+1<length  and (node[0]+1,node[1]) not in path and L[node[0]+1][node[1]]==1:
                path.append((node[0]+1,node[1]))
                queue.enqueue([path,2])
                path=path[:-1]
            if node[1]+1<length and (node[0],node[1]+1) not in path  and L[node[0]][node[1]+1]==1:
                path.append((node[0],node[1]+1))
                queue.enqueue([path,1])
                path=path[:-1]
            if node[0]-1>=0 and (node[0]-1,node[1]) not in path and L[node[0]-1][node[1]]==1:
                path.append((node[0]-1,node[1]))
                queue.enqueue([path,0])
                path=path[:-1]
        if direct==2:
            if node[1]-1>=0 and (node[0],node[1]-1) not in path  and L[node[0]][node[1]-1]==1:
                path.append((node[0],node[1]-1))
                queue.enqueue([path,3])
                path=path[:-1]
            if node[0]+1<length  and (node[0]+1,node[1]) not in path and L[node[0]+1][node[1]]==1:
                path.append((node[0]+1,node[1]))
                queue.enqueue([path,2])
                path=path[:-1]
            if node[1]+1<length  and (node[0],node[1]+1) not in path and L[node[0]][node[1]+1]==1:
                path.append((node[0],node[1]+1))
                queue.enqueue([path,1])
                path=path[:-1]
        if direct==3:
            if node[0]-1>=0 and (node[0]-1,node[1]) not in path and L[node[0]-1][node[1]]==1:
                path.append((node[0]-1,node[1]))
                queue.enqueue([path,0])
                path=path[:-1]
            if node[1]-1>=0  and (node[0],node[1]-1) not in path and L[node[0]][node[1]-1]==1:
                path.append((node[0],node[1]-1))
                queue.enqueue([path,3])
                path=path[:-1]
            if node[0]+1<length  and (node[0]+1,node[1]) not in path and L[node[0]+1][node[1]]==1:
                path.append((node[0]+1,node[1]))
                queue.enqueue([path,2])
                path=path[:-1]
    #print(pathrecord)
    return pathrecord



provided_input = input('Enter one integer: ')
try:
    for_seed = int(provided_input)
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(for_seed)
grid = [[randrange(2) for _ in range(10)] for _ in range(10)]
print('Here is the grid that has been generated:')
display_grid()
#print(grid)
path = leftmost_longest_path_from_top_left_corner(grid,[0,0])
if not path:
    print('There is no path from the top left corner.')
else:
    print(f'The leftmost longest path from the top left corner is: {path}')
           
