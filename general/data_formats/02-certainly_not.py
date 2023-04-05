from Crypto.PublicKey import RSA

key = RSA.importKey(open('transparency.pem', 'rb').read())

print(key.domain())