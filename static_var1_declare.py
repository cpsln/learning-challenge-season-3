class Test:
    a=10  # static variable within the class
    def __init__(self):
        self.b=20
        Test.c=30 # using class name inside constructor static variable
    
    def m1(self):
        self.d=40
        Test.e=50 # using class name inside instance method static variable
    
    @classmethod
    def m2(cls): # class method
        cls.f=60
        Test.g=70

    @staticmethod
    def m3():
        Test.h=80

t=Test()
t.m1()
Test.m2()
Test.m3() # or t.m3()
Test.i=90 # static variable outside the class
print(Test.__dict__)
print(t.a,t.c,t.e,t.f,t.g,t.h,t.i) # using object reference access static variable
print(Test.a,Test.c,Test.e,Test.f,Test.g,Test.h,Test.i) # using class name access static variable

