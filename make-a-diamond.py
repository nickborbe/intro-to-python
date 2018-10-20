def diamond(n):
    if(n % 2 == 0 or n < 1):
        return null

    result = ''

    for num in range(1, n+2, 2):
        for times in range(1, n - num/2):
            result += ' '

        for times in range(1, num+1):
            result += '*'
        
        result += '\n'

    
    for num in range(n-2, -1, -2):
        for times in range(n - num/2 , 1, -1):
            result += ' '

        for times in range(num+1, 1, -1):
            result += '*'

        result += '\n'



    return result
        

    


print diamond(7)