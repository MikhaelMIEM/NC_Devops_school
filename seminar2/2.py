def fix_float(prec):
    def decorator(f):
        round_if_float = lambda x: round(x, prec) if type(x) is float else x
        def wrapped(*args, **kwargs):
            new_args = [round_if_float(arg) for arg in args]
            new_kwargs = {key: round_if_float(val) for key, val in kwargs.items()}
            ans = f(*new_args, **new_kwargs) 
            return round_if_float(ans)
        return wrapped
    return decorator

@fix_float(4)
def strange_multiplier(*args, mult=0):
    return sum(args) * args[mult]

print(strange_multiplier(0.451235421901, 1.12312342121, 2.523412E-2, 4, mult=-3))

@fix_float(2)
def add_greeting(greeting, number):
    return f'{greeting}, {number}!'

print(add_greeting('Hi', 10.4567))
