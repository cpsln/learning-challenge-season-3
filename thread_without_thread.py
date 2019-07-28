import time
def doubles():
    for n in range(1,6):
        time.sleep(1)
        print('Double:',2*n)

def squares():
    for n in range(1,6):
        time.sleep(1)
        print('Square:',n*n)

# num=[1,2,3,4,5]
begin=time.time()
doubles()
squares()
end=time.time()
print('Total time:',end-begin)