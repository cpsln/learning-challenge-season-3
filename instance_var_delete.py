class Test:
    def __init__(self):
        self.a=10
        self.b=20
        self.c=30
        self.d=40 
    def delete(self):
        # delete inside the class
        del self.b
        del self.c

t1=Test()
print('without call delete method\n')
print(t1.__dict__)

t1.delete()
print('\nafter call delete method\n')
print(t1.__dict__)

# delete outside the class using reference and variable name
del t1.a # a is variable name
# del t1.d
print('\noutside the class\n')
print(t1.__dict__)