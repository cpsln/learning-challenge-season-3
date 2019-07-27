n=int(input('enter row: '))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()

print('\n-------number----------\n')

for i in range(n,0,-1):
    if i<n:
        print(' '*(n-i),end='')
    for j in range(i,0,-1):
        print(i,end='')
    print() 
print('\n--------------number 1 to 5-----------------\n')
for i in range(1,n+1):
    if i>1:
        print(' '*(i-1),end='')
    for j in range(1,n+2-i):
        print(j,end='')
    print()   