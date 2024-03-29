from pwn import remote # pip install pwntools
import base64
import codecs
import random
import json
from Crypto.Util.number import *

r = remote('socket.cryptohack.org', 13377, level = "debug")

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hash):
    request = json.dumps(hash).encode()
    r.sendline(request)


def decoding():
    for i in range(0, 101):
        received = json_recv()

        to_send = {
            "decoded": ""
        }
        if "type" in received:
            if received["type"] == "base64":
                to_send["decoded"] = base64.b64decode(received["encoded"]).decode("utf-8")

            elif received["type"] == "hex":
                to_send["decoded"] = bytes.fromhex(received["encoded"]).decode("utf-8")

            elif received["type"] == "rot13":
                to_send["decoded"] = codecs.decode(received["encoded"], 'rot_13')

            elif received["type"] == "bigint":
                tmp = int(received["encoded"], 16)
                to_send["decoded"] = long_to_bytes(tmp).decode("utf-8")

            elif received["type"] == "utf-8":        
                for b in received["encoded"]:
                    to_send["decoded"] += chr(b) 
            
            json_send(to_send)
        
        elif "flag" in received:
            print(received["flag"])
        
    return 0
if __name__ == "__main__":
    decoding()
