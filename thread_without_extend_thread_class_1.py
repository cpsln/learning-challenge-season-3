from threading import*
class MyThraed():
    def display(self):
        for i in range(5):
            print('Child Thread')

obj=MyThraed()
t=Thread(target=obj.display)
t.start()
for i in range(5):
            print('Mian Thread')
