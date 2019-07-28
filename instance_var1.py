class Test:
    def __init__(self):
        self.x=10
    
t1=Test()
t2=Test()
print(t1.x,' ',t2.x)
print(t1.__dict__)
t1.x=88
print(t1.__dict__)
print(t1.x,' ',t2.x)