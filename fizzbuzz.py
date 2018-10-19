def fizzbuzz():
    for num in range(1,76):
        result = ''
        if(num % 3 == 0):
            result += 'fizz'
        if(num % 5 == 0):
            result += 'buzz'
        if(num % 5 != 0 and num % 3 != 0):
            result = num
        

        print result
   
   


fizzbuzz()