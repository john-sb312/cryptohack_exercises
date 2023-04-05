from Crypto.PublicKey import RSA

key = RSA.importKey(open('bruce_rsa.pub', 'rb').read())

print(key.n)