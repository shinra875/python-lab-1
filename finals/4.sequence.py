RED = '\u001b[41m'
BLUE = '\u001b[44m'
WHITE = '\u001b[47m'
GREEN = '\u001b[48;5;34m'
YELLOW = '\u001b[48;5;11m'
BLACK = '\u001b[48;5;16m'
END = '\u001b[0m'

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