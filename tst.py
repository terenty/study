import simplecrypt

# txt = "Hello, Alies"
# passw = "secure"
# print(txt)
# print(passw)
# enctxt = encrypt(passw, txt)
# print(enctxt)
# dectxt = decrypt(passw, enctxt)
# print(dectxt)
# print("why")

# with open("encrypted.bin", "rb") as inp:
#     enrypted = inp.read()
#
# print(enrypted)
#
#
# for line in open("passwords.txt", "r"):
#
#     try:
#         print(line)
#         dectxt = simplecrypt.decrypt(line.rstrip(), enrypted)#.decode('utf8')
#         print(dectxt)
#     except simplecrypt.DecryptionException:
#         print("Wrong password")

with open("test.txt") as f, open("tset.txt", "w") as f1:
    sp = []
    for line in f:
        sp.append(line.rstrip())

    print(sp)
    sp.reverse()
    print(sp)

    for li in sp:
        f1.write(li+"\n")
