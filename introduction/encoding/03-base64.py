from base64 import b64encode

hex = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

byte = bytes.fromhex(hex)

final = b64encode(byte)
print(final)