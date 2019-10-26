def numpattern8(number):
    for row in range(1, number):
        for column in range(1, row + 1):
            print(column, end=' ')
        print("")
