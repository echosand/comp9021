import sys
from math import gcd


try:
    numerator, denominator = input('Enter two strictly positive integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    numerator, denominator = int(numerator), int(denominator)
    if numerator <= 0 or denominator <= 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()


has_finite_expansion = False
integral_part = 0
sigma = ''
tau = ''

# Replace this comment with your code
a= numerator
b= denominator
solution = []
remainder = []

integral_part =a//b
while a!=0:
    k = a // b
    solution.append(k)
    l = a % b
    remainder.append(l)
    a = l
    if a==0:
        has_finite_expansion = True
        break
    else:
        if a in remainder[0:len(remainder)-1]:
            has_finite_expansion = False
			
            break
        else:
            a=a*10

def loop_num(num,list1,list2):
    for i in range(0,len(list1)):
        if num== list1[i]:
            xigema=list2[0:i+1]
            tao = list2[i+1:]
            return (xigema,tao)
            break
loop=loop_num(a,remainder,solution)

def string(list1):
    str1=''
    for i in range (len(list1)):
        str1 += str(list1[i])
    return str1
tau = string(loop[1])
sigma = string(loop[0])
if integral_part >0:
	cut_length = len(str(integral_part))
	sigma = sigma[cut_length:]
else:
	sigma = sigma[1:]
    

if has_finite_expansion:
    print(f'\n{numerator} / {denominator} has a finite expansion')
else:
    print(f'\n{numerator} / {denominator} has no finite expansion')
if not tau:
    if not sigma:
        print(f'{numerator} / {denominator} = {integral_part}')
    else:
        print(f'{numerator} / {denominator} = {integral_part}.{sigma}')
else:
    print(f'{numerator} / {denominator} = {integral_part}.{sigma}({tau})*')
