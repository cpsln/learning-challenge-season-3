import emp,pickle
f=open('emp1.txt','wb')
n=int(input('Enter number of employee: '))
for i in range(n):
    eno=int(input('Enter Employee number: '))
    ename=input("Enter employee name: ")
    esal=float(input("Enter employee salary: "))
    eaddr=input("Enter employee addeass: ")
    e=emp.Employee(eno,ename,esal,eaddr)
    pickle.dump(e,f)