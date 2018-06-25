import sys
from random import seed, randint


try:
    arg_for_seed, upper_bound, length = input('Enter three nonnegative integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, upper_bound, length = int(arg_for_seed), int(upper_bound), int(length)
    if arg_for_seed < 0 or upper_bound < 0 or length < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
L = [randint(0, upper_bound) for _ in range(length)]
print('\nThe generated list L is:')
print('  ', L)


L_1 = []
L_2 = []
L_3 = []
elements_to_keep = []

new_list = sorted(list(set(L)))
new_length = len(new_list)
elements_to_keep = new_list[0:new_length:2]


#L_1
for i in range(length):
    for j in range(len(elements_to_keep)):
        if L[i] == elements_to_keep[j]:
            L_1.append(L[i]) 
            
#L_2
etk = elements_to_keep[:]
for k in range (len(L_1)):
    for l in range (len(etk)):
        if L_1[k] == etk [l]:
            L_2.append(L_1[k])
            del etk[l]
            break
        
#L_3
def ifcontin(List):
    L= list(set(List))
    L.sort()
    m=max(L)
    n=min(L)
    if m-n+1==len(L) :
        return True
    else:
        return False

L_3= []     #L_3 unselected list
for m in range(length-1):
    for n in range(m+1,length):
        L_3_sub = L[m:n+1]   #L_3_sub every list with original sequence
        if ifcontin(L_3_sub) == True and len(L_3_sub) > len(L_3):
            L_3 = L_3_sub
print('\nThe elements to keep in L_1 and L_2 are:')
print('  ', elements_to_keep)
print('\nHere is L_1:')
print('  ', L_1)
print('\nHere is L_2:')
print('  ', L_2)
print('\nHere is L_3:')
print('  ', L_3)
