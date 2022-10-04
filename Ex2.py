num = int(input('Enter N-number:'))
mult = 2
if num == 1 or num == 2:
    print(num)
elif num > 2:
    for i in range(3, num+1):
        mult *= i
    print(mult)
else:
    print('Incorrect number!')
