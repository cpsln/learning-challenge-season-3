import copy
l1=[10,20,[30,40],50,60]
l2=copy.deepcopy(l1)
print(l1,'\n',l2,'\n')
l2[2][0]=400
print(l1,'\n',l2)