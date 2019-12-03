def num_len(value):
    i = 0
    while value // 10 ** i:
        i += 1
    return i

def is_palindrome(value):
    if value%10 == 0:
        return 'NO'
    length = num_len(value)
    for i in range(length // 2):
        left_digit = (value//10**(length-i-1))%10
        right_digit = (value%10**(i+1))//10**i
        if not (left_digit == right_digit):
            return 'NO'
    return 'YES'


if __name__ == '__main__':
    while True:
        try:
            val = abs(int(input()))
        except ValueError:
            print('Value is not integer')
            continue
        except KeyboardInterrupt:
            exit()
    
        print(is_palindrome(val))
   
