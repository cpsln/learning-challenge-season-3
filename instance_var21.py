cdclass Test:
    def __init__(self,name,age,tech):
        self.name=name
        self.age=age
        self.tech=tech

s1=Test('chandra',48,'python')
s2=Test('vikash',45,'python')
s1.gf='abc'
s1.gf2='abcgd'
print(s1.__dict__)
print(s2.__dict__)

        