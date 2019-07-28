class Test:
    a=10  #class level or static variable
    def __init__(self):
        self.b=20
        
t=Test()
print(t.a,' ',t.b)
print(Test.a,' ',t.b)