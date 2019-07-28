from threading import*
class MyThraed(Thread):
    def run(self):
        for i in range(5):
            print('Child Thread')

t=MyThraed()
t.start()
for i in range(5):
    print('Main Thread')