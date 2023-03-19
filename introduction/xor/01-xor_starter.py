string = ''

for i in "label":
    tmp = ord(i) ^ 13
    string += chr(tmp)


print("crypto" + "{" + string + "}")
