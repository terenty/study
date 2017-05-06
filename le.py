def f(x, y):
    try:
        return x/y
    except (TypeError, ZeroDivisionError) as e:
        print(type(e))
        print(e)
        print(e.args)


print(f(6, 3))
print(f(6, 0))
print(f(6, []))

#--------------------------------
def greet(name):
    if name[0].isupper():
        return "Hello, " + name
    else:
        raise ValueError(name + "is unappropriate name")

while True:
    try:
        name = input("please enter your name:")
        greeting = greet(name)
        print(greeting)
    except ValueError:
        print("Please try again")
    else:
        break

print(__name__)
def fib(k):
    if k == 0 or k == 1:
        return 1
    else:
        return fib(k-1) + fib(k-2)

if __name__ == "__main__":
    print(fib(31))
with open("encrypted.bin", "rb") as inp:
    enrypted = inp.read()

print(enrypted)


for line in open("passwords.txt", "r"):

    try:
        print(line)
        dectxt = simplecrypt.decrypt(line.rstrip(), enrypted)#.decode('utf8')
        print(dectxt)
    except simplecrypt.DecryptionException:
        print("Wrong password")

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
#
# import os
# import os.path
# import shutil
#
# arcf = "main.zip"
# shutil.unpack_archive(arcf)
# dirname = arcf.split(".")[0]
#
# print(dirname)
#
# dir_py = []
# for (current_dir, dirs, files) in os.walk(dirname):
# #    print(current_dir, dirs, files)
#     for i in files:
# #        print(files)
#         if i.lower().endswith(".py"):
# #            print(current_dir)
#             dir_py.append(current_dir)
# #            print(dir_py)
#             break
# with open("main_out.txt", "w") as fout:
#     for el in sorted(dir_py):
#         print(el, file=fout)


# print(os.getcwd())
# print(os.listdir())
# print(os.listdir(".idea"))
# print(os.path.abspath("tst.py"))

# def mod_checker(x, mod=0):
#     return lambda y: y % x == mod
#
# mod_5 = mod_checker(5)
# if mod_5(5):
#     print("True")
# else:
#     print("False")