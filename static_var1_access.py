class Test:
    a=10  
    def __init__(self):
        print('---------access inside constructor---------')
        print(self.a)
        print(Test.a)

    def m1(self):
        print('\n---------access inside instance method---------')
        print(self.a)
        print(Test.a)
   
    @classmethod
    def m2(cls): 
        print('\n-----------access inside class method---------')
        print(cls.a)
        print(Test.a)

    @staticmethod
    def m3():
        print('\n---------access inside static---------')
        print(Test.a)

t=Test()
t.m1()
t.m2()
t.m3()
print('\n---------access outside class---------')
print(t.a)
print(Test.a)