from binascii import unhexlify

encrypted = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
encrypted = unhexlify(encrypted)
stringlist_to_xor = [i for i in encrypted]

possibleflag_list = []
for order in range(256):
    possibleflag_ord = [order ^ i for i in stringlist_to_xor]
    possibleflag = ''.join(chr(i) for i in possibleflag_ord)
    possibleflag_list.append(possibleflag)

for i in possibleflag_list:
    if "crypto" in i:
        print(i)
    else: continue