def reverse_int(value):
    reversed_int = 0
    while value:
        reversed_int = reversed_int*10 + value%10
        value = value // 10
    return reversed_int

def is_palindrome(value):
    if value == reverse_int(value) and value%10 != 0:
        return 'Yes'
    else:
        return 'No'

if __name__ == '__main__':
    while True:
        try:
            val = abs(int(input()))
        except ValueError:
            print('Value is not integer')
            continue
        except KeyboardInterrupt:
            break
    
        print(is_palindrome(val))
   
