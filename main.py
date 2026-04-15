ten_digits = range(1,10)

for digit in ten_digits:
    if digit == 1:
        print(str(digit) + 'st')
    elif digit == 2:
        print(str(digit) + 'nd')
    elif digit == 3:
        print(str(digit) + 'rd')
    else:
        print(str(digit) + 'th')

