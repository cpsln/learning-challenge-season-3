class Employee:
    def __init__(self,eno,ename,esal,eaddr):
        self.eno=eno
        self.ename=ename
        self.asal=esal
        self.eaddr=eaddr
    def display(self):
        print(self.eno,'\t',self.ename,'\t',self.asal,'\t',self.eaddr)
    