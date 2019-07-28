import jwt
import json
from jwt.contrib.algorithms.pycrypto import RSAAlgorithm
private_key = b'-----BEGIN PRIVATE KEY-----\nMIGEAgEAMBAGByqGSM49AgEGBS...'
public_key = b'-----BEGIN PUBLIC KEY-----\nMHYwEAYHKoZIzj0CAQYFK4EEAC...'
encoded = jwt.encode({'some': 'payload'}, private_key, algorithm='RS384')
print(encoded)