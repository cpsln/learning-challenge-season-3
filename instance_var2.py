class Test:
    def __init__(self):
        self.x=10
        self.y=20
    def m1(self):
        self.z=300
        self.m=200
    
t1=Test()
# intance variable ,inside constructor
print(t1.__dict__)
print(t1.x,' ',t1.y)
# intance variable ,inside instance method 
t1.m1()
print(t1.__dict__)
print(t1.x,' ',t1.y,' ',t1.z,' ',t1.m)
# add outside the class instance variable
t1.n=150
print(t1.__dict__)
print(t1.x,' ',t1.y,' ',t1.z,' ',t1.m)
