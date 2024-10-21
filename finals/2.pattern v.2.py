b_s = '\u001b[44m  '  # blue space
w_s = '\u001b[47m  '  # white space

def fs(x):  # first-sixth line
    return print(w_s*x, b_s*x, w_s*x, sep = '',end='')

def sf(x):  # second-fifth line
    return print(w_s, b_s, w_s*2, b_s, w_s, sep = '',end='')

def tf(x):  # third-fourth line
    return print(b_s, w_s*x, w_s*x, b_s, sep = '',end='')

m = int(input("Сколько нарисовать колец? "))  # кол-во колец
M=m  # буфер

for y in range(1,6+1):
    if y == 1:
        while M!=0:
            M-=1
            fs(2)
        print()
        M=m

    elif y in [2,5]:
        while M!=0:
            M-=1
            sf(2)
        print()
        M=m

    elif y in [3,4]:
        while M!=0:
            M-=1
            tf(2)
        print()
        M=m

    elif y == 6:
        while M!=0:
            M-=1
            fs(2)
        break
print('\u001b[0m')