def print_mul(n):
    row=1
    while row<=n:
        col=1
        while col<=row:
            print(row,"*",col,"=",row*col,end='  ')
            col+=1
        row+=1
        print()
print_mul(5)

