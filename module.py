
i=1
j=1
def pattern(irow,icol):
    for i in range (irow):
        for j in range (icol):
            if((irow==icol) or (irow>icol)):
                print( '*' ,end=' ')
            else:
                pass
        print()