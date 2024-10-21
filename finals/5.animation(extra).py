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