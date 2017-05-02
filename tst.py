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

#-------------files-------------------------
# with open("test.txt") as f, open("tset.txt", "w") as f1:
#     sp = []
#     for line in f:
#         sp.append(line.rstrip())
#
#     print(sp)
#     sp.reverse()
#     print(sp)
#
#     for li in sp:
#         f1.write(li+"\n")

import os
import os.path
import shutil

arcf = "main.zip"
shutil.unpack_archive(arcf)
dirname = arcf.split(".")[0]

print(dirname)

dir_py = []
for (current_dir, dirs, files) in os.walk(dirname):
#    print(current_dir, dirs, files)
    for i in files:
#        print(files)
        if i.lower().endswith(".py"):
#            print(current_dir)
            dir_py.append(current_dir)
#            print(dir_py)
            break
with open("main_out.txt", "w") as fout:
    for el in sorted(dir_py):
        print(el, file=fout)


# print(os.getcwd())
# print(os.listdir())
# print(os.listdir(".idea"))
# print(os.path.abspath("tst.py"))
