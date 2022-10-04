num = int(input('Enter N-number: '))
array = []
f = open('file.txt', 'w')
for i in range(-num, num+1):
    f.write(str(i) + '\n')
f.close
f = open('file.txt', 'r')
pos1 = int(input('Enter first position: '))
pos2 = int(input('Enter second position: '))
if 0 <= pos1 <= 2*num+1 and 0 <= pos2 <= 2*num+1:
    lines = f.readlines()
    print(int(lines[pos1])*int(lines[pos2]))
else:
    print('Incorrect number!')
f.close
