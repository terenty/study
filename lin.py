class NonPositiveError(Exception):
    pass

class PositiveList(list):
    def append(self, x):
        if x <= 0:
            raise NonPositiveError
        else:
            super().append(x)

ls=PositiveList()

ls.append(1)
ls.append(2)
print(ls)
ls.append(-1)
