def diamond(n):
    if(n % 2 == 0 or n < 1):
        return null

    result = ''
    num = 1
    while (num <= n):
        for times in range(1,num):
            result += '*'
        
        result += '\n'
        num += 2
     
    return result
        

    




print diamond(3)