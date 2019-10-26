def digitadd(num1):
    sum=0
    while(num1>0):
        digit=num1%10
        sum=digit+sum
        num1=num1//10
    return sum


