string = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
string2 = bytes.fromhex(string)
flag_format = b'crypto{'

key = [o1 ^ o2
       for (o1, o2) in zip(string2, flag_format)] + [ord("y")]

