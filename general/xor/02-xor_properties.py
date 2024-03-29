from Crypto.Util.number import *

key1 = 0xa6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
key2_xor_key1 = 0x37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
key2_xor_key3 = 0xc1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
flag_xor = 0x04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf

key2 = key1 ^ key2_xor_key1
key3 = key2 ^ key2_xor_key3

flag = flag_xor ^ key1 ^ key2 ^ key3
flag = long_to_bytes(flag)
print(flag.decode("utf-8"))