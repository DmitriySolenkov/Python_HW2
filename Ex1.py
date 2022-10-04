num = int(input('Enter N-number:'))
if num >= 1:
    dictionary = {a: 3*a+1 for a in range(1, num+1)}
    print(dictionary)
else:
    print('Incorrect number!')
