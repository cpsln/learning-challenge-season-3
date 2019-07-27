import pickle
class Employee:
    def __init__(self,eno,ename,esal,eaddr):
        self.eno=eno
        self.ename=ename
        self.asal=esal
        self.eaddr=eaddr
    def display(self):
        print(self.eno,'\n',self.ename,'\n',self.asal,'\n',self.eaddr)

with open('emp.txt','wb') as f:
    e=Employee(100,'chandra',1000,'Bangalore')
    pickle.dump(e,f)
    print('Pickling of employee object completed...')

with open('emp.txt','rb') as f:
    obj=pickle.load(f)
    print('Employee informtion after unpickling....')
    obj.display()
    print(obj)
    