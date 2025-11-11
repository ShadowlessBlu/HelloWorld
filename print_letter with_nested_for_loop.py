numbers = [2, 2, 2, 2, 6, 6]

for number in numbers:
    output = ''
    for x in range(number):
        output += 'x'
    print(output)

#same code as the top
for number in numbers:
    print('x' * number)