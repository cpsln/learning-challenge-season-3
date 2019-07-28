class Outer:
    def __init__(self):
        print('Outer class object creation.....')

    class Inner:
        def __init__(self):
            print('Inner class object creation....')
        def m1(self):
            print('Inner class method')

o=Outer() # create outer class object
i=o.Inner() # create innner class object
# call inner class method
i.m1()

print('\n---------- or formate 1 ----------------\n')
i=Outer().Inner()
i.m1()

print('\n---------- or formate 2 ----------------\n')
Outer().Inner().m1()
