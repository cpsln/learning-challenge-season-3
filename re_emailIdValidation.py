import re
s= input('Enter email_id: ')
m=re.fullmatch('\w[a-zA-Z0-9_.]*@(gmail|rediffmail)[.]com',s)
if m!=None:
    print(s,'is valid email_id')
else:
    print(s,'is not valid email_id')