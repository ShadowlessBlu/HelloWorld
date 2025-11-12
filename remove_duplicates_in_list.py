numbers = [5, 5, 2, 2, 1, 1, 5, 5, 7, 7, 4, 4]
numbers2 = numbers.copy()
uniques = []

for i in numbers:
    while numbers.count(i) > 1:
        numbers.remove(i)
        numbers.sort()
print(numbers)

for num in numbers2:
    if num not in uniques:
        uniques.append(num)
print(uniques)

