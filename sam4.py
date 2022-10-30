a=int(input('Enter the numbers'))
b=int(input())
c=int(input())
if a>b:
    if c>a:
        print('str(c)+ is greater')
    else:
        print('str(a)+ is greater')
if b>c:
    if a>b:
        print('str(a) is greater')
    else:
        print('str(b)+ is greater')
if a>c:
    if b>a:
        print('str(b) is greater')
    else:
        print('str(a) is greater')
