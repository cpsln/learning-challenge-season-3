import emp,pickle
f=open('emp1.txt','rb')
print('Employee Detail.......')
obj=pickle.load(f)
'''while (obj!=''):
    obj.display()
    obj=pickle.load(f)'''
while True:
    try:
        obj=pickle.load(f)
        obj.display()
    except EOFError:
        print('All employee completed')
        break