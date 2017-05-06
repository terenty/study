# unique value in list
# def unique(iterable, seen=None):
#     seen = set(seen or []) #None --- falsy
#     acc = []
#     for item in iterable:
#         if item not in seen:
#             seen.add(item)
#             acc.append(item)
#     return acc
# xs = [1, 1, 2, 2, 3]
# print(unique(xs))
# rec = (0,0),(1,1)
# print(rec)
# (x1,y1),(x2,y2) = rec
# print(x2)
#---------------- key agrs ---------------------
# def runner(cmd, **kwargs):
#     print("runner...")
#     if kwargs.get("verbose", True):
#         print("Logging enabled")
#
# runner("mysql", limit=42)
# runner("mysql", **{"verbose": False})
# runner("mysql", **{"verbose": True})
# options = {"verbose": False}
# runner("mysql", **options)
# runner("mysql", **{"verbose": True})



