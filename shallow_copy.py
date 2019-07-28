import copy
l1=[10,20,[30,40],50,60]
l2=copy.copy(l1)
print(l1)
print(l2)
l1[2][0]=444
print('\n',l1)
print(l2)