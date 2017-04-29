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