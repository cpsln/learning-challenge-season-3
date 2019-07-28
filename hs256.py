import jwt
e='9559229571'
en=jwt.encode(e,'secret',algorithm='HS256')
print(en)

a=jwt.decode(en, 'secret', algorithms=['HS256'])
print(a)
# {'some':'payloyed'}