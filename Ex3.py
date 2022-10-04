num = int(input('Enter N-number:'))
sum=0
if num>=1:
    for i in range(1,num+1):
        sum+=(1+(1/i))**i
    print(round(sum,2))
else:
    print('Incorrect number!')