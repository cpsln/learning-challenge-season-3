#create a file and store in file many type of mobile number and this program find indian number to your file

import re
f1=open('input.txt','r')
f2=open('output.txt','w')
for line in f1:
    l=re.findall('[6-9]\d{9}',line)
    for n in l:
        f2.write(n+'\n')
    print(l)

print('\n------------Extracted all mobile number into output.txt--------------')
f1.close()
f2.close()
f=open('output.txt','r')
for ls in f:
    print(ls)
f.close()