from decimal import Decimal, getcontext

getcontext().prec = 1000

def print_header():
    print('{0:>10}{1:>10}{2:>10}{3:>60}'.format(
        'iteration', 'k', 'ans check', 'ans'))

def print_ans_data(length, k, check, val):
    print('{0:>10}{1:>10}{2:>10}{3:>60}'.format(
        length, k, check, val))

def is_int(val):
    return val.as_integer_ratio()[1] == 1

def ans_check(length, k, val):
    return (val*10 + k) * k == val + k*(10**length)

def magical_majestic_formula(length, k):
    """
    Моя выведенная формула.
    Возвращает ответ по длине числа.
    """
    return (k * 10**(length) - k**2)/(10*k - 1)

if __name__ == '__main__':
    print_header()
    for digit in range(10):
        k = Decimal(digit)
        length = Decimal(0)
        while True:
            val = magical_majestic_formula(length, k)
            if is_int(val):
                print_ans_data(length, k, ans_check(length, k, val), int(val)*10 + k)
                break
            length += 1

