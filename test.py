def wrap(func):
    def inner(a):
       print(a) 
       return func(a)
    return inner

@wrap
def func(x):
    return x 


def estLen(string : str):
    counter = 0
    return len(string)