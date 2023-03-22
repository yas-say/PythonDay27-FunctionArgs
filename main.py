#Unlimited Positional Args
# def add(*args):
#     sum = 0
#     for n in args:
#         sum += n
#     return sum
#
#
# print(add(1, 2, 3))


#Unlimited Keyword Args
def calc(n, **kwargs):
    print(kwargs)
    print(type(kwargs))

    print(n)
    print(n+kwargs.get("add"))
    print(kwargs.get("mul"))


calc(2,add=3,mul=5)
calc(2,add=4)