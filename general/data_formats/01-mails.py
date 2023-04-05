from Crypto.PublicKey import RSA

key = RSA.importKey(open('email.pem', 'rb').read())

print(key.d)