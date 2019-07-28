class Employee:
     def __init__(self,eno,ename,esal):
         self.eno=eno
         self.ename=ename
         self.esal=esal

     def display(self):
        print('Employee number:',self.eno)
        print('Employee name:',self.ename)
        print('Employee salary:',self.esal)

class Test:
    def modify(emp):
        emp.esal=emp.esal+1000
        emp.display()


e=Employee(100,'chandra',5000)
Test.modify(e)