string = ''
for i in "label":
    string += chr(ord(i) ^ 13)

print("crypto" + "{" + string + "}")
