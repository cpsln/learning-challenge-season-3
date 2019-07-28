class Student:
    def __init__(self,name,rollno):
        # instance variable inside the costructor
        self.name=name
        self.rollno=rollno
    
    def info(self):
        # accesss instance variable inside the class by using self 
        print('Name is : ',self.name)
        print('Rollno.: ',self.rollno)
    
s1=Student('chandra',16016)
s1.info()
# accesss instance variable outside the class by using reference of object
print('outside the class name: ',s1.name) 