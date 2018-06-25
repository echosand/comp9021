from math import sqrt


class PointError(Exception):
    def __init__(self, message):
        self.message = message


class Point():
    def __init__(self, x = None, y = None):
        if x is None and y is None:
            self.x = 0
            self.y = 0
        elif x is None or y is None:
            raise PointError('Need two coordinates, point not created.')
        else:
            self.x = x
            self.y = y



class TriangleError(Exception):
    def __init__(self, message):
        self.message = message


class Triangle:
    def __init__(self,*, point_1, point_2, point_3):
        self.point_1=point_1
        self.point_2=point_2
        self.point_3=point_3
        self.perimeter=0
        self.area=0
        if self.iftriangle():
            self.perimeter=self.getperimeter()
            self.area=self.getarea()
        

    def iftriangle(self):
        if (self.point_3.x-self.point_1.x)!=0 and(self.point_2.x-self.point_1.x)!=0:
            if ((self.point_3.y-self.point_1.y)/(self.point_3.x-self.point_1.x))==((self.point_2.y-self.point_1.y)/(self.point_2.x-self.point_1.x)):
                raise TriangleError('Incorrect input, triangle not created.')       
        elif (self.point_3.x-self.point_1.x)==0 and (self.point_2.x-self.point_1.x)==0:
            raise TriangleError('Incorrect input, triangle not created.')
        elif (self.point_3.x==self.point_1.x)and (self.point_3.y==self.point_1.y):
            raise('Incorrect input, triangle not created.')
            return False
        elif(self.point_2.x==self.point_1.x)and (self.point_2.y==self.point_1.y):
            print('Incorrect input, triangle not created..')
            return False
        return True

    def ifchange(self):
        if (self.point_3.x-self.point_1.x)!=0 and(self.point_2.x-self.point_1.x)!=0:
            if ((self.point_3.y-self.point_1.y)/(self.point_3.x-self.point_1.x))==((self.point_2.y-self.point_1.y)/(self.point_2.x-self.point_1.x)):           
                print('Incorrect input, triangle not modified.')
                return False
        elif (self.point_3.x-self.point_1.x)==0 and (self.point_2.x-self.point_1.x)==0:
            print('Incorrect input, triangle not modified.')
            return False
        elif (self.point_3.x==self.point_1.x)and (self.point_3.y==self.point_1.y):
            print('Incorrect input, triangle not motified.')
            return False
        elif(self.point_2.x==self.point_1.x)and (self.point_2.y==self.point_1.y):
            print('Incorrect input, triangle not motified.')
            return False
        return True
       
    def change_point_or_points(self, *, point_1 = None,point_2 = None, point_3 = None):
        tempp=self.perimeter
        tempa=self.area
        if point_1 is not None:
            self.point_1 = point_1
        if point_2 is not None:
            self.point_2 = point_2
        if point_3 is not None:
            self.point_3 = point_3
        if self.ifchange():
            self.perimeter=self.getperimeter()
            self.area=self.getarea()
        else:
            self.perimeter=tempp
            self.area=tempa

    def getperimeter(self):
        perimeter = sqrt((self.point_1.x-self.point_2.x)**2+(self.point_1.y-self.point_2.y)**2)+sqrt((self.point_2.x-self.point_3.x)**2+(self.point_2.y-self.point_3.y)**2)+sqrt((self.point_1.x-self.point_3.x)**2+(self.point_1.y-self.point_3.y)**2)
        return perimeter
    
    def getarea(self):
        a=sqrt((self.point_1.x-self.point_2.x)**2+(self.point_1.y-self.point_2.y)**2)
        b=sqrt((self.point_2.x-self.point_3.x)**2+(self.point_2.y-self.point_3.y)**2)
        c=sqrt((self.point_1.x-self.point_3.x)**2+(self.point_1.y-self.point_3.y)**2)
        p=0.5*self.perimeter
        area = sqrt(p*((p-a)*(p-b)*(p-c)))
        return area
