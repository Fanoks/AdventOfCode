def merge(x = []):
    for i in x:
        y += i
    return y
def check(first, temp1, temp2, temp3):
    for number in numbers:
        if temp3 == number:
            temp3 = numbers[number]
            if first:
                temp1, temp2 = temp3, temp3
                first = False
                return first, temp1, temp2, temp3
            else:
                temp2 = temp3
                return first, temp1, temp2, temp3
numbers = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}
temp1, temp2, temp3, first, x, y, final = '', '', [], True, [], [], 0
f = open('a.txt', 'r')
for i in range(1000):
    x.append(f.readline())
for i in range(1000):
    for j in x[i]:
        if j.isdigit() and first == True:
            temp1, temp2 = j, j
            temp3 = ''
        elif j.isdigit():
            temp2 = j
            temp3 = ''
        else:
            if len(temp3) >= 3:
                if merge(temp3) == 'one':
                    pass
            else:
                temp3.append(j)
    temp3 = ''
    y.append(int((temp1 + temp2)))
for i in range(1000):
    final += y[i]
print(final)