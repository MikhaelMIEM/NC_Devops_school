def stat_counter():
    func_calls = {}
    func = yield func_calls
    while True:
        def decorator(func):
            def wrapped(*args, **kwargs):
                if func not in func_calls:
                    func_calls[func] = 1
                else:
                    func_calls[func] += 1
                return func(*args, **kwargs)
            return wrapped
        func = yield decorator(func)

if __name__ == '__main__':
    statistic = stat_counter()
    function_calls_statistic = next(statistic)

    @statistic.send
    def f1(a):
        return a + 1

    @statistic.send
    def f2(a, b):
        return f1(a) + f1(b)

    print(f1(f2(2, 3) + f2(5, 6)))
    print(function_calls_statistic)
