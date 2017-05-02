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