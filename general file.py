print("Пожалуйста, откройте терминал на весь экран и перезапустите программу. это нужно для общего решения узора, иначе выдает графические проблемы")
z = int(input("Сколько нарисовать колец? "))  # кол-во колец

RED = '\u001b[41m  '
BLUE = '\u001b[44m  '
WHITE = '\u001b[47m  '
GREEN = '\u001b[48;5;34m  '
END = '\u001b[0m  '



print('-'*45,' ЗАДАНИЕ №1. ФЛАГ ','-'*45, sep='\n')

m=2
for i in range(1, 10+1):
    if i in [1,2,9,10]:  # в строках 1, 2, 9, 10 у нас будет следующий блок команд (далее аналогично)
        print(RED*5*m, end='')
    elif i in [3,4,7,8]:
        print(RED*2*m, WHITE*m, RED*2*m, sep='',end='')
    elif i in [5,6]:
        print(RED*m, WHITE*3*m, RED*m, sep='',end='')
    print("\u001b[0m")



print('-'*45,' ЗАДАНИЕ №2. УЗОР ','-'*45, sep='\n')

def fs(x):  # first-sixth line
    return print(END*x, BLUE*x, END*x, sep = '',end='')
def sf(x):  # second-fifth line
    return print(END, BLUE, END*2, BLUE, END, sep = '',end='')
def tf(x):  # third-fourth line
    return print(BLUE, END*x, END*x, BLUE, sep = '',end='')
M=z  # буфер

for y in range(1,6+1):
    if y == 1:
        while M!=0:
            M-=1
            fs(2)
        print()
        M=z

    elif y in [2,5]:
        while M!=0:
            M-=1
            sf(2)
        print()
        M=z

    elif y in [3,4]:
        while M!=0:
            M-=1
            tf(2)
        print()
        M=z
    elif y == 6:
        while M!=0:
            M-=1
            fs(2)
        break
print('\u001b[0m')



print('-'*45,' ЗАДАНИЕ №3. ГРАФИК y=x/3 ','-'*45, sep='\n')

print('Y')
for i in range(9):
    print(9-i, f'{'   '*(9*3-3*i-1)}{RED}{"   "}{END}')
print('  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27  X')



print('-'*45,' ЗАДАНИЕ №4. ПОСЛЕДОВАТЕЛЬСНОСТЬ ','-'*45, sep='\n')

a = [float(i) for i in open('sequence.txt')]
a.sort()
ans = []
another = []

for i in a:
    if -3 <= i <= 3:
        ans.append(i)
    else:
        another.append(i)

print(f'от -3 до 3 ({len(ans)}{' из 250)'}{GREEN}{' '*int(len(ans)/len(a)*100)}{END}{len(ans)/len(a)*100}{'%'}')
print(f'остальных ({len(another)}{' из 250)'}{BLUE}{' '*int(len(another)/len(a)*100)}{END}{len(another)/len(a)*100}{'%'}')



print('-'*45,' ЗАДАНИЕ №5(дополнительное). Анимация','-'*45, sep='\n')

END = ' \u001b[0m  '
import sys, time
def tic_tac_toe():
    print("\n\nReady, Set, Play!\n\n")
    for i in range(1,6):
        if i%2!=0:
            print("   ","|", "   ", "|")
        elif i%2==0:
            print("---"*5)
    while True:
        time.sleep(1)
        
        sys.stdout.write('\u001b[3A' + '\u001b[7C' + 'X')
        sys.stdout.flush()
        time.sleep(1)
        
        sys.stdout.write('\u001b[2A' + '\u001b[2D '+ 'O')
        sys.stdout.flush()
        time.sleep(1)
        
        sys.stdout.write('\u001b[5C' + 'X')
        sys.stdout.flush()
        time.sleep(1)
        
        sys.stdout.write('\u001b[13D' + '\u001b[4B' + 'O')
        sys.stdout.flush()
        time.sleep(1)
        
        sys.stdout.write('\u001b[11C' + 'X')
        sys.stdout.flush()
        time.sleep(1)
        
        sys.stdout.write('\u001b[2A' + '\u001b[1D' + 'O')
        sys.stdout.flush()
        time.sleep(1)
        
        sys.stdout.write('\u001b[2A' + '\u001b[13D' + 'X')
        sys.stdout.flush()
        time.sleep(1)
        break
    print("\u001b[6B \u001b[100D Партия!\n\n")

def loading():
    print('Loading...')
    for i in range(0,100):
        width = (i+1)//4
        time.sleep(0.04)
        sys.stdout.write(u"\u001b[1000D" + ' \\ ' + str(i + 1) + "%" + ' [' + '#'*width + ' '*(25-width) + ']')
        sys.stdout.flush()
        
        time.sleep(0.04)
        sys.stdout.write(u"\u001b[1000D" + ' | ' + str(i + 1) + "%" + ' [' + '#'*width + ' '*(25-width) + ']')
        sys.stdout.flush()

        time.sleep(0.04)
        sys.stdout.write(u"\u001b[1000D" + ' / ' + str(i + 1) + "%" + ' [' + '#'*width + ' '*(25-width) + ']')
        sys.stdout.flush()           #рабочая прога формата \ 15% [
        #                                                   | 15% [
        #                                                   / 15% [
    print(END)


loading()
tic_tac_toe()