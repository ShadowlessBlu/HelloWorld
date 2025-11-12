Number_Dictionary = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "0": "zero",
}
word_num = ''
p_num = input("Phone:")
for num in p_num:
    word_num += Number_Dictionary[num] + ' '
print(word_num)

output = ''
for ch in p_num:
    output += Number_Dictionary.get(ch, "!") + ' '
print(output)