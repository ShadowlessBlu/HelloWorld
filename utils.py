def find_max(numbers):
    maxi = numbers[0]
    for num in numbers:
        if num > maxi:
            maxi = num
    return maxi
