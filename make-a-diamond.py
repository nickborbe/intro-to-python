def diamond(n):
    if(n % 2 == 0 or n < 1):
        return null

    result = '*'
    for num in range(1, n):
        for times in range(1,num):
            result += '*'
        
        result += '\n'

    return result
        

    


print diamond(3)