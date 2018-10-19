
def under_limit(array_of_nums, limit):
    result = True
    for num in array_of_nums:
        if(num > limit):
            result = False

    return result


array = [10, 11, 14, 16, 17, 14, 35, 19, 21, 24, 23, 1, 6, 7]

print under_limit(array, 25)


