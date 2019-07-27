# import serial
# import pickle
# import matplotlib.pyplot as plt
# arduinodata=serial.Serial('COM4',9600,timeout=1)

l=[]
for i in range(10):
    l.append(i)

print(l)
with open('file.txt','w') as f:
    for i in l:
        f.write('%d'%i)

with open('file.txt','r') as f1:
    while True:
         l=f1.read()
         print(l)
         if not l:
            break
