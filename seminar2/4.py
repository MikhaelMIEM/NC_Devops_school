from math import *

def get_min_function(sequence, *funcs):
    """
    Я бы так в жизни не написал.
    Извините.
    """
    return min({func: sum([func(elem) for elem in sequence]) for func in funcs}.items(), key=lambda x: x[1])[0]

if __name__ == "__main__":
    print(get_min_function(range(1,4), sin, exp))
