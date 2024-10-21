red = "\u001b[41m  "
white = "\u001b[47m  "

def end():
    return print(red*5*m, end='')
def middle():
    return print(red*2*m, white*m, red*2*m, sep='',end='')
def central():
    return print(red*m, white*3*m, red*m, sep='',end='')

m=2
for i in range(1, 10+1):
    if i in [1,2,9,10]:  # в строках 1, 2, 9, 10 у нас будет следующий блок команд (далее аналогично)
        end()
    elif i in [3,4,7,8]:
        middle()
    elif i in [5,6]:
        central()
    print("\u001b[0m")