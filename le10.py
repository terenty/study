def f(x, y):
    try:
        return x/y
    except TypeError:
        print ("Type error")
    except ZeroDivisionError:
        print("Zero division")

print(f(6, 3))
