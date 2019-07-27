n=int(input('enter row: '))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(64+j),end=' ')
    print()
print('\n-----reverse char triangle----------\n')
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print(chr(64+j),end=' ')
    print()
print('\n------triangle char n position to 1 position-------\n')
a=1
for i in range(1,n+1):
    a=1
    for j in range(1,n+1):
        if j<=n-i:
            print(' ',end=' ')
        else:
            print(chr(64+a)+' ',end='')
            a+=1
    print()


for i in range(1,n+1):
    print(' '*(n-i),end='')
    for j in range(1,i+1):
        print(chr(64+j),end='')
    print()
