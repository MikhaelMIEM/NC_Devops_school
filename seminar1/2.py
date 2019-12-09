def print_header():
    print('{0:>10}{1:>10}{2:>10}{3:>60}'.format(
        'iteration', 'k', 'ans check', 'ans'))

def print_ans_data(length, k, check, val):
    print('{0:>10}{1:>10}{2:>10}{3:>60}'.format(
        length, k, check, val))

def is_value_int(length, k):
    return (k * 10**(length) - k**2) % (10*k - 1) == 0

def ans_check(length, k, val):
    return (val*10 + k) * k == val + k*(10**length)

def magical_majestic_formula(length, k):
    """
    Моя выведенная формула.
    Возвращает ответ по длине числа.
    """
    return (k * 10**(length) - k**2) // (10*k - 1)

if __name__ == '__main__':
    print_header()
    for digit in range(10):
        k = digit
        length = 0
        while True:
            if is_value_int(length, k):
                val = magical_majestic_formula(length, k)
                print_ans_data(length, k, ans_check(length, k, val), int(val)*10 + k)
                break
            length += 1

