def print_star(n):
    row=0
    while row<n:
        col=0
        while col<=row:
            print('*',end='')
            col+=1
        print()
        row+=1
print_star(5)