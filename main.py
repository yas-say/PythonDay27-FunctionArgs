#Unlimited Positional Args
# def add(*args):
#     sum = 0
#     for n in args:
#         sum += n
#     return sum
#
#
# print(add(1, 2, 3))



def calc(n, **kwargs):
    print(kwargs)
    print(type(kwargs))

    print(n)
    print(n+kwargs["add"])
    print(n + kwargs["mul"])


calc(2,add=3,mul=5)