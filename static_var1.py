class Test:
    a=10  #class level or static variable
    def __init__(self):
        self.b=20
        
t=Test()
t1=Test()
print('t: ',t.a,' ',t.b)
print('t1: ',t1.a,' ',t1.b)
Test.a=222
t.b=111
print('t: ',t.a,' ',t.b)
print('t1: ',t1.a,' ',t1.b)