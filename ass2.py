import os
import copy

class FriezeError(Exception):
    def __init__(self,message):
        self.message=message
        
    
class Frieze:
    def __init__(self,name):
        self.name=name[:-4]
        with open(name,'r') as f:
            data=f.readlines()
        matrix=[]
        for line in data:
            matrix.append(line.split())
        #print(matrix)
        nums=[]
        for i in range(16):
            nums.append(str(i))
        grid1=[]
        for i in range(len(matrix)):
            if matrix[i]!=[]:
                grid1.append(matrix[i])
        #print(grid1)
        for i in range(len(grid1)):
            for j in range(len(grid1[i])):
                if grid1[i][j] not in nums:
                    raise FriezeError('Incorrect input.')
        grid=[]
        for i in range(len(grid1)):
            if grid1[i]!=[]:
                grid.append([])
                for j in range(len(grid1[i])):
                    grid[i].append(int(grid1[i][j]))
        #print(grid)
        self.grid=grid
        if self.firstjudge() == False:
            raise FriezeError('Incorrect input.')
        self.direct=self.binarymatrix()
        self.period=self.findperiod()

        if self.secondjudge() == False:
            raise FriezeError('Input does not represent a frieze.')



    def findperiod(self):
        length=len(self.grid[0])-1
        #print(length)
        testscope=[]
        self.period=0
        flag=True
        for i in range(1,(length)//2+1):
            if length%i==0:
                testscope.append(i)
        #print(testscope)
        for i in testscope:
            flag=True
            for j in range(len(self.grid)):
                for k in range(i):
                    for l in range(i,length,i):
                        if self.grid[j][k]!=self.grid[j][k+l]:
                            #print(' here')
                            flag=False
                            break
                    if flag==False:
                        break
                if flag==False:
                    break
            if flag==True:
                self.period = i
                break
        #print(self.period)
        return self.period
    def firstjudge(self):
        if len(self.grid)<3 or  len(self.grid)>17:
            return False
        orilen=len(self.grid[0])
        for i in range(1,len(self.grid)):
            if len(self.grid[i]) != orilen:
                return False
        if orilen > 51 or orilen <5:
            return False
        return True
    def secondjudge(self):
        #上下不能超出边界且必须有边界
        l1=len(self.grid)
        l2=len(self.grid[0])
        for i in range(l2-1):
            if [0,i] not in self.direct[1]:
                return False
            if [l1-1,i]not in self.direct[1]:
                return False           
        for i in self.direct[3]:
            if i[0]==0:
                return False
        for i in self.direct[2]:
            if i[0]==0:
                return False
        for i in self.direct[0]:
            if i[0]==l1-1:
                return False
        #最右只有0,1
        for i in range(l1):
            if self.grid[i][l2-1] not in [0,1]:
                return False
        #最左最右对称
        for i in self.direct[3]:
            if i[1]==0:
                if[i[0],l2-1]not in self.direct[3]:
                    return False
            if i[1]==l2-1:
                if [i[0],0] not in self.direct[3]:
                    return False
        #period小于2
        if self.period<2:
            #print(self.period)
            return False
        #无交叉
        for i in self.direct[0]:
            if [i[0]+1,i[1]] in self.direct[2]:
                return False
            
            
    def binarymatrix(self):
        binmatrix=[]
        for i in range(len(self.grid)):
            binmatrix.append([])
            for j in range(len(self.grid[i])):
                binmatrix[i].append(str(bin(self.grid[i][j]))[2:].zfill(4))
        l=len(binmatrix)
        direct={0:[],1:[],2:[],3:[]}
        for i in range(l):
            for j in range(len(binmatrix[i])):
                for k in range(4):
                    if binmatrix[i][j][k]=='1':
                        direct[k].append([i,j])
        self.direct=[direct[0],direct[1],direct[2],direct[3]]
        #print (self.direct)
        return self.direct

    def edges(self):
        direct=copy.deepcopy(self.direct)
        edge={0:[],1:[],2:[],3:[]}
        if direct[3]!=[]:
            l1=sorted(direct[3],key=lambda x:x[1])
            edge[3].append([l1[0]])
            index=0
            for i in range(1,len(l1)):
                if i<len(l1)-1:
                    if [l1[i][0]-1,l1[i][1]]==l1[i-1] and [l1[i+1][0]-1,l1[i+1][1]]!=l1[i]:
                        edge[3][index].append(l1[i])
                    if [l1[i][0]-1,l1[i][1]]!=l1[i-1]:
                        edge[3].append([l1[i]])
                        index+=1
                if i==len(l1)-1:
                    if l1[-1]==[l1[-2][0]+1,l1[-2][1]]:
                        edge[3][index].append(l1[-1])
                    else:
                        edge[3].append([l1[-1]])
            #print(edge[3])
        if direct[1]!=[]:
            l2=sorted(direct[1])
            #print(l2)
            edge[1].append([l2[0]])
            index=0
            for i in range(1,len(l2)):
                if i<len(l2)-1:
                    if [l2[i][0],l2[i][1]-1]==l2[i-1] and [l2[i+1][0],l2[i+1][1]-1]!=l2[i]:
                        edge[1][index].append(l2[i])
                    if [l2[i][0],l2[i][1]-1]!=l2[i-1]:
                        edge[1].append([l2[i]])
                        index+=1
                if i==len(l2)-1:
                    if l2[-1]==[l2[-2][0],l2[-2][1]+1]:
                        edge[1][index].append(l2[-1])
                    else:
                        edge[1].append([l2[-1]])
            #print(edge[1])
        if direct[2]!=[]:
            l3=direct[2]
            edge[2].append([l3[0]])
            l3.remove(l3[0])
            while l3 !=[]:
                flag=0
                for i in range(len(edge[2])):
                    if [l3[0][0]-1,l3[0][1]+1] not in edge[2][i] and [l3[0][0]+1,l3[0][1]-1] not in edge[2][i]:
                        flag=0
                    elif [l3[0][0]-1,l3[0][1]+1] in edge[2][i]:
                        if len(edge[2][i])==2:
                            edge[2][i][0]=l3[0]
                        else:
                            edge[2][i].append(l3[0])
                            edge[2][i].reverse()
                        flag=1
                        break
                    elif [l3[0][0]+1,l3[0][1]-1] in edge[2][i]:
                        if len(edge[2][i])==2:
                            edge[2][i][1]=l3[0]
                        else:
                            edge[2][i].append(l3[0])
                        flag=1
                        break
                if flag ==0:
                    edge[2].append([l3[0]])
                l3.remove(l3[0])
            edge[2].sort(key=lambda x:(x[0][0],x[0][1]))
            #print(edge[2])
        if direct[0]!=[]:
            l4=direct[0]
            edge[0].append([l4[0]])
            l4.remove(l4[0])
            while l4 !=[]:
                flag=0
                for i in range(len(edge[0])):
                    if [l4[0][0]+1,l4[0][1]+1] not in edge[0][i] and [l4[0][0]-1,l4[0][1]-1] not in edge[0][i]:
                        flag=0
                    elif [l4[0][0]-1,l4[0][1]-1] in edge[0][i]:
                        if len(edge[0][i])==2:
                            edge[0][i][1]=l4[0]
                        else:
                            edge[0][i].append(l4[0])
                        flag=1
                        break
                    elif [l4[0][0]+1,l4[0][1]+1] in edge[0][i]:
                        if len(edge[0][i])==2:
                            edge[0][i][0]=l4[0]
                        else:
                            edge[0][i].append(l4[0])
                            edge[0][i].reverse()
                        flag=1
                        break
                if flag ==0:
                    edge[0].append([l4[0]])
                l4.remove(l4[0])
            #print(edge[0])
        self.edge=[edge[0],edge[1],edge[2],edge[3]]
        return self.edge

    def if_horizontal(self):
        direct = copy.deepcopy(self.direct)
        length=len(self.grid[0])
        leng=len(self.grid)
        periodlength=self.period
        north=True
        east=True
        northeast=True
        southeast=True
        for i in range(periodlength):
            for j in range(leng):
                if [i,j] in direct[1]:
                    if [leng-1-i,j] not in direct[1]:
                        east=False
                        break
            if east == False:
                break
        if east == True:
            for i in range(periodlength):
                for j in range(1,leng):
                    if [i,j] in direct[3]:
                        if [leng-i,j] not in direct[3]:
                            north=False
                            break
                if north == False:
                    break
        if east==True and north==True:
            while direct[0]!=[]:
                if [leng-1-direct[0][0][0],direct[0][0][1]]in direct[2]:
                    direct[2].remove([leng-1-direct[0][0][0],direct[0][0][1]])
                    direct[0].remove(direct[0][0])
                else:
                    northeast=False
                    break
            if direct[2]!=[]:
                southeast=False
        if east==True and north==True and northeast==True and southeast==True:
            return True
        else:
            return False

    def if_vertical(self):
        direct = copy.deepcopy(self.direct)
        length=len(self.grid[0])
        leng=len(self.grid)
        period=self.period
        for i in range(0,period):
            #print(i)
            flag1=True
            centersum=2*i+period-1
            for j in range(i,i+period):
                for k in range(leng):
                    #print([k,j],[k,centersum-j])
                    if [k,j] in direct[3] and [k,centersum-j]not in direct[3]:
                        flag1=False
                        break
                    #print([k,j],[k,centersum-j-1])
                    if [k,j] in direct[1] and [k,centersum-j-1]not in direct[1]:
                        flag1=False
                        break
                    if [k,j] in direct[2] and [k-1,centersum-j-1]not in direct[0]:
                        flag1=False
                        break
                    if [k,j] in direct[0] and [k+1,centersum-j-1]not in direct[2]:
                        flag1=False
                        break
                if flag1==False:
                    break
            if flag1 ==True:
                break
        if flag1==False:
            direct = self.direct
            length=len(self.grid[0])
            leng=len(self.grid)
            period=self.period
            for i in range(0,period):
                #print(i)
                flag2=True
                centersum=2*i+period
                for j in range(i,i+period):
                    for k in range(leng):
                        #print([k,j],[k,centersum-j])
                        if [k,j] in direct[3] and [k,centersum-j]not in direct[3]:
                            flag2=False
                            break
                        #print([k,j],[k,centersum-j])
                        if [k,j] in direct[1] and [k,centersum-j-1]not in direct[1]:
                            flag2=False
                            break
                        if [k,j] in direct[2] and [k-1,centersum-j-1]not in direct[0]:
                            flag2=False
                            break
                        if [k,j] in direct[0] and [k+1,centersum-j-1]not in direct[2]:
                            flag2=False
                            break
                    if flag2==False:
                        break
                if flag2 ==True:
                    break

        if flag1==True or flag2==True:
            return True
        else:
            return False


    def if_glid(self):
        period=self.period
        direct = copy.deepcopy(self.direct)
        length=len(self.grid)
        newspace=[]
        for i in range(length):
            newspace.append([])
            for j in range(period):
                newspace[i].append(0)
        for i in range(length):
            for j in range(period):
                if [i,j] in direct[1]:
                    newspace[length-1-i][j]=newspace[length-1-i][j]+4
                if [i,j] in direct[2]:
                    newspace[length-1-i][j]=newspace[length-1-i][j]+8
                if [i,j] in direct[3]:
                    newspace[length-i][j]=newspace[length-i][j]+1
                if [i,j] in direct[0]:
                    newspace[length-1-i][j]=newspace[length-1-i][j]+2
        #print(newspace)
        glid=period//2
        flag=True
        for i in range(period):
            for j in range(length):
                if newspace[j][i]!=self.grid[j][i+glid]:
                    flag=False
                    break
            if flag==False:
                break
        return flag
            
    def if_rotation(self):
        period=self.period
        direct = copy.deepcopy(self.direct)
        length=len(self.grid)
        flag2=True
        for i in range(0,period):
            flag1=True
            centersum=2*i+period-1
            for j in range(i,i+period):
                for k in range(length):
                    if [k,j]in direct[0]:
                        #print([k,j],[length-k-2,centersum-j-1],8)
                        if[length-k-2,centersum-j-1]not in direct[0]:
                            flag1=False
                            break
                    if [k,j]in direct[1]:
                        #print([k,j],[length-1-k,centersum-j-1],4)
                        if [length-1-k,centersum-j-1] not in direct[1]:
                            flag1=False
                            break
                    if [k,j]in direct[2]:
                        #print([k,j],[length-k,centersum-j-1],2)
                        if [length-k,centersum-j-1] not in direct[2]:
                            flag1=False
                            break
                    if [k,j]in direct[3]:
                        #print([k,j],[length-k,centersum-j],1)
                        if[length-k,centersum-j]not in direct[3]:
                            flag1=False
                            break
                if flag1==False:
                    break
            if flag1==True:
                break
        if flag1==False:
            for i in range(0,period):
                flag2=True
                centersum=2*i+period-1
                for j in range(i,i+period):
                    for k in range(length):
                        if [k,j]in direct[0]:
                            #print([k,j],[length-k-2,centersum-j],8)
                            if [length-k-2,centersum-j] not in direct[0]:
                                flag2=False
                                break
                        if [k,j]in direct[1]:
                            #print([k,j],[length-1-k,centersum-j],4)
                            if[length-1-k,centersum-j]not in direct[1]:
                                flag2=False
                                break
                        if [k,j]in direct[2]:
                            #print([k,j],[length-k,centersum-j],2)
                            if[length-k,centersum-j] not in direct[2]:
                                flag2=False
                                break
                        if [k,j]in direct[3]:
                            #print([k,j],[length-k,centersum-j+1],1)
                            if[length-k,centersum-j+1] not in direct[3]:
                                flag2=False
                                break
                    if flag2==False:
                        break
                if flag2==True:
                    break
        if flag1 ==True or flag2==True:
            return True
        else:
            return False                       

        
    def analyse(self):
        vertical=self.if_vertical()
        horizontal=self.if_horizontal()
        glid=self.if_glid()
        rotation=self.if_rotation()
        #print(vertical,horizontal,glid,rotation)
        if horizontal==False and  glid==False and vertical==False and rotation==False:
            str=(f'Pattern is a frieze of period {self.period} that is invariant under translation only.')
        elif horizontal==False and  glid==False and vertical==True and rotation==False:
            str=(f'Pattern is a frieze of period {self.period} that is invariant under translation\n        and vertical reflection only.')
        elif horizontal==True and  glid==False and vertical==False and rotation==False:
            str=(f'Pattern is a frieze of period {self.period} that is invariant under translation\n        and horizontal reflection only.')
        elif horizontal==False and  glid==True and vertical==False and rotation==False:
            str=(f'Pattern is a frieze of period {self.period} that is invariant under translation\n        and glided horizontal reflection only.')
        elif horizontal==False and  glid==False and vertical==False and rotation==True:
            str=(f'Pattern is a frieze of period {self.period} that is invariant under translation\n        and rotation only.')
        elif horizontal==False and  glid==True and vertical==True and rotation==True:
            str=(f'Pattern is a frieze of period {self.period} that is invariant under translation,\n        glided horizontal and vertical reflections, and rotation only.')
        elif horizontal==True and  glid==False and vertical==True and rotation==True:
            str=(f'Pattern is a frieze of period {self.period} that is invariant under translation,\n        horizontal and vertical reflections, and rotation only.')
        print(str)

        
    def fixedges(self):
        edge=self.edges()
        for i in range(len(edge)):
            for j in range(len(edge[i])):
                if i==0:
                    if len(edge[i][j])==2:
                        edge[i][j][0]=[edge[i][j][0][1],edge[i][j][0][0]]
                        edge[i][j][1]=[edge[i][j][1][1]+1,edge[i][j][1][0]+1]
                    if len(edge[i][j])==1:
                        edge[i][j][0]=[edge[i][j][0][1],edge[i][j][0][0]]
                        edge[i][j].append([edge[i][j][0][0]+1,edge[i][j][0][1]+1])                        
                if i==1:
                    if len(edge[i][j])==2:
                        edge[i][j][0]=[edge[i][j][0][1],edge[i][j][0][0]]
                        edge[i][j][1]=[edge[i][j][1][1]+1,edge[i][j][1][0]]
                    if len(edge[i][j])==1:
                        edge[i][j][0]=[edge[i][j][0][1],edge[i][j][0][0]]
                        edge[i][j].append([edge[i][j][0][0]+1,edge[i][j][0][1]])
                if i==2:
                    if len(edge[i][j])==2:
                        edge[i][j][0]=[edge[i][j][0][1],edge[i][j][0][0]]
                        edge[i][j][1]=[edge[i][j][1][1]+1,edge[i][j][1][0]-1]
                    if len(edge[i][j])==1:
                        edge[i][j][0]=[edge[i][j][0][1],edge[i][j][0][0]]
                        edge[i][j].append([edge[i][j][0][0]+1,edge[i][j][0][1]-1])
                if i==3:
                    if len(edge[i][j])==2:
                        edge[i][j][0]=[edge[i][j][0][1],edge[i][j][0][0]-1]
                        edge[i][j][1]=[edge[i][j][1][1],edge[i][j][1][0]]
                    if len(edge[i][j])==1:
                        edge[i][j][0]=[edge[i][j][0][1],edge[i][j][0][0]-1]
                        edge[i][j].append([edge[i][j][0][0],edge[i][j][0][1]+1])
        #print(edge[0])
        return edge
                    
    def display(self):
        edge=self.fixedges()
        document = open(f"{self.name}.tex", "w+")
        #print ("文件名: ", document.name)
        document.write('\documentclass[10pt]{article}\n\\usepackage{tikz}\n\\usepackage[margin=0cm]{geometry}\n\pagestyle{empty}')
        document.write('\n\n\\begin{document}\n\n\\vspace*{\\fill}\n\\begin{center}\n\\begin{tikzpicture}[x=0.2cm, y=-0.2cm, thick, purple]\n')
        document.write('% North to South lines\n')
        for i in range(len(edge[3])):
            document.write(f'    \\draw ({edge[3][i][0][0]},{edge[3][i][0][1]}) -- ({edge[3][i][1][0]},{edge[3][i][1][1]});\n')
        document.write('% North-West to South-East lines\n')
        for i in range(len(edge[0])):
            document.write(f'    \\draw ({edge[0][i][0][0]},{edge[0][i][0][1]}) -- ({edge[0][i][1][0]},{edge[0][i][1][1]});\n')        
        document.write('% West to East lines\n')
        for i in range(len(edge[1])):
            document.write(f'    \\draw ({edge[1][i][0][0]},{edge[1][i][0][1]}) -- ({edge[1][i][1][0]},{edge[1][i][1][1]});\n')
        document.write('% South-West to North-East lines\n')
        for i in range(len(edge[2])):
            document.write(f'    \\draw ({edge[2][i][0][0]},{edge[2][i][0][1]}) -- ({edge[2][i][1][0]},{edge[2][i][1][1]});\n')
        document.write('\\end{tikzpicture}\n')
        document.write('\\end{center}\n')
        document.write('\\vspace*{\\fill}\n\n')
        document.write('\\end{document}\n')        
        
        #print (document.tell())
        #输出当前指针位置
        document.seek(os.SEEK_SET)
        #设置指针回到文件最初
        context = document.read()
        #print (context)
        document.close()
