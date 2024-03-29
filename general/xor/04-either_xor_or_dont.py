

encrypted = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
encrypted = bytes.fromhex(encrypted)
flag_format = b"crypto{"

def xor_something(msg1, msg2):
       msg_return = b''
       for f1, f2 in zip(msg1, msg2):
              msg_return += bytes([f1 ^ f2])
       return msg_return

def appending_key(encrypted_msg, header_key):
       return_key = header_key 
       while (len(return_key) < len(encrypted_msg)):
              return_key += header_key
       else: return return_key[:-(len(return_key) - len(encrypted_msg))].encode()

key = xor_something(encrypted[:7], flag_format).decode() + "y"
key = appending_key(encrypted, key)
print(xor_something(encrypted, key).decode("utf-8"))
