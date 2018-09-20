for m in range(1,10):
    for n in range(1, m):
        print(end='       ')
    for q in range(m,10):
        print("{}*{}={:2} ".format(m,q,m*q),end='')
    print()
