def chain_slice(start, end, *args):
    from itertools import chain, islice
    return islice(chain(*args), start, end)

if __name__ == '__main__':
    print(*(chain_slice(17, 33, range(7),  range(8),  range(6),  range(9),  range(5))))

